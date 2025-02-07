from django.db.models import Q
from rest_framework import status, viewsets
from rest_framework.response import Response

from app.vps_control.models import VPS
from app.vps_control.serializers import (
    VPSServerSerializer,
    VPSServersFilterSerializer,
    VPSServerStatusSerializer,
)


class VPSServerRepository:

    def get_server(self, pk=None):
        return VPS.objects.get(pk=pk)

    def get_servers(self, query):

        return VPS.objects.filter(query)

    def create_server(self, data):
        return VPS.objects.create(**data)

    def set_state_server(self, pk=None, data=None):
        VPS.objects.filter(pk=pk).update(**data)
        return self.get_server(pk)

    def delete_server(self, pk=None):
        vps_server = VPS.objects.get(pk=pk)
        vps_server.delete()
