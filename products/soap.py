from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from lxml import etree
from products.models import Product


SOAP_ENVELOPE_NS = "http://schemas.xmlsoap.org/soap/envelope/"
PRODUCT_NS = "http://product.soap.blinkit"


def create_soap_response(content):
    """Create a SOAP response envelope."""
    envelope = etree.Element(
        "{%s}Envelope" % SOAP_ENVELOPE_NS,
        nsmap={'soap': SOAP_ENVELOPE_NS, 'prod': PRODUCT_NS}
    )
    body = etree.SubElement(envelope, "{%s}Body" % SOAP_ENVELOPE_NS)
    body.append(content)
    return HttpResponse(
        etree.tostring(envelope, pretty_print=True, xml_declaration=True, encoding='UTF-8'),
        content_type='text/xml; charset=utf-8'
    )


def create_soap_fault(faultcode, faultstring):
    """Create a SOAP fault response."""
    envelope = etree.Element(
        "{%s}Envelope" % SOAP_ENVELOPE_NS,
        nsmap={'soap': SOAP_ENVELOPE_NS}
    )
    body = etree.SubElement(envelope, "{%s}Body" % SOAP_ENVELOPE_NS)
    fault = etree.SubElement(body, "{%s}Fault" % SOAP_ENVELOPE_NS)
    
    fc = etree.SubElement(fault, "faultcode")
    fc.text = faultcode
    
    fs = etree.SubElement(fault, "faultstring")
    fs.text = faultstring
    
    return HttpResponse(
        etree.tostring(envelope, pretty_print=True, xml_declaration=True, encoding='UTF-8'),
        content_type='text/xml; charset=utf-8',
        status=500
    )


@csrf_exempt
def product_soap_service(request):
    """Handle SOAP requests for Product operations."""
    if request.method == 'GET':
        # Return WSDL
        wsdl = generate_product_wsdl(request)
        return HttpResponse(wsdl, content_type='text/xml')
    
    if request.method != 'POST':
        return HttpResponse(status=405)
    
    try:
        # Parse SOAP request
        root = etree.fromstring(request.body)
        body = root.find('.//{%s}Body' % SOAP_ENVELOPE_NS)
        
        # Handle different operations
        if body.find('.//{%s}list_products' % PRODUCT_NS) is not None:
            return handle_list_products()
        elif body.find('.//{%s}get_product' % PRODUCT_NS) is not None:
            product_id = body.find('.//{%s}get_product/{%s}product_id' % (PRODUCT_NS, PRODUCT_NS))
            return handle_get_product(int(product_id.text) if product_id is not None else None)
        elif body.find('.//{%s}create_product' % PRODUCT_NS) is not None:
            return handle_create_product(body)
        else:
            return create_soap_fault('Client', 'Unknown operation')
            
    except Exception as e:
        return create_soap_fault('Server', str(e))


def handle_list_products():
    """Handle list_products SOAP operation."""
    products = Product.objects.all()[:10]
    
    response = etree.Element(
        "{%s}list_productsResponse" % PRODUCT_NS,
        nsmap={'prod': PRODUCT_NS}
    )
    
    for product in products:
        prod_elem = etree.SubElement(response, "{%s}product" % PRODUCT_NS)
        
        id_elem = etree.SubElement(prod_elem, "{%s}id" % PRODUCT_NS)
        id_elem.text = str(product.id)
        
        name_elem = etree.SubElement(prod_elem, "{%s}name" % PRODUCT_NS)
        name_elem.text = product.name
        
        sku_elem = etree.SubElement(prod_elem, "{%s}sku" % PRODUCT_NS)
        sku_elem.text = product.sku
        
        price_elem = etree.SubElement(prod_elem, "{%s}price" % PRODUCT_NS)
        price_elem.text = str(product.price)
        
        status_elem = etree.SubElement(prod_elem, "{%s}status" % PRODUCT_NS)
        status_elem.text = product.status
    
    return create_soap_response(response)


