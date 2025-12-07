from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import APIEndpoint, Changelog, SetupStep


class DocumentationHomeView(TemplateView):
    """Home page for documentation."""
    template_name = 'documentation/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_endpoints'] = APIEndpoint.objects.filter(is_active=True).count()
        context['rest_endpoints'] = APIEndpoint.objects.filter(protocol='REST', is_active=True).count()
        context['soap_endpoints'] = APIEndpoint.objects.filter(protocol='SOAP', is_active=True).count()
        context['latest_version'] = Changelog.objects.first()
        return context


class SetupGuideView(ListView):
    """View for setup instructions."""
    model = SetupStep
    template_name = 'documentation/setup_guide.html'
    context_object_name = 'steps'
    
    def get_queryset(self):
        return SetupStep.objects.all()


class APIDocumentationView(ListView):
    """View for API documentation."""
    model = APIEndpoint
    template_name = 'documentation/api_docs.html'
    context_object_name = 'endpoints'
    
    def get_queryset(self):
        queryset = APIEndpoint.objects.filter(is_active=True)
        
        # Filter by protocol if specified
        protocol = self.request.GET.get('protocol')
        if protocol:
            queryset = queryset.filter(protocol=protocol)
        
        # Filter by app if specified
        app_name = self.request.GET.get('app')
        if app_name:
            queryset = queryset.filter(app_name=app_name)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Group endpoints by app
        apps = APIEndpoint.objects.filter(is_active=True).values_list('app_name', flat=True).distinct()
        context['apps'] = sorted(set(apps))
        
        # Get unique protocols
        context['protocols'] = ['REST', 'SOAP']
        
        # Get current filters
        context['current_protocol'] = self.request.GET.get('protocol', '')
        context['current_app'] = self.request.GET.get('app', '')
        
        return context


class APIEndpointDetailView(DetailView):
    """Detailed view for a single API endpoint."""
    model = APIEndpoint
    template_name = 'documentation/endpoint_detail.html'
    context_object_name = 'endpoint'


class ChangelogView(ListView):
    """View for changelog."""
    model = Changelog
    template_name = 'documentation/changelog.html'
    context_object_name = 'changes'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = Changelog.objects.all()
        
        # Filter by version if specified
        version = self.request.GET.get('version')
        if version:
            queryset = queryset.filter(version=version)
        
        # Filter by change type if specified
        change_type = self.request.GET.get('type')
        if change_type:
            queryset = queryset.filter(change_type=change_type)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get unique versions
        context['versions'] = Changelog.objects.values_list('version', flat=True).distinct()
        
        # Get change types
        context['change_types'] = ['feature', 'enhancement', 'bugfix', 'breaking', 'documentation']
        
        return context


class ProjectStructureView(TemplateView):
    """View for project structure documentation."""
    template_name = 'documentation/project_structure.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Define project structure
        context['structure'] = {
            'Apps': [
                {'name': 'products', 'description': 'Product catalog management (SKU, pricing, inventory status)'},
                {'name': 'orders', 'description': 'Order lifecycle and fulfillment tracking'},
                {'name': 'inventory', 'description': 'Stock level management across warehouses'},
                {'name': 'catalog', 'description': 'Category hierarchy and brand management'},
                {'name': 'seller', 'description': 'Seller onboarding and verification (GSTIN/PAN validation)'},
                {'name': 'analytics', 'description': 'Sales reports and product performance metrics'},
                {'name': 'documentation', 'description': 'Project documentation and API reference'},
            ],
            'Technologies': [
                {'name': 'Django 6.0', 'purpose': 'Web framework'},
                {'name': 'Django REST Framework 3.16.1', 'purpose': 'REST API framework'},
                {'name': 'django-filter 25.2', 'purpose': 'Advanced filtering'},
                {'name': 'lxml 6.0.2', 'purpose': 'XML processing for SOAP'},
                {'name': 'zeep 4.3.2', 'purpose': 'SOAP client library'},
            ]
        }
        
        return context
