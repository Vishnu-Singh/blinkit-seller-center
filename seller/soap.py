from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def seller_soap_service(request):
    """Simplified SOAP service for Seller - returns basic XML response."""
    if request.method == 'GET':
        return HttpResponse("Seller SOAP service. Access WSDL at ?wsdl", content_type='text/plain')
    return HttpResponse("Seller SOAP endpoint", content_type='text/xml')