def handle_get_product(product_id):
    """Handle get_product SOAP operation."""
    if product_id is None:
        return create_soap_fault('Client', 'Product ID is required')
    
    try:
        product = Product.objects.get(id=product_id)
        
        response = etree.Element(
            "{%s}get_productResponse" % PRODUCT_NS,
            nsmap={'prod': PRODUCT_NS}
        )
        
        id_elem = etree.SubElement(response, "{%s}id" % PRODUCT_NS)
        id_elem.text = str(product.id)
        
        name_elem = etree.SubElement(response, "{%s}name" % PRODUCT_NS)
        name_elem.text = product.name
        
        sku_elem = etree.SubElement(response, "{%s}sku" % PRODUCT_NS)
        sku_elem.text = product.sku
        
        desc_elem = etree.SubElement(response, "{%s}description" % PRODUCT_NS)
        desc_elem.text = product.description
        
        price_elem = etree.SubElement(response, "{%s}price" % PRODUCT_NS)
        price_elem.text = str(product.price)
        
        return create_soap_response(response)
        
    except Product.DoesNotExist:
        return create_soap_fault('Client', 'Product not found')


def handle_create_product(body):
    """Handle create_product SOAP operation."""
    create_elem = body.find('.//{%s}create_product' % PRODUCT_NS)
    
    name = create_elem.find('.//{%s}name' % PRODUCT_NS).text
    sku = create_elem.find('.//{%s}sku' % PRODUCT_NS).text
    description = create_elem.find('.//{%s}description' % PRODUCT_NS).text
    price = create_elem.find('.//{%s}price' % PRODUCT_NS).text
    mrp = create_elem.find('.//{%s}mrp' % PRODUCT_NS).text
    category = create_elem.find('.//{%s}category' % PRODUCT_NS).text
    
    product = Product.objects.create(
        name=name,
        sku=sku.upper(),
        description=description,
        price=float(price),
        mrp=float(mrp),
        category=category,
        brand="Default",
        weight=0
    )
    
    response = etree.Element(
        "{%s}create_productResponse" % PRODUCT_NS,
        nsmap={'prod': PRODUCT_NS}
    )
    
    message_elem = etree.SubElement(response, "{%s}message" % PRODUCT_NS)
    message_elem.text = f"Product created successfully with ID: {product.id}"
    
    return create_soap_response(response)


def generate_product_wsdl(request):
    """Generate WSDL for Product SOAP service."""
    base_url = f"{request.scheme}://{request.get_host()}{request.path}"
    
    wsdl = f"""<?xml version="1.0" encoding="UTF-8"?>
<definitions name="ProductService"
             targetNamespace="http://product.soap.blinkit"
             xmlns="http://schemas.xmlsoap.org/wsdl/"
             xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
             xmlns:tns="http://product.soap.blinkit"
             xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    
    <types>
        <xsd:schema targetNamespace="http://product.soap.blinkit">
            <xsd:element name="list_products"/>
            <xsd:element name="list_productsResponse">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element name="product" type="tns:Product" minOccurs="0" maxOccurs="unbounded"/>
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
            
            <xsd:complexType name="Product">
                <xsd:sequence>
                    <xsd:element name="id" type="xsd:int"/>
                    <xsd:element name="name" type="xsd:string"/>
                    <xsd:element name="sku" type="xsd:string"/>
                    <xsd:element name="price" type="xsd:decimal"/>
                    <xsd:element name="status" type="xsd:string"/>
                </xsd:sequence>
            </xsd:complexType>
        </xsd:schema>
    </types>
    
    <message name="list_productsRequest">
        <part name="parameters" element="tns:list_products"/>
    </message>
    <message name="list_productsResponse">
        <part name="parameters" element="tns:list_productsResponse"/>
    </message>
    
    <portType name="ProductServicePortType">
        <operation name="list_products">
            <input message="tns:list_productsRequest"/>
            <output message="tns:list_productsResponse"/>
        </operation>
    </portType>
    
    <binding name="ProductServiceBinding" type="tns:ProductServicePortType">
        <soap:binding transport="http://schemas.xmlsoap.org/soap/http"/>
        <operation name="list_products">
            <soap:operation soapAction="list_products"/>
            <input>
                <soap:body use="literal"/>
            </input>
            <output>
                <soap:body use="literal"/>
            </output>
        </operation>
    </binding>
    
    <service name="ProductService">
        <port name="ProductServicePort" binding="tns:ProductServiceBinding">
            <soap:address location="{base_url}"/>
        </port>
    </service>
</definitions>"""
    
    return wsdl

