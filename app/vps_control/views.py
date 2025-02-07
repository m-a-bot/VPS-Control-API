from django.db.models import Q
from rest_framework import status, viewsets
from rest_framework.response import Response

from app.vps_control.models import VPS
from app.vps_control.serializers import (
    VPSServerSerializer,
    VPSServersFilterSerializer,
    VPSServerStatusSerializer,
)


class VPSViewSet(viewsets.ViewSet):
    def list(self, request):

        filter_serializer = VPSServersFilterSerializer(
            data=request.query_params
        )

        if not filter_serializer.is_valid():
            return Response(
                filter_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        server_status = filter_serializer.validated_data.get("status")

        min_cpu = filter_serializer.validated_data.get("min_cpu")
        max_cpu = filter_serializer.validated_data.get("max_cpu")

        min_ram = filter_serializer.validated_data.get("min_ram")
        max_ram = filter_serializer.validated_data.get("max_ram")

        min_hdd = filter_serializer.validated_data.get("min_hdd")
        max_hdd = filter_serializer.validated_data.get("max_hdd")

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

        vps_servers = VPS.objects.filter(query)

        serializer = VPSServerSerializer(vps_servers, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            vps_server = VPS.objects.get(pk=pk)
            serializer = VPSServerSerializer(vps_server)
            return Response(serializer.data)
        except VPS.DoesNotExist:
            return Response(
                {"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND
            )

    def create(self, request):
        serializer = VPSServerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            vps_server = VPS.objects.get(pk=pk)
        except VPS.DoesNotExist:
            return Response(
                {"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = VPSServerStatusSerializer(
            vps_server, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            vps_server = VPS.objects.get(pk=pk)
            vps_server.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except VPS.DoesNotExist:
            return Response(
                {"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND
            )
