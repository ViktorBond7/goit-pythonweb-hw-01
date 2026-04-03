from abc import ABC, abstractmethod
from colorama import Fore, Style, init
import logging

init(autoreset=True)

logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler()],
)


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> None:
        raise NotImplementedError(
            "Метод start_engine() повинен бути реалізований в підкласах"
        )


class Car(Vehicle):
    def __init__(self, make: str, model: str):
        self.make: str = make
        self.model: str = model

    def start_engine(self) -> None:
        logging.info(
            f"{Fore.GREEN}{self.make} {self.model}{Style.RESET_ALL}: Двигун запущено"
        )


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str):
        self.make: str = make
        self.model: str = model

    def start_engine(self) -> None:
        logging.info(
            f"{Fore.BLUE}{self.make} {self.model}{Style.RESET_ALL}: Мотор заведено"
        )


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:

        raise NotImplementedError(
            "Метод create_car() повинен бути реалізований в підкласах"
        )

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        raise NotImplementedError(
            "Метод create_motorcycle() повинен бути реалізований в підкласах"
        )


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(f"{make} (US Spec)", model)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(f"{make} (US Spec)", model)


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(f"{make} (EU Spec)", model)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(f"{make} (EU Spec)", model)


if __name__ == "__main__":
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    car1 = us_factory.create_car("Ford", "Mustang")
    motorcycle1 = us_factory.create_motorcycle("Harley-Davidson", "Sportster")

    car2 = eu_factory.create_car("Volkswagen", "Golf")
    motorcycle2 = eu_factory.create_motorcycle("BMW", "R1200")

    car1.start_engine()
    motorcycle1.start_engine()
    car2.start_engine()
    motorcycle2.start_engine()
