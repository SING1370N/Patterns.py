from __future__ import annotations
from abc import ABC, abstractmethod


class Shape:
    """
    Абстракция устанавливает интерфейс для «управляющей» части двух иерархий
    классов. Она содержит ссылку на объект из иерархии Реализации и делегирует
    ему всю настоящую работу.
    """

    def __init__(self, color: Color) -> None:
        self._color = color

    def __str__(self):
        return f"{self.info_color()}"

    def info_color(self) -> str:
        pass


# Расширяем АБСТРАКЦИЮ
class Circle(Shape):
    """
    Можно расширить Абстракцию без изменения классов Реализации.
    """

    def info_color(self) -> str:
        return f"Квадрат {self._color.painting()}"


class Square(Shape):
    """
    Можно расширить Абстракцию без изменения классов Реализации.
    """

    def info_color(self) -> str:
        return f"Квадрат {self._color.painting()}"


class Triangle(Shape):
    """
    Можно расширить Абстракцию без изменения классов Реализации.
    """

    def info_color(self) -> str:
        return f"Треугольник {self._color.painting()}"


class Color(ABC):
    """
    Implementation
    Реализация устанавливает интерфейс для всех классов реализации. Он не должен
    соответствовать интерфейсу Абстракции. На практике оба интерфейса могут быть
    совершенно разными. Как правило, интерфейс Реализации предоставляет только
    примитивные операции, в то время как Абстракция определяет операции более
    высокого уровня, основанные на этих примитивах.
    """

    @abstractmethod
    def painting(self) -> str:
        pass


"""
Каждая Конкретная Реализация соответствует определённой платформе и реализует
интерфейс Реализации с использованием API этой платформы.
"""


class Blue(Color):
    def painting(self) -> str:
        return "является синим"


class Green(Color):
    def painting(self) -> str:
        return "является зеленым"


class Red(Color):
    def painting(self) -> str:
        return "является красным"


if __name__ == "__main__":
    print(Square(Red()).info_color())
    print(Square(Blue()).info_color())

    print("///////////////////////////")
    Blue = Blue()
    Green = Green()
    Red = Red()

    print(Square(Red))
    print(Triangle(Blue))
    print(Circle(Green))
    print(Triangle(Green))
