from rest_framework import serializers

from app.vps_control.models import VPS, VPS_SERVER_STATUSES


class VPSServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VPS
        fields = "__all__"


class VPSServerStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VPS
        fields = ("status",)


class VPSServersFilterSerializer(serializers.Serializer):
    status = serializers.ChoiceField(
        choices=VPS_SERVER_STATUSES, required=False
    )

    min_cpu = serializers.IntegerField(required=False)
    max_cpu = serializers.IntegerField(required=False)

    min_ram = serializers.IntegerField(required=False)
    max_ram = serializers.IntegerField(required=False)

    min_hdd = serializers.IntegerField(required=False)
    max_hdd = serializers.IntegerField(required=False)
