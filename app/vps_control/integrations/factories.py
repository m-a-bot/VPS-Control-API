from app.vps_control.integrations.vps_server_api import VPSControlAPI
from app.vps_control.interfaces.vps_server_api_interface import IVPSControlAPI
from app.vps_control.stubs.vps_server_api_stub import VPSControlAPIStub


class VPSControlAPIBuilder:
    @staticmethod
    def build_service(url) -> IVPSControlAPI:
        if "test" in url:
            return VPSControlAPIStub()
        return VPSControlAPI()
