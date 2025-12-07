# Blinkit Seller Center API

A full-fledged Django project implementing Blinkit Seller Center APIs with both REST and SOAP endpoints.

## Project Structure

The application is organized into 7 Django apps based on API classification:

1. **Products** - Product management
2. **Orders** - Order management
3. **Inventory** - Stock management
4. **Catalog** - Category and brand management
5. **Seller** - Seller profile management
6. **Analytics** - Sales reports and analytics
7. **Documentation** - Interactive documentation portal

## Features

- ✅ Complete REST API implementation using Django REST Framework
- ✅ Complete SOAP API implementation using custom lxml-based solution
- ✅ Full CRUD operations for all resources
- ✅ Advanced filtering, searching, and ordering
- ✅ Django Admin interface for all models
- ✅ Interactive web-based documentation portal
- ✅ Comprehensive API documentation with examples

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Vishnu-Singh/blinkit-seller-center.git
cd blinkit-seller-center
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Populate documentation (optional but recommended):
```bash
python manage.py populate_docs
```

5. Create a superuser (for admin access):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Quick Access

- **Documentation Portal**: http://localhost:8000/docs/
- **REST API**: http://localhost:8000/api/
- **SOAP API**: http://localhost:8000/soap/
- **Admin Panel**: http://localhost:8000/admin/

## Documentation Portal

The project includes an interactive web-based documentation portal accessible at `/docs/` with the following sections:

- **Home** - Overview and quick statistics
- **Setup Guide** - Step-by-step installation instructions
- **API Documentation** - Complete API reference with examples
- **Project Structure** - Architecture and technology stack
- **Changelog** - Version history and changes

Access the documentation at: http://localhost:8000/docs/

## API Endpoints

### REST API Endpoints

All REST APIs are accessible at `http://localhost:8000/api/`

#### Products API (`/api/products/`)
- `GET /api/products/` - List all products
- `POST /api/products/` - Create a new product
- `GET /api/products/{id}/` - Retrieve a specific product
- `PUT /api/products/{id}/` - Update a product
- `PATCH /api/products/{id}/` - Partial update a product
- `DELETE /api/products/{id}/` - Delete a product
- `GET /api/products/active/` - List active products
- `POST /api/products/{id}/deactivate/` - Deactivate a product

#### Orders API (`/api/orders/`)
- `GET /api/orders/` - List all orders
- `POST /api/orders/` - Create a new order
- `GET /api/orders/{id}/` - Retrieve a specific order
- `PUT /api/orders/{id}/` - Update an order
- `PATCH /api/orders/{id}/` - Partial update an order
- `DELETE /api/orders/{id}/` - Delete an order
- `POST /api/orders/{id}/update_status/` - Update order status
- `GET /api/orders/pending/` - List pending orders

#### Inventory API (`/api/inventory/`)
- `GET /api/inventory/` - List all inventory items
- `POST /api/inventory/` - Create a new inventory item
- `GET /api/inventory/{id}/` - Retrieve a specific inventory item
- `PUT /api/inventory/{id}/` - Update an inventory item
- `PATCH /api/inventory/{id}/` - Partial update an inventory item
- `DELETE /api/inventory/{id}/` - Delete an inventory item
- `GET /api/inventory/low_stock/` - List low stock items
- `POST /api/inventory/{id}/update_stock/` - Update stock levels

#### Catalog API
**Categories** (`/api/categories/`)
- `GET /api/categories/` - List all categories
- `POST /api/categories/` - Create a new category
- `GET /api/categories/{id}/` - Retrieve a specific category
- `PUT /api/categories/{id}/` - Update a category
- `PATCH /api/categories/{id}/` - Partial update a category
- `DELETE /api/categories/{id}/` - Delete a category
- `GET /api/categories/root/` - List root categories

**Brands** (`/api/brands/`)
- `GET /api/brands/` - List all brands
- `POST /api/brands/` - Create a new brand
- `GET /api/brands/{id}/` - Retrieve a specific brand
- `PUT /api/brands/{id}/` - Update a brand
- `PATCH /api/brands/{id}/` - Partial update a brand
- `DELETE /api/brands/{id}/` - Delete a brand
- `GET /api/brands/active/` - List active brands

#### Seller API (`/api/sellers/`)
- `GET /api/sellers/` - List all sellers
- `POST /api/sellers/` - Create a new seller
- `GET /api/sellers/{id}/` - Retrieve a specific seller
- `PUT /api/sellers/{id}/` - Update a seller
- `PATCH /api/sellers/{id}/` - Partial update a seller
- `DELETE /api/sellers/{id}/` - Delete a seller
- `POST /api/sellers/{id}/verify/` - Verify a seller
- `GET /api/sellers/active/` - List active sellers

