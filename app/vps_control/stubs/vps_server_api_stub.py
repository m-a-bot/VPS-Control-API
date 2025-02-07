from app.vps_control.interfaces.vps_server_api_interface import IVPSServerAPI


class VPSServerAPIStub(IVPSServerAPI):
    def __init__(self): ...

    def create_server(self, *args, **kwargs):
        pass

    def delete_server(self, *args, **kwargs):
        pass

    def run_server(self, *args, **kwargs):
        pass

    def block_server(self, *args, **kwargs):
        pass

    def stop_server(self, *args, **kwargs):
        pass
