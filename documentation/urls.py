from django.urls import path
from .views import (
    DocumentationHomeView,
    SetupGuideView,
    APIDocumentationView,
    APIEndpointDetailView,
    ChangelogView,
    ProjectStructureView,
)

app_name = 'documentation'

urlpatterns = [
    path('', DocumentationHomeView.as_view(), name='home'),
    path('setup/', SetupGuideView.as_view(), name='setup'),
    path('api/', APIDocumentationView.as_view(), name='api_docs'),
    path('api/<int:pk>/', APIEndpointDetailView.as_view(), name='endpoint_detail'),
    path('changelog/', ChangelogView.as_view(), name='changelog'),
    path('structure/', ProjectStructureView.as_view(), name='structure'),
]
