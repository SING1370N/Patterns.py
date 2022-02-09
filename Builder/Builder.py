from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

# Строитель - объявляет создающие методы для различных частей
class Cooking(ABC):

    @property
    @abstractmethod
    def ingredient(self) -> None:
        pass

    @abstractmethod
    def sausage(self) -> None:
        pass

    @abstractmethod
    def cheese(self) -> None:
        pass

    @abstractmethod
    def pineapples(self) -> None:
        pass



class ConcreteCooking(Cooking):

    def __init__(self) -> None:
        """
        Новый экземпляр строителя должен содержать пустой объект продукта,
        который используется в дальнейшей сборке.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Food()

    @property
    def ingredient(self) -> Food:

        product = self._product
        self.reset()
        return product

    def sausage(self) -> None:
        self._product.add("колбаска")

    def cheese(self) -> None:
        self._product.add("сыр")

    def pineapples(self) -> None:
        self._product.add("ананасы")


class Food:
    """
    Имеет смысл использовать паттерн Строитель только тогда, когда ваши продукты
    достаточно сложны и требуют обширной конфигурации.

    В отличие от других порождающих паттернов, различные конкретные строители
    могут производить несвязанные продукты. Другими словами, результаты
    различных строителей могут не всегда следовать одному и тому же интерфейсу.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_ingredient(self) -> None:
        print(f"Части продукта: {', '.join(self.parts)}", end="")


#   Повар отвечает только за выполнение шагов приготовления (необязателен, так как клиент может готовить сам)
class Cook:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Cooking:
        return self._builder

    @builder.setter
    def builder(self, builder: Cooking) -> None:
        """
        Директор работает с любым экземпляром строителя, который передаётся ему
        клиентским кодом. Таким образом, клиентский код может изменить конечный
        тип вновь собираемого продукта.
        """
        self._builder = builder

    def cooking_pizza_home(self) -> None:
        self.builder.sausage()

    def cooking_pizza_major(self) -> None:
        self.builder.sausage()
        self.builder.cheese()
        self.builder.pineapples()


if __name__ == "__main__":
    """
    Клиентский код создаёт объект-строитель, передаёт его директору, а затем
    инициирует процесс построения. Конечный результат извлекается из объекта-
    строителя.
    """

    cook = Cook()
    cooking = ConcreteCooking()
    cook.builder = cooking

    print("Пицца домашняя:")
    cook.cooking_pizza_home()
    cooking.ingredient.list_ingredient()

    print("\n")

    print("Пицца Мажор:")
    cook.cooking_pizza_major()
    cooking.ingredient.list_ingredient()

    print("\n")

    # Строитель без класса Директор.
    print("Пицца <<Сделай сам>>:")
    cooking.sausage()
    cooking.cheese()
    cooking.ingredient.list_ingredient()
