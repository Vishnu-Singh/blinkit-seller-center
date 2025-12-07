from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def analytics_soap_service(request):
    """Simplified SOAP service for Analytics - returns basic XML response."""
    if request.method == 'GET':
        return HttpResponse("Analytics SOAP service. Access WSDL at ?wsdl", content_type='text/plain')
    return HttpResponse("Analytics SOAP endpoint", content_type='text/xml')
