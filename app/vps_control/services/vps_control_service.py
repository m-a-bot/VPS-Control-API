from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response

from app.vps_control.integrations.factories import VPSControlAPIBuilder
from app.vps_control.models import VPS
from app.vps_control.repositories.vps_server_repository import (
    VPSServerRepository,
)
from app.vps_control.serializers import (
    VPSServerSerializer,
    VPSServersFilterSerializer,
    VPSServerStatusSerializer,
    VPSUpdatedServerSerializer,
)


class VPSControlService:

    def __init__(self):
        self._repository = VPSServerRepository()
        self.vps_control_api = VPSControlAPIBuilder.build_service("test")
        self.status_func_mapping = {
            "started": self._start_server,
            "blocked": self._block_server,
            "stopped": self._stop_server,
        }

    def get_server(self, uid):

        try:
            vps_server = self._repository.get_server(uid)
            serializer = VPSServerSerializer(vps_server)
            return Response(serializer.data)
        except VPS.DoesNotExist:
            return Response(
                {"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND
            )

    def get_servers(self, query_params):

        filter_serializer = VPSServersFilterSerializer(data=query_params)

        if not filter_serializer.is_valid():
            return Response(
                filter_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        query = self.__get_filter_query(filter_serializer.validated_data)

        vps_servers = self._repository.get_servers(query)

        serializer = VPSServerSerializer(vps_servers, many=True)

        return Response(serializer.data)

    def create_server(self, data):
        serializer = VPSServerSerializer(data=data)
        if serializer.is_valid():
            valid_data = serializer.validated_data

            self.vps_control_api.create_server(valid_data)

            vps = self._repository.create_server(valid_data)

            return Response(
                VPSServerSerializer(vps).data, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete_server(self, uid):

        try:
            self.vps_control_api.delete_server(uid)

            self._repository.delete_server(uid)

            return Response(status=status.HTTP_204_NO_CONTENT)
        except VPS.DoesNotExist:
            return Response(
                {"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND
            )

    def set_state(self, uid, data):
        serializer = VPSServerStatusSerializer(data=data)
        if serializer.is_valid():
            valid_data = serializer.validated_data
            server_status = valid_data["status"]
            try:
                func = self.status_func_mapping[server_status]
                func(uid)

                vps = self._repository.set_state_server(uid, valid_data)

                return Response(VPSUpdatedServerSerializer(vps).data)
            except VPS.DoesNotExist:
                return Response(
                    {"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _start_server(self, uid):
        self.vps_control_api.run_server(uid)

    def _block_server(self, uid):
        self.vps_control_api.block_server(uid)

    def _stop_server(self, uid):
        self.vps_control_api.stop_server(uid)

    def __get_filter_query(self, validated_data):

        server_status = validated_data.get("status")

        min_cpu = validated_data.get("min_cpu")
        max_cpu = validated_data.get("max_cpu")

        min_ram = validated_data.get("min_ram")
        max_ram = validated_data.get("max_ram")

        min_hdd = validated_data.get("min_hdd")
        max_hdd = validated_data.get("max_hdd")

        query = Q()

        if server_status:
            query &= Q(status=server_status)

        if min_cpu:
            query &= Q(cpu__gte=min_cpu)

        if max_cpu:
            query &= Q(cpu__lte=max_cpu)

        if min_ram:
            query &= Q(ram__gte=min_ram)

        if max_ram:
            query &= Q(ram__lte=max_ram)

        if min_hdd:
            query &= Q(hdd__gte=min_hdd)

        if max_hdd:
            query &= Q(hdd__lte=max_hdd)

        return query
