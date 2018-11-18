from django.contrib import admin
from django.urls import path
from rest_framework import routers
from cars.views import CarViewSet, DocumentViewSet, validate_car, get_id_token, delete_car
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings


router = routers.SimpleRouter()
router.register(r'car', CarViewSet)
router.register(r'document', DocumentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^validate_car/$', validate_car),
    url(r'^get_id_token/$', get_id_token),
    url(r'^delete_car/$', delete_car)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
