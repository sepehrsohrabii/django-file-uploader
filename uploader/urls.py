from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from uploader_app import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as authviews
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'UploadedFiles', views.UploadedFileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('UploadedFiles/', views.UploadedFile_list),
    path('UploadedFiles/<int:pk>', views.UploadedFile_detail),
    path('api-token-auth/', authviews.obtain_auth_token),
    path('swagger-ui/', TemplateView.as_view(
            template_name='swagger-ui.html',
            extra_context={'schema_url':'openapi-schema'}
        ), name='swagger-ui'),
    path('openapi/', get_schema_view(
            title="API schemaView",
            description="API for all things …",
            version="1.0.0"
        ), name='openapi-schema'),
]