#### Analytics API
**Sales Reports** (`/api/sales-reports/`)
- `GET /api/sales-reports/` - List all sales reports
- `POST /api/sales-reports/` - Create a new sales report
- `GET /api/sales-reports/{id}/` - Retrieve a specific sales report
- `PUT /api/sales-reports/{id}/` - Update a sales report
- `PATCH /api/sales-reports/{id}/` - Partial update a sales report
- `DELETE /api/sales-reports/{id}/` - Delete a sales report
- `GET /api/sales-reports/summary/` - Get summary statistics

**Product Performance** (`/api/product-performance/`)
- `GET /api/product-performance/` - List all product performance reports
- `POST /api/product-performance/` - Create a new product performance report
- `GET /api/product-performance/{id}/` - Retrieve a specific product performance report
- `PUT /api/product-performance/{id}/` - Update a product performance report
- `PATCH /api/product-performance/{id}/` - Partial update a product performance report
- `DELETE /api/product-performance/{id}/` - Delete a product performance report
- `GET /api/product-performance/top_performers/` - Get top performing products

### SOAP API Endpoints

All SOAP APIs are accessible at `http://localhost:8000/soap/`

#### Products SOAP (`/soap/products/`)
- `get_product(product_id)` - Get product by ID
- `list_products()` - List all products
- `create_product(name, sku, description, price, mrp, category)` - Create a product
- `update_product_status(product_id, status)` - Update product status
- `delete_product(product_id)` - Delete a product

#### Orders SOAP (`/soap/orders/`)
- `get_order(order_id)` - Get order by ID
- `list_orders()` - List all orders
- `create_order(order_id, customer_name, customer_phone, customer_address, total_amount, payment_method)` - Create an order
- `update_order_status(order_id, status)` - Update order status
- `get_orders_by_status(status)` - Get orders by status

#### Inventory SOAP (`/soap/inventory/`)
- `get_inventory(inventory_id)` - Get inventory by ID
- `list_inventory()` - List all inventory items
- `create_inventory(product_sku, product_name, available_quantity, warehouse_location)` - Create inventory
- `update_stock(inventory_id, quantity)` - Update stock
- `get_low_stock_items()` - Get low stock items

#### Catalog SOAP (`/soap/catalog/`)
- `get_category(category_id)` - Get category by ID
- `list_categories()` - List all categories
- `create_category(name, description, is_active)` - Create a category
- `get_brand(brand_id)` - Get brand by ID
- `list_brands()` - List all brands
- `create_brand(name, description, is_active)` - Create a brand

#### Seller SOAP (`/soap/seller/`)
- `get_seller(seller_id)` - Get seller by ID
- `list_sellers()` - List all sellers
- `create_seller(seller_id, business_name, contact_name, email, phone, address, gstin, pan, bank_account, bank_ifsc)` - Create a seller
- `verify_seller(seller_id)` - Verify a seller
- `list_active_sellers()` - List active sellers

#### Analytics SOAP (`/soap/analytics/`)
- `get_sales_report(report_id)` - Get sales report by ID
- `list_sales_reports()` - List recent sales reports
- `get_sales_summary()` - Get overall sales summary
- `get_product_performance(performance_id)` - Get product performance by ID
- `get_top_performers()` - Get top performing products

## Testing the APIs

### Testing REST APIs

You can test REST APIs using:

1. **Django REST Framework Browsable API**: Navigate to any REST endpoint in a browser
2. **cURL**:
```bash
# List products
curl http://localhost:8000/api/products/

# Create a product
curl -X POST http://localhost:8000/api/products/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Product 1", "sku": "SKU001", "description": "Test product", "price": 100, "mrp": 120, "category": "Electronics", "brand": "TestBrand", "weight": 0.5}'
```

3. **Postman** or any other API testing tool

### Testing SOAP APIs

You can test SOAP APIs using:

1. **SOAP UI** or **Postman**
2. Access the WSDL at: `http://localhost:8000/soap/{app_name}/?wsdl`
   - Example: `http://localhost:8000/soap/products/?wsdl`

Example SOAP Request:
```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
                  xmlns:prod="product.soap.blinkit">
   <soapenv:Header/>
   <soapenv:Body>
      <prod:list_products/>
   </soapenv:Body>
</soapenv:Envelope>
```

## Django Admin

Access the admin interface at `http://localhost:8000/admin/`

You can manage all models (Products, Orders, Inventory, Categories, Brands, Sellers, Sales Reports, Product Performance) through the admin interface.

## Database

The project uses SQLite by default. The database file is `db.sqlite3` in the project root.

## Technologies Used

- **Django 6.0** - Web framework
- **Django REST Framework 3.16.1** - REST API framework
- **Spyne 2.14.0** - SOAP API framework
- **django-filter 25.2** - Advanced filtering
- **lxml 6.0.2** - XML processing
- **defusedxml 0.7.1** - Secure XML parsing

## Project Architecture

Each app follows Django's MVT (Model-View-Template) architecture with:
- **Models** - Database schema
- **Views** - Business logic (ViewSets for REST, ServiceBase for SOAP)
- **Serializers** - Data serialization for REST APIs
- **Admin** - Django admin configuration
- **URLs** - URL routing

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues and questions, please open an issue on GitHub.
