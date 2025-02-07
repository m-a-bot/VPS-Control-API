from app.vps_control.integrations.vps_server_api import VPSServerAPI
from app.vps_control.interfaces.vps_server_api_interface import IVPSServerAPI
from app.vps_control.stubs.vps_server_api_stub import VPSServerAPIStub


class VPSServerAPIBuilder:
    @staticmethod
    def build_service(url) -> IVPSServerAPI:
        if "test" in url:
            return VPSServerAPIStub()
        return VPSServerAPI()
