from __future__ import annotations
from abc import ABC


class Mediator(ABC):
    # Интерфейс Посредника /// sender: отправитель, event: действие
    def notify(self, sender: object, event: str, command: str) -> None:
        pass


class LogicMediator(Mediator):
    def __init__(self, buttons: BaseComponent, forms: BaseComponent = None, tables: BaseComponent = None):
        self._button = buttons
        self._button.mediator = self
        self._form = forms
        self._form.mediator = self
        self._table = tables
        self._table.mediator = self

    # sender: отправитель, event: действие
    def notify(self, sender: object, space: str = "", command: str = "") -> None:
        space = space.lower()
        command = command.lower()
        if space == "window":
            print(" - Window:", end="")
            self.function_button(command)
            self.function_form(command)
        elif space == "error":
            print(" - Error:", end="")
            self.function_button(command)
            self.function_form(command)
        elif space == "info":
            print(" - Info:", end="")
            self.function_button(command)
            self.function_form(command)
            self.function_table(command)
        else:
            print(f" --- Неизвестное действие или место - м: {space},", f"д: {command} ---")

    def function_button(self, command: str) -> None:
        if command == "open":
            print(" -> Открываю", type(self._button).__name__)
        elif command == "close":
            print(" -> Закрываю", type(self._button).__name__)
        else:
            print(f" -> Неизвестное действие {command} в кнопках")

    def function_table(self, command: str) -> None:
        if command == "input":
            print(" -> Ввод", type(self._table).__name__)
        elif command == "output":
            print(" -> Вывод", type(self._table).__name__)
        elif command == "open":
            print(" -> Открыть", type(self._table).__name__)
        else:
            print(f" -> Неизвестное действие {command} в таблицах")

    def function_form(self, command: str) -> None:
        if command == "input":
            print(" -> Ввод", type(self._form).__name__)
        elif command == "output":
            print(" -> Вывод", type(self._form).__name__)
        elif command == "open":
            print(" -> Открыть", type(self._form).__name__)
        else:
            print(f" -> Неизвестное действие {command} в формах")


class BaseComponent:
    """
    Базовый Компонент обеспечивает базовую функциональность хранения экземпляра
    посредника внутри объектов компонентов.
    """

    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    # Дескриптор для изменения установки на mediator.
    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


"""
Конкретные Компоненты реализуют различную функциональность. Они не зависят от
других компонентов. Они также не зависят от каких-либо конкретных классов
посредников.
"""


class Button(BaseComponent):
    def open(self, space: str) -> None:
        print("Кнопка в", space)
        self.mediator.notify(self, space, "open")

    def close(self, space: str) -> None:
        print("Кнопка в", space)
        self.mediator.notify(self, space, "close")

    def bag_button(self, space: str = "") -> None:
        print("Кнопка в", space)
        self.mediator.notify(self, space, "no")


class Table(BaseComponent):
    def input(self, space: str) -> None:
        print("Таблица в", space)
        self.mediator.notify(self, space, "input")

    def output(self, space: str) -> None:
        print("Таблица в", space)
        self.mediator.notify(self, space, "output")


class Form(BaseComponent):
    def input(self, space: str) -> None:
        print("Форма в", space)
        self.mediator.notify(self, space, "input")

    def output(self, space: str) -> None:
        print("Форма в", space)
        self.mediator.notify(self, space, "output")


if __name__ == "__main__":
    button = Button()
    form = Form()
    table = Table()
    mediator = LogicMediator(button, form, table)

    button.open("window")
    button.bag_button("Menu")
    print()
    table.output("Menu")
    table.input("Error")
    print()
    form.output("Info")
    form.input("S")
    print()
    button.open("Info")
