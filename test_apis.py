#!/usr/bin/env python3
"""
Example script demonstrating how to use the Blinkit Seller Center APIs.
Run this after starting the Django server: python manage.py runserver
"""

import requests
import json

BASE_URL = "http://localhost:8000"


def test_rest_apis():
    """Test REST API endpoints."""
    print("=" * 60)
    print("Testing REST APIs")
    print("=" * 60)
    
    # Test Products API
    print("\n1. Testing Products API")
    print("-" * 40)
    
    # Create a product
    product_data = {
        "name": "Sample Product",
        "sku": "SKU12345",
        "description": "This is a sample product",
        "price": 99.99,
        "mrp": 120.00,
        "category": "Electronics",
        "brand": "SampleBrand",
        "weight": 0.5,
        "status": "active"
    }
    
    print("Creating a product...")
    response = requests.post(f"{BASE_URL}/api/products/", json=product_data)
    if response.status_code == 201:
        print(f"✓ Product created successfully!")
        product = response.json()
        product_id = product['id']
        print(f"  Product ID: {product_id}")
        print(f"  Name: {product['name']}")
    else:
        print(f"✗ Failed to create product: {response.status_code}")
        print(f"  {response.text}")
        return
    
    # List products
    print("\nListing all products...")
    response = requests.get(f"{BASE_URL}/api/products/")
    if response.status_code == 200:
        data = response.json()
        print(f"✓ Found {data['count']} products")
    else:
        print(f"✗ Failed to list products")
    
    # Test Orders API
    print("\n2. Testing Orders API")
    print("-" * 40)
    
    order_data = {
        "order_id": "ORD12345",
        "customer_name": "John Doe",
        "customer_phone": "+919876543210",
        "customer_address": "123 Main Street, City",
        "total_amount": 99.99,
        "payment_method": "UPI",
        "status": "pending"
    }
    
    print("Creating an order...")
    response = requests.post(f"{BASE_URL}/api/orders/", json=order_data)
    if response.status_code == 201:
        print(f"✓ Order created successfully!")
        order = response.json()
        print(f"  Order ID: {order['order_id']}")
    else:
        print(f"✗ Failed to create order: {response.status_code}")
    
    # Test Inventory API
    print("\n3. Testing Inventory API")
    print("-" * 40)
    
    inventory_data = {
        "product_sku": "SKU12345",
        "product_name": "Sample Product",
        "available_quantity": 100,
        "reserved_quantity": 10,
        "warehouse_location": "Warehouse A",
        "low_stock_threshold": 20
    }
    
    print("Creating inventory item...")
    response = requests.post(f"{BASE_URL}/api/inventory/", json=inventory_data)
    if response.status_code == 201:
        print(f"✓ Inventory item created successfully!")
    else:
        print(f"✗ Failed to create inventory: {response.status_code}")
    
    # Test Catalog API
    print("\n4. Testing Catalog API")
    print("-" * 40)
    
    category_data = {
        "name": "Electronics",
        "description": "Electronic items",
        "is_active": True,
        "display_order": 1
    }
    
    print("Creating a category...")
    response = requests.post(f"{BASE_URL}/api/categories/", json=category_data)
    if response.status_code == 201:
        print(f"✓ Category created successfully!")
    else:
        print(f"  Category may already exist: {response.status_code}")
    
    # Test Seller API
    print("\n5. Testing Seller API")
    print("-" * 40)
    
    seller_data = {
        "seller_id": "SELL001",
        "business_name": "Sample Business",
        "contact_name": "Jane Smith",
        "email": "seller@example.com",
        "phone": "+919876543210",
        "address": "Business Address",
        "gstin": "22AAAAA0000A1Z5",
        "pan": "AAAAA0000A",
        "bank_account": "1234567890",
        "bank_ifsc": "ABCD0123456"
    }
    
    print("Creating a seller...")
    response = requests.post(f"{BASE_URL}/api/sellers/", json=seller_data)
    if response.status_code == 201:
        print(f"✓ Seller created successfully!")
    else:
        print(f"  Seller may already exist: {response.status_code}")
    
    # Test Analytics API
    print("\n6. Testing Analytics API")
    print("-" * 40)
    
    print("Getting sales summary...")
    response = requests.get(f"{BASE_URL}/api/sales-reports/summary/")
    if response.status_code == 200:
        summary = response.json()
        print(f"✓ Sales Summary retrieved:")
        print(f"  Total Revenue: ${summary['total_revenue']}")
        print(f"  Total Orders: {summary['total_orders']}")
    else:
        print(f"✗ Failed to get sales summary")
    
    print("\n" + "=" * 60)
    print("REST API Testing Complete!")
    print("=" * 60)


def test_soap_apis():
    """Test SOAP API endpoints."""
    print("\n" + "=" * 60)
    print("Testing SOAP APIs")
    print("=" * 60)
    
    # Test Products SOAP API
    print("\n1. Testing Products SOAP API")
    print("-" * 40)
    
    # Get WSDL
    print("Getting WSDL...")
    response = requests.get(f"{BASE_URL}/soap/products/")
    if response.status_code == 200 and 'wsdl' in response.text.lower():
        print("✓ WSDL retrieved successfully!")
    else:
        print("✗ Failed to get WSDL")
    
    # Test list_products SOAP operation
    soap_envelope = """<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
                  xmlns:prod="http://product.soap.blinkit">
   <soapenv:Header/>
   <soapenv:Body>
      <prod:list_products/>
   </soapenv:Body>
</soapenv:Envelope>"""
    
    print("\nTesting list_products SOAP operation...")
    headers = {'Content-Type': 'text/xml; charset=utf-8'}
    response = requests.post(f"{BASE_URL}/soap/products/", 
                            data=soap_envelope, 
                            headers=headers)
    if response.status_code == 200:
        print("✓ SOAP request successful!")
        print(f"  Response length: {len(response.text)} bytes")
    else:
        print(f"✗ SOAP request failed: {response.status_code}")
    
    print("\n" + "=" * 60)
    print("SOAP API Testing Complete!")
    print("=" * 60)


if __name__ == "__main__":
    print("\nBlinkit Seller Center API Testing Script")
    print("Make sure the Django server is running on port 8000\n")
    
    try:
        # Test if server is running
        response = requests.get(f"{BASE_URL}/api/products/", timeout=2)
        
        # Run tests
        test_rest_apis()
        test_soap_apis()
        
        print("\n✓ All tests completed!")
        print("\nTo view the browsable API, open: http://localhost:8000/api/products/")
        print("To access Django admin, open: http://localhost:8000/admin/")
        
    except requests.exceptions.ConnectionError:
        print("✗ Error: Cannot connect to the server.")
        print("Please start the server with: python manage.py runserver")
    except Exception as e:
        print(f"✗ Error: {e}")
