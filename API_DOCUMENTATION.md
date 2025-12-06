# Blinkit Seller Center - API Documentation

## Overview
This document provides detailed information about all available API endpoints in the Blinkit Seller Center application.

## Base URLs
- **REST API**: `http://localhost:8000/api/`
- **SOAP API**: `http://localhost:8000/soap/`
- **Admin**: `http://localhost:8000/admin/`

---

## REST API Endpoints

### 1. Products API

**Base Path**: `/api/products/`

#### List Products
- **Endpoint**: `GET /api/products/`
- **Description**: Get a paginated list of all products
- **Query Parameters**:
  - `status` - Filter by status (active, inactive, out_of_stock)
  - `category` - Filter by category
  - `brand` - Filter by brand
  - `search` - Search in name, sku, description
  - `ordering` - Order by field (created_at, price, name)

#### Create Product
- **Endpoint**: `POST /api/products/`
- **Request Body**:
```json
{
  "name": "Product Name",
  "sku": "SKU001",
  "description": "Product description",
  "price": 99.99,
  "mrp": 120.00,
  "category": "Electronics",
  "brand": "BrandName",
  "status": "active",
  "weight": 0.5
}
```

#### Get Product Details
- **Endpoint**: `GET /api/products/{id}/`
- **Description**: Get detailed information about a specific product

#### Update Product
- **Endpoint**: `PUT /api/products/{id}/`
- **Endpoint**: `PATCH /api/products/{id}/` (Partial update)

#### Delete Product
- **Endpoint**: `DELETE /api/products/{id}/`

#### Custom Actions
- **Get Active Products**: `GET /api/products/active/`
- **Deactivate Product**: `POST /api/products/{id}/deactivate/`

---

### 2. Orders API

**Base Path**: `/api/orders/`

#### List Orders
- **Endpoint**: `GET /api/orders/`
- **Query Parameters**:
  - `status` - Filter by status
  - `payment_method` - Filter by payment method
  - `search` - Search in order_id, customer_name, customer_phone

#### Create Order
- **Endpoint**: `POST /api/orders/`
- **Request Body**:
```json
{
  "order_id": "ORD001",
  "customer_name": "John Doe",
  "customer_phone": "+919876543210",
  "customer_address": "123 Main St, City",
  "total_amount": 250.00,
  "payment_method": "UPI",
  "status": "pending"
}
```

#### Update Order Status
- **Endpoint**: `POST /api/orders/{id}/update_status/`
- **Request Body**:
```json
{
  "status": "confirmed"
}
```

#### Custom Actions
- **Get Pending Orders**: `GET /api/orders/pending/`

---

### 3. Inventory API

**Base Path**: `/api/inventory/`

#### List Inventory
- **Endpoint**: `GET /api/inventory/`
- **Query Parameters**:
  - `warehouse_location` - Filter by warehouse
  - `search` - Search in product_sku, product_name

#### Create Inventory Item
- **Endpoint**: `POST /api/inventory/`
- **Request Body**:
```json
{
  "product_sku": "SKU001",
  "product_name": "Product Name",
  "available_quantity": 100,
  "reserved_quantity": 10,
  "warehouse_location": "Warehouse A",
  "low_stock_threshold": 20
}
```

#### Update Stock
- **Endpoint**: `POST /api/inventory/{id}/update_stock/`
- **Request Body**:
```json
{
  "available_quantity": 150
}
```

#### Custom Actions
- **Get Low Stock Items**: `GET /api/inventory/low_stock/`

---

### 4. Catalog API

**Base Path**: `/api/categories/` and `/api/brands/`

#### Categories

**List Categories**
- **Endpoint**: `GET /api/categories/`
- **Query Parameters**:
  - `is_active` - Filter by active status
  - `parent_category` - Filter by parent category

**Create Category**
- **Endpoint**: `POST /api/categories/`
- **Request Body**:
```json
{
  "name": "Category Name",
  "description": "Category description",
  "is_active": true,
  "display_order": 1
}
```

**Get Root Categories**
- **Endpoint**: `GET /api/categories/root/`

#### Brands

**List Brands**
- **Endpoint**: `GET /api/brands/`

**Create Brand**
- **Endpoint**: `POST /api/brands/`
- **Request Body**:
```json
{
  "name": "Brand Name",
  "description": "Brand description",
  "logo_url": "https://example.com/logo.png",
  "is_active": true
}
```

**Get Active Brands**
- **Endpoint**: `GET /api/brands/active/`

---

### 5. Seller API

**Base Path**: `/api/sellers/`

