# ABC nie pozwoli utworzyć obiektu z niezaimplementowanymi metodami

from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def turn_on(self) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        pass

    @abstractmethod
    def get_status(self) -> bool:
        pass


class Service:
    def __init__(self):
        self.devices = []

    def register_device(self, device: Device) -> None:
        device.connect()
        self.devices.append(device)


class TV(Device):
    def __init__(self):
        self._status = False

    # def connect(self) -> str:
    #     return "TV"

    def turn_on(self) -> None:
        self._status = True

    def turn_off(self) -> None:
        self._status = False

    def get_status(self) -> bool:
        return self._status


class Radio(Device):
    def __init__(self):
        self._status = False

    def connect(self) -> str:
        return "Radio"

    def turn_on(self) -> None:
        self._status = True

    def turn_off(self) -> None:
        self._status = False

    def get_status(self) -> bool:
        return self._status



service = Service()

tv = TV()
radio = Radio()

service.register_device(tv)
service.register_device(radio)


print(radio.turn_on())
print(radio.get_status())
# True
print(tv.turn_on())
print(tv.get_status())
# True
from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def turn_on(self) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        pass

    @abstractmethod
    def get_status(self) -> bool:
        pass


class Service:
    def __init__(self):
        self.devices = []

    def register_device(self, device: Device) -> None:
        device.connect()
        self.devices.append(device)


class TV(Device):
    def __init__(self):
        self._status = False

    # def connect(self) -> str:
    #     return "TV"

    def turn_on(self) -> None:
        self._status = True

    def turn_off(self) -> None:
        self._status = False

    def get_status(self) -> bool:
        return self._status


class Radio(Device):
    def __init__(self):
        self._status = False

    def connect(self) -> str:
        return "Radio"

    def turn_on(self) -> None:
        self._status = True

    def turn_off(self) -> None:
        self._status = False

    def get_status(self) -> bool:
        return self._status



service = Service()

tv = TV()
radio = Radio()

service.register_device(tv)
service.register_device(radio)


print(radio.turn_on())
print(radio.get_status())
# True
print(tv.turn_on())
print(tv.get_status())
# True
