from django.core.management.base import BaseCommand
from documentation.models import APIEndpoint, Changelog, SetupStep
from datetime import date


class Command(BaseCommand):
    help = 'Populate sample documentation data'

    def handle(self, *args, **options):
        self.stdout.write('Populating documentation data...')
        
        # Clear existing data
        APIEndpoint.objects.all().delete()
        Changelog.objects.all().delete()
        SetupStep.objects.all().delete()
        
        # Create Setup Steps
        setup_steps = [
            {
                'order': 1,
                'title': 'Clone the Repository',
                'description': 'Clone the Blinkit Seller Center repository from GitHub to your local machine.',
                'command': 'git clone https://github.com/Vishnu-Singh/blinkit-seller-center.git\ncd blinkit-seller-center',
                'is_required': True
            },
            {
                'order': 2,
                'title': 'Install Dependencies',
                'description': 'Install all required Python packages using pip.',
                'command': 'pip install -r requirements.txt',
                'is_required': True
            },
            {
                'order': 3,
                'title': 'Run Database Migrations',
                'description': 'Create database tables by running Django migrations.',
                'command': 'python manage.py migrate',
                'is_required': True
            },
            {
                'order': 4,
                'title': 'Create Superuser',
                'description': 'Create an admin user to access the Django admin panel.',
                'command': 'python manage.py createsuperuser',
                'is_required': False
            },
            {
                'order': 5,
                'title': 'Populate Documentation',
                'description': 'Load sample documentation data (optional but recommended).',
                'command': 'python manage.py populate_docs',
                'is_required': False
            },
            {
                'order': 6,
                'title': 'Start Development Server',
                'description': 'Run the Django development server.',
                'command': 'python manage.py runserver',
                'is_required': True
            },
        ]
        
        for step_data in setup_steps:
            SetupStep.objects.create(**step_data)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(setup_steps)} setup steps'))
        
        # Create API Endpoints
        api_endpoints = [
            # Products REST APIs
            {
                'name': 'List Products',
                'app_name': 'products',
                'protocol': 'REST',
                'method': 'GET',
                'path': '/api/products/',
                'description': 'Retrieve a paginated list of all products with filtering and search capabilities.',
                'parameters': 'Query Parameters:\n- status: Filter by status (active, inactive, out_of_stock)\n- category: Filter by category\n- brand: Filter by brand\n- search: Search in name, SKU, description\n- ordering: Order by field (created_at, price, name)',
                'response_example': '{\n  "count": 100,\n  "next": "http://localhost:8000/api/products/?page=2",\n  "previous": null,\n  "results": [\n    {\n      "id": 1,\n      "name": "Sample Product",\n      "sku": "SKU001",\n      "price": "99.99",\n      "status": "active"\n    }\n  ]\n}'
            },
            {
                'name': 'Create Product',
                'app_name': 'products',
                'protocol': 'REST',
                'method': 'POST',
                'path': '/api/products/',
                'description': 'Create a new product in the catalog.',
                'request_example': '{\n  "name": "New Product",\n  "sku": "SKU123",\n  "description": "Product description",\n  "price": 99.99,\n  "mrp": 120.00,\n  "category": "Electronics",\n  "brand": "BrandName",\n  "weight": 0.5\n}',
                'response_example': '{\n  "id": 1,\n  "name": "New Product",\n  "sku": "SKU123",\n  "price": "99.99",\n  "status": "active",\n  "created_at": "2024-12-07T00:00:00Z"\n}'
            },
            {
                'name': 'Get Product Details',
                'app_name': 'products',
                'protocol': 'REST',
                'method': 'GET',
                'path': '/api/products/{id}/',
                'description': 'Retrieve detailed information about a specific product.',
                'parameters': 'Path Parameters:\n- id: Product ID (integer)',
            },
            {
                'name': 'Deactivate Product',
                'app_name': 'products',
                'protocol': 'REST',
                'method': 'POST',
                'path': '/api/products/{id}/deactivate/',
                'description': 'Deactivate a product without deleting it.',
                'parameters': 'Path Parameters:\n- id: Product ID (integer)',
            },
            # Orders REST APIs
            {
                'name': 'List Orders',
                'app_name': 'orders',
                'protocol': 'REST',
                'method': 'GET',
                'path': '/api/orders/',
                'description': 'Retrieve a list of all orders with filtering options.',
                'parameters': 'Query Parameters:\n- status: Filter by order status\n- payment_method: Filter by payment method\n- search: Search by order ID, customer name, or phone',
            },
            {
                'name': 'Create Order',
                'app_name': 'orders',
                'protocol': 'REST',
                'method': 'POST',
                'path': '/api/orders/',
                'description': 'Create a new order.',
                'request_example': '{\n  "order_id": "ORD123",\n  "customer_name": "John Doe",\n  "customer_phone": "+919876543210",\n  "customer_address": "123 Main St",\n  "total_amount": 250.00,\n  "payment_method": "UPI"\n}',
            },
            {
                'name': 'Update Order Status',
                'app_name': 'orders',
                'protocol': 'REST',
                'method': 'POST',
                'path': '/api/orders/{id}/update_status/',
                'description': 'Update the status of an order.',
                'request_example': '{\n  "status": "confirmed"\n}',
            },
            # Inventory REST APIs
            {
                'name': 'List Inventory',
                'app_name': 'inventory',
                'protocol': 'REST',
                'method': 'GET',
                'path': '/api/inventory/',
                'description': 'Retrieve inventory levels for all products.',
                'parameters': 'Query Parameters:\n- warehouse_location: Filter by warehouse\n- search: Search by product SKU or name',
            },
            {
                'name': 'Get Low Stock Items',
                'app_name': 'inventory',
                'protocol': 'REST',
                'method': 'GET',
                'path': '/api/inventory/low_stock/',
                'description': 'Get all items with stock below threshold.',
            },
            # SOAP APIs
            {
                'name': 'list_products',
                'app_name': 'products',
                'protocol': 'SOAP',
                'method': 'SOAP',
                'path': '/soap/products/',
                'description': 'SOAP operation to list all products.',
                'request_example': '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"\n                  xmlns:prod="http://product.soap.blinkit">\n  <soapenv:Header/>\n  <soapenv:Body>\n    <prod:list_products/>\n  </soapenv:Body>\n</soapenv:Envelope>',
            },
        ]
        
        for endpoint_data in api_endpoints:
            APIEndpoint.objects.create(**endpoint_data)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(api_endpoints)} API endpoints'))
        
        # Create Changelog entries
        changelog_entries = [
            {
                'version': '1.1.0',
                'change_type': 'feature',
                'title': 'Documentation App Added',
                'description': 'Created a comprehensive documentation app with web-based interface for project setup, API documentation, and changelog tracking.',
                'app_affected': 'documentation',
                'release_date': date.today()
            },
            {
                'version': '1.0.0',
                'change_type': 'feature',
                'title': 'Initial Release',
                'description': 'Complete Django 6.0 project with 6 domain-specific apps, REST and SOAP APIs, and comprehensive admin interface.',
                'app_affected': '',
                'release_date': date(2024, 12, 6)
            },
            {
                'version': '1.0.0',
                'change_type': 'feature',
                'title': 'REST API Implementation',
                'description': 'Implemented 47+ REST API endpoints using Django REST Framework with advanced filtering, searching, and pagination.',
                'app_affected': 'all',
                'release_date': date(2024, 12, 6)
            },
            {
                'version': '1.0.0',
                'change_type': 'feature',
                'title': 'SOAP API Implementation',
                'description': 'Implemented 6 SOAP service endpoints with WSDL generation and proper fault handling.',
                'app_affected': 'all',
                'release_date': date(2024, 12, 6)
            },
        ]
        
        for changelog_data in changelog_entries:
            Changelog.objects.create(**changelog_data)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(changelog_entries)} changelog entries'))
        self.stdout.write(self.style.SUCCESS('Documentation data populated successfully!'))