#### List Sellers
- **Endpoint**: `GET /api/sellers/`
- **Query Parameters**:
  - `is_active` - Filter by active status
  - `is_verified` - Filter by verification status

#### Create Seller
- **Endpoint**: `POST /api/sellers/`
- **Request Body**:
```json
{
  "seller_id": "SELL001",
  "business_name": "Business Name",
  "contact_name": "Contact Person",
  "email": "seller@example.com",
  "phone": "+919876543210",
  "address": "Business Address",
  "gstin": "22AAAAA0000A1Z5",
  "pan": "AAAAA0000A",
  "bank_account": "1234567890",
  "bank_ifsc": "ABCD0123456"
}
```

#### Verify Seller
- **Endpoint**: `POST /api/sellers/{id}/verify/`

#### Custom Actions
- **Get Active Sellers**: `GET /api/sellers/active/`

---

### 6. Analytics API

**Base Path**: `/api/sales-reports/` and `/api/product-performance/`

#### Sales Reports

**List Sales Reports**
- **Endpoint**: `GET /api/sales-reports/`
- **Query Parameters**:
  - `date` - Filter by date

**Create Sales Report**
- **Endpoint**: `POST /api/sales-reports/`
- **Request Body**:
```json
{
  "date": "2024-12-06",
  "total_orders": 150,
  "total_revenue": 50000.00,
  "total_items_sold": 500,
  "average_order_value": 333.33,
  "cancelled_orders": 5,
  "returned_orders": 2
}
```

**Get Sales Summary**
- **Endpoint**: `GET /api/sales-reports/summary/`

#### Product Performance

**List Product Performance**
- **Endpoint**: `GET /api/product-performance/`

**Get Top Performers**
- **Endpoint**: `GET /api/product-performance/top_performers/`

---

## SOAP API Endpoints

### Products SOAP Service

**Endpoint**: `http://localhost:8000/soap/products/`

**WSDL**: `http://localhost:8000/soap/products/?wsdl`

#### Available Operations:
- `list_products()` - List all products
- `get_product(product_id)` - Get product by ID
- `create_product(name, sku, description, price, mrp, category)` - Create a product

**Example SOAP Request**:
```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
                  xmlns:prod="http://product.soap.blinkit">
   <soapenv:Header/>
   <soapenv:Body>
      <prod:list_products/>
   </soapenv:Body>
</soapenv:Envelope>
```

### Other SOAP Services

All other SOAP services follow similar patterns:

- **Orders**: `http://localhost:8000/soap/orders/`
- **Inventory**: `http://localhost:8000/soap/inventory/`
- **Catalog**: `http://localhost:8000/soap/catalog/`
- **Seller**: `http://localhost:8000/soap/seller/`
- **Analytics**: `http://localhost:8000/soap/analytics/`

---

## Response Format

### REST API
All REST API responses follow this format:

**Success Response**:
```json
{
  "id": 1,
  "name": "Product Name",
  "sku": "SKU001",
  ...
}
```

**List Response** (with pagination):
```json
{
  "count": 100,
  "next": "http://localhost:8000/api/products/?page=2",
  "previous": null,
  "results": [
    {...},
    {...}
  ]
}
```

**Error Response**:
```json
{
  "field_name": [
    "Error message"
  ]
}
```

### SOAP API
SOAP responses are in XML format following SOAP 1.1 specification.

---

## Authentication

Currently, the API does not require authentication. For production use, implement:
- Token-based authentication for REST APIs
- WS-Security for SOAP APIs

---

## Rate Limiting

No rate limiting is implemented in the current version.

---

## Error Codes

### REST API
- `200` - Success
- `201` - Created
- `400` - Bad Request
- `404` - Not Found
- `500` - Internal Server Error

### SOAP API
- SOAP Fault with appropriate faultcode and faultstring

---

## Testing

### Using cURL (REST)
```bash
# List products
curl http://localhost:8000/api/products/

# Create a product
curl -X POST http://localhost:8000/api/products/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Test Product","sku":"TEST001","description":"Test","price":100,"mrp":120,"category":"Test","brand":"Test","weight":1.0}'
```

### Using Browser
Navigate to `http://localhost:8000/api/products/` to access the Django REST Framework browsable API.

### Using SOAP UI
1. Import WSDL: `http://localhost:8000/soap/products/?wsdl`
2. Create and send SOAP requests

---

## Additional Information

- All datetime fields are in ISO 8601 format
- All monetary values are in decimal format with 2 decimal places
- SKU must be unique across products
- Order IDs must be unique
- GSTIN must be 15 characters
- PAN must be 10 characters
- IFSC must be 11 characters
