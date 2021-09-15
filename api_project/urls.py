from django.contrib import admin
from django.urls import path, include

# drf_yasg document imports
from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
      openapi.Info(
          title="Client registration API",
          default_version='v1',
          description="This api is a challenger",
          terms_of_service="https://www.google.com/policies/terms/",
          contact=openapi.Contact(email="heltonteixeiradesouza@hotmail.com"),
          license=openapi.License(name="BSD License"),
        ),
      public=True,
      permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('clientes/', include('api_project.cadastro.urls')),
]
