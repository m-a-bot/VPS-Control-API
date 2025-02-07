from django.db.models import Q
from rest_framework import status, viewsets
from rest_framework.response import Response

from app.vps_control.models import VPS
from app.vps_control.serializers import (
    VPSServerSerializer,
    VPSServersFilterSerializer,
    VPSServerStatusSerializer,
)
from app.vps_control.services.vps_control_service import VPSControlService


class VPSViewSet(viewsets.ViewSet):
    def list(self, request):

        return VPSControlService().get_servers(request.query_params)

    def retrieve(self, request, pk=None):
        return VPSControlService().get_server(pk)

    def create(self, request):

        return VPSControlService().create_server(request.data)

    def partial_update(self, request, pk=None):

        return VPSControlService().set_state(pk, request.data)

    def destroy(self, request, pk=None):
        return VPSControlService().delete_server(pk)
