from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def inventory_soap_service(request):
    """Simplified SOAP service for Inventory - returns basic XML response."""
    if request.method == 'GET':
        return HttpResponse("Inventory SOAP service. Access WSDL at ?wsdl", content_type='text/plain')
    return HttpResponse("Inventory SOAP endpoint", content_type='text/xml')
