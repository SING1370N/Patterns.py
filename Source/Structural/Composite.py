from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    """
    Базовый класс объявляет общие операции
    """

    def __init__(self):
        self._parent = None

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    @staticmethod
    def check() -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass


class Pizza(Component):
    """
    Класс еды - пиццы
    """

    def operation(self) -> str:
        return "Pizza"


class Trash(Component):
    """
    Класс мусор
    """

    def operation(self) -> str:
        return "trash"


class Box(Component):

    def __init__(self) -> None:
        super().__init__()
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def check(self) -> bool:
        return True

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        if not results:
            return f"BOX(Empty)"
        return f"BOX({' + '.join(results)})"


def check_obj(component: Component) -> None:
    print(component.operation(), end="")


def check_all(component1: Component, component2: Component) -> None:
    if component1.check():
        component1.add(component2)
    print(component1.operation(), end="")


if __name__ == "__main__":
    food = Pizza()
    print("Что мы видим?")
    check_obj(food)
    print("\n")
    box = Box()

    box1 = Box()
    box1.add(Pizza())
    box1.add(Box())

    box2 = Box()
    box2.add(Trash())

    box.add(box1)
    box.add(box2)

    print("А что в этой коробке?")
    check_obj(box)
    print("\n")

    print("Client: Мне не нужно проверять классы компонентов, даже при управлении деревом:")
    check_all(box, food)
