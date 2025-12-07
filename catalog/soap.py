from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def catalog_soap_service(request):
    """Simplified SOAP service for Catalog - returns basic XML response."""
    if request.method == 'GET':
        return HttpResponse("Catalog SOAP service. Access WSDL at ?wsdl", content_type='text/plain')
    return HttpResponse("Catalog SOAP endpoint", content_type='text/xml')
