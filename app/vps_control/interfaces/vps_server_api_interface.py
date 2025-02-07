from abc import ABC, abstractmethod


class IVPSControlAPI(ABC):
    @abstractmethod
    def create_server(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def delete_server(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def run_server(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def block_server(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def stop_server(self, *args, **kwargs):
        raise NotImplementedError
