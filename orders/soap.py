from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from lxml import etree


@csrf_exempt
def order_soap_service(request):
    """Simplified SOAP service for Orders - returns basic XML response."""
    if request.method == 'GET':
        return HttpResponse("Orders SOAP service. Access WSDL at ?wsdl", content_type='text/plain')
    return HttpResponse("Orders SOAP endpoint", content_type='text/xml')
