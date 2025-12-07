# Documentation App - User Guide

## Overview

The Documentation app provides an interactive web-based portal for the Blinkit Seller Center project. It serves as a comprehensive resource for developers and users to understand the project setup, API usage, and track changes.

## Features

### 1. Documentation Portal Home (`/docs/`)
- Dashboard with project statistics
- Quick access links to all sections
- Latest release information
- Key features overview

### 2. Setup Guide (`/docs/setup/`)
- Step-by-step installation instructions
- System requirements
- Dependencies list
- Troubleshooting section
- Customizable setup steps via admin

### 3. API Documentation (`/docs/api/`)
- Complete REST and SOAP API reference
- Filter by protocol (REST/SOAP) or app
- Detailed endpoint information with examples
- Request/response examples
- Parameter documentation

### 4. Project Structure (`/docs/structure/`)
- Django apps overview
- Technology stack
- Directory structure
- Database models
- API architecture

### 5. Changelog (`/docs/changelog/`)
- Version history
- Feature additions
- Enhancements and bug fixes
- Breaking changes tracking
- Filter by version or change type

## Database Models

### APIEndpoint
Stores API endpoint documentation including:
- Endpoint name and path
- Protocol (REST/SOAP) and method
- Description and examples
- Request/response samples
- Query parameters

### Changelog
Tracks project changes:
- Version number
- Change type (feature, enhancement, bugfix, breaking, documentation)
- Title and description
- Affected app
- Release date

### SetupStep
Manages setup instructions:
- Step order and title
- Description and command
- Required/optional flag

## Usage

### Accessing Documentation
```
http://localhost:8000/docs/
```

### Populating Sample Data
```bash
python manage.py populate_docs
```

This command creates:
- 6 setup steps
- 10+ API endpoint examples
- 4 changelog entries

### Managing Documentation

All documentation can be managed through Django Admin:

1. **Add/Edit API Endpoints**: `/admin/documentation/apiendpoint/`
2. **Manage Changelog**: `/admin/documentation/changelog/`
3. **Update Setup Steps**: `/admin/documentation/setupstep/`

### Adding New API Documentation

Via Django Admin:
1. Go to `/admin/documentation/apiendpoint/add/`
2. Fill in the endpoint details:
   - Name, app, protocol, method
   - Path and description
   - Request/response examples
   - Parameters
3. Save

Via Python Shell:
```python
from documentation.models import APIEndpoint

APIEndpoint.objects.create(
    name='Example Endpoint',
    app_name='products',
    protocol='REST',
    method='GET',
    path='/api/products/example/',
    description='Example endpoint description',
    is_active=True
)
```

### Adding Changelog Entries

```python
from documentation.models import Changelog
from datetime import date

Changelog.objects.create(
    version='1.2.0',
    change_type='feature',
    title='New Feature',
    description='Description of the new feature',
    app_affected='products',
    release_date=date.today()
)
```

## Customization

### Templates
All templates are located in `documentation/templates/documentation/`:
- `base.html` - Base template with styling
- `home.html` - Home page
- `setup_guide.html` - Setup instructions
- `api_docs.html` - API documentation list
- `endpoint_detail.html` - Individual endpoint details
- `changelog.html` - Version history
- `project_structure.html` - Architecture overview

### Styling
The documentation uses embedded CSS in `base.html`. To customize:
1. Edit the `<style>` section in `base.html`
2. Modify colors, fonts, layout as needed
3. All pages inherit from `base.html`

## Benefits

1. **Centralized Documentation** - All project documentation in one place
2. **Easy Maintenance** - Update via Django Admin
3. **Version Control** - Track changes through changelog
4. **User-Friendly** - Clean, responsive interface
5. **Searchable** - Filter and search capabilities
6. **Examples Included** - Request/response samples for all APIs
7. **Always Up-to-Date** - Documentation lives with the code

## Future Enhancements

Potential improvements:
- API testing directly from documentation
- Interactive API explorer
- Code samples in multiple languages
- Search functionality across all documentation
- API versioning support
- Export documentation to PDF
- Dark mode theme
- Multi-language support

## Maintenance

### Regular Tasks
1. Update API documentation when adding new endpoints
2. Add changelog entries for each release
3. Keep setup instructions current
4. Review and update examples

### Best Practices
- Document all API endpoints
- Include examples for complex operations
- Keep changelog entries concise but informative
- Use consistent terminology
- Update version numbers appropriately

## Troubleshooting

### Documentation Not Loading
- Check if 'documentation' is in INSTALLED_APPS
- Verify URL configuration includes documentation.urls
- Run migrations: `python manage.py migrate`

### Empty Documentation Pages
- Run `python manage.py populate_docs` to load sample data
- Add entries via Django Admin

### Template Not Found
- Ensure templates are in `documentation/templates/documentation/`
- Check template names in views match actual files

## Support

For issues or questions:
1. Check Django logs for errors
2. Verify database migrations are applied
3. Review admin panel for data
4. Consult project README for setup instructions
