import logging

from app.vps_control.interfaces.vps_server_api_interface import IVPSControlAPI

logger = logging.getLogger(__name__)


class VPSControlAPIStub(IVPSControlAPI):
    def __init__(self):
        logger.info("Init test vps control api")

    def create_server(self, data):
        logger.info(f"VPS server created with parameters {data}")

    def delete_server(self, uid):
        logger.info(f"VPS server № {uid} deleted")

    def run_server(self, uid):
        logger.info(f"VPS server № {uid} was running")

    def block_server(self, uid):
        logger.info(f"VPS server № {uid} has been blocked")

    def stop_server(self, uid):
        logger.info(f"VPS server № {uid} has been stopped")
