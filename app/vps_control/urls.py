from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app.vps_control.views import VPSViewSet

router = DefaultRouter()
router.register(r"vps_servers", VPSViewSet, basename="vps_server")

urlpatterns = [path("", include(router.urls))]
