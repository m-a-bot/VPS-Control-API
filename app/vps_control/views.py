from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from app.vps_control.models import VPS
from app.vps_control.serializers import VPSSerializer


# Create your views here.
class VPSViewSet(ModelViewSet):
    queryset = VPS.objects.all()
    serializer_class = VPSSerializer
