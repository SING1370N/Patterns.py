from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from random import randint


class Building(ABC):
    """
    Интерфейс Компонента объявляет метод accept, который в качестве аргумента
    может получать любой объект, реализующий интерфейс посетителя.

    Каждый Конкретный Компонент должен реализовать метод accept таким образом,
    чтобы он вызывал метод посетителя, соответствующий классу компонента.
    """

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass

    @abstractmethod
    def type_building(self) -> None:
        pass


class Home(Building):
    def accept(self, visitor: Visitor) -> None:
        """
        Обратите внимание, мы вызываем visit_home, что соответствует
        названию текущего класса. Таким образом мы позволяем
        посетителю узнать, с каким классом компонента он работает.
        """
        visitor.visit_home(self)

    @staticmethod
    def type_building():
        return "Дом"


class Factory(Building):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_factory(self)

    @staticmethod
    def type_building():
        return "Фабрика"


class Store(Building):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_store(self)

    @staticmethod
    def type_building():
        return "Магазин"

    """
    Конкретные Компоненты могут иметь особые методы, не объявленные в их
    базовом классе или интерфейсе. Посетитель всё же может использовать эти
    методы, поскольку он знает о конкретном классе компонента.
    """

    @staticmethod
    def buying(product: str) -> str:
        return f"купил {product} на {randint(1,2000)} грн. {randint(0,99)} коп."


class Visitor(ABC):
    """
    Интерфейс Посетителя объявляет набор методов посещения, соответствующих
    классам компонентов. Сигнатура метода посещения позволяет посетителю
    определить конкретный класс компонента, с которым он имеет дело.
    """

    @abstractmethod
    def visit_home(self, element: Home) -> None:
        pass

    @abstractmethod
    def visit_factory(self, element: Factory) -> None:
        pass

    @abstractmethod
    def visit_store(self, element: Store) -> None:
        pass


"""
Конкретные Посетители реализуют несколько версий одного и того же алгоритма,
которые могут работать со всеми классами конкретных компонентов.

Максимальную выгоду от паттерна Посетитель вы почувствуете, используя его со
сложной структурой объектов, такой как дерево Компоновщика. В этом случае было
бы полезно хранить некоторое промежуточное состояние алгоритма при выполнении
методов посетителя над различными объектами структуры.
"""


class Builder(Visitor):
    _for_print = "посещён СТРОИТЕЛЕМ"

    def visit_factory(self, element: Factory) -> None:
        print(f"{element.type_building()}: {self._for_print}, время поработать")

    def visit_home(self, element: Home) -> None:
        print(f"{element.type_building()}: {self._for_print}")

    def visit_store(self, element: Store) -> None:
        print(f"{element.type_building()}: {self._for_print}, а так же {element.buying('стройматериалов')}")


class Student(Visitor):
    _for_print = "посещён СТУДЕНТОМ"

    def visit_factory(self, element: Factory) -> None:
        print(f"{element.type_building()} {self._for_print} для практики")

    def visit_home(self, element: Home) -> None:
        print(f"{element.type_building()} {self._for_print}, время делать лабы")

    def visit_store(self, element: Store) -> None:
        print(f"{element.type_building()} {self._for_print}, а так же {element.buying('ручек и тетрадей')}")


def client_code(components_list: List[Building], visitor: Visitor) -> None:
    """
    Клиентский код может выполнять операции посетителя над любым набором
    элементов, не выясняя их конкретных классов. Операция принятия направляет
    вызов к соответствующей операции в объекте посетителя.
    """
    for component in components_list:
        component.accept(visitor)


if __name__ == "__main__":

    print("Студент решает прогулятся:")
    components = [Home(), Store(), Home()]
    student = Student()
    client_code(components, student)

    print("\nПосле получения профессии меняется маршрут:")
    components = [Home(), Factory(), Store(), Home()]
    builder = Builder()
    client_code(components, builder)
