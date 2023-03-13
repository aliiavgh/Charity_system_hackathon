from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from config import settings


schema_view = get_schema_view(
    openapi.Info(
        title='Charity system',
        default_version='v1',
        description='charity foundations'
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
