from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    """
    Интерфейс Команды объявляет метод для выполнения команд.
    """
    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    """
    Некоторые команды способны выполнять простые операции самостоятельно.
    """
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"Простоая команада (печать): ({self._payload})")


class ComplexCommand(Command):
    """
    Но есть и команды, которые делегируют более сложные операции другим
    объектам, называемым «получателями».
    """
    def __init__(self, receive: Receiver, *commands: str) -> None:
        """
        Сложные команды могут принимать один или несколько объектов-получателей
        вместе с любыми данными о контексте через конструктор.
        """
        self._receiver = receive
        self._commands = commands

    def execute(self) -> None:
        """
        Команды могут делегировать выполнение любым методам получателя.
        """
        print("Сложная команда: с помощью получателя объекта")
        self._receiver.do_something(self._commands[0])
        for command in self._commands[1:]:
            self._receiver.do_something_else(command)


class Receiver:
    """
    Классы Получателей содержат некую важную бизнес-логику. Они умеют выполнять
    все виды операций, связанных с выполнением запроса. Фактически, любой класс
    может выступать Получателем.
    """
    @staticmethod
    def do_something(a: str) -> None:
        print(f"PC: Работая над ({a}.)")

    @staticmethod
    def do_something_else(b: str) -> None:
        print(f"PC: также работает над ({b}.)")


class Invoker:
    """
    Отправитель связан с одной или несколькими командами. Он отправляет запрос
    команде.
    """
    _on_commands = None
    _on_start = None
    _on_finish = None

    """
    Инициализация команд.
    """
    def set_commands(self, commands: Command):
        self._on_commands = commands

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def action(self) -> None:
        """
        Отправитель не зависит от классов конкретных команд и получателей.
        Отправитель передаёт запрос получателю косвенно, выполняя команду.
        """
        print("Начало простого:")
        if isinstance(self._on_start, Command):
            self._on_start.execute()
        print(" --- выполнение ---\nКонец простого:")
        print("Начало сложного:")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()
        print(" --- выполнение ---\nКонец сложного:")


if __name__ == "__main__":
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Hello!"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(
        receiver, "Delete files", "Open dir", "del pass", "block pc"))
    invoker.action()
