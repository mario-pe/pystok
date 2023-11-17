#protocol bazuje buck tapingu pozwoli na utworzenie obiektu z dowolnymi metodami ale w momęcie uzycia bedzie sprawdzal czy metody istnieja
# zmniesza code capling
from typing import Protocol


class DeviceProtocol(Protocol):
    def connect(self) -> None:
        ...      # ... oznacza, że metoda nie ma implementacji mozna uzywać zamiast pass

    def turn_on(self) -> None:
        ...

    def turn_off(self) -> None:
        ...


class Diagnostic(Protocol):
    def get_status(self) -> bool:
        ...


class ServiceProtocol:
    def __init__(self):
        self.devices = []

    def register_device(self, device: DeviceProtocol) -> None:
        device.connect()
        self.devices.append(device)


class TV:
    def connect(self) -> str:
        return "TV"

    def turn_on(self) -> None:
        self._status = True

    def turn_off(self) -> None:
        self._status = False

    def get_status(self) -> bool:
        return self._status


class Radio:
    # def connect(self) -> str:
    #     return "Radio"

    def turn_on(self) -> None:
        self._status = True

    def turn_off(self) -> None:
        self._status = False

    def get_status(self) -> bool:
        return self._status


tv = TV()
radio = Radio()

service_protocol = ServiceProtocol()
service_protocol.register_device(tv)
service_protocol.register_device(radio)



print(radio.turn_on())
print(radio.get_status())
# True
print(tv.turn_on())
print(tv.get_status())
# True
