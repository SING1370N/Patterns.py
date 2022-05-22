from __future__ import annotations
from abc import ABC, abstractmethod
from time import strftime, gmtime

class Cook(ABC):
    # Класс объявляет фабричный метод, который должен возвращать объект класса (еда).
    # Подклассы Создателя обычно предоставляют реализацию этого метода.
    @abstractmethod
    def factory_method(self):
        pass



    def make(self, time_cooking) -> str:
        # Вызываем фабричный метод, чтобы получить объект-продукт.
        product = self.factory_method()
        # Работа с продуктом.
        if strftime("%H", gmtime(time_cooking)) != '00':
            product.time_cooking = strftime("%H", gmtime(time_cooking))
            if strftime("%M", gmtime(time_cooking)) != '00':
                product.time_cooking += strftime(":%M", gmtime(time_cooking))
            if strftime("%S", gmtime(time_cooking)) != '00':
                product.time_cooking += strftime(":%S", gmtime(time_cooking)) + " ч."
            else:
                product.time_cooking += " ч."
        elif strftime("%M", gmtime(time_cooking)) != '00':
            if strftime("%S", gmtime(time_cooking)) == '00':
                product.time_cooking = strftime("%M", gmtime(time_cooking)) + " м."
            else:
                product.time_cooking = strftime("%M:%S", gmtime(time_cooking)) + " м."
        else:
            product.time_cooking = strftime("%S", gmtime(time_cooking)) + " c."
        result = f"Готовим {product.operation()} "
        return result


class CookingSoup(Cook):
    def factory_method(self) -> Product:
        return VegetableSoup()

class CookingJuice(Cook):
    def factory_method(self) -> Product:
        return Tomatojuice()

class CookingSalad(Cook):
    def factory_method(self) -> Product:
        return SaladCaesar()


class Product(ABC):
    """
    Интерфейс Продукта объявляет операции, которые должны выполнять все
    конкретные продукты.
    """
    @abstractmethod
    def operation(self) -> str:
        pass


class VegetableSoup(Product):
    def operation(self) -> str:
        return f"овощной суп за {self.time_cooking}"

class Tomatojuice(Product):
    def operation(self) -> str:
        return f"сок томатный за {self.time_cooking}"

class SaladCaesar(Product):
    def operation(self) -> str:
        return f"cалат <<Цезарь>> за {self.time_cooking}"


def client(creator: Cook, time = 30) -> None:
    print(creator.make(time))

if __name__ == "__main__":
    client(CookingSoup(), 3000)
    client(CookingSalad(), 8880)
    client(CookingJuice())