from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional
#   Желательный тип - Optional
#   Любой тип - Any
from sys import setrecursionlimit   # ЛИМИТ РЕКУРСИИ


class Handler(ABC):
    """
    Интерфейс Обработчика (Handler) объявляет метод построения цепочки обработчиков. Он
    также объявляет метод для выполнения запроса.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class BasicHandler(Handler):
    """
    Поведение цепочки по умолчанию может быть реализовано внутри базового класса
    обработчика.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Возврат обработчика отсюда позволит связать обработчики простым
        # способом, вот так:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str | None:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


"""
Все Конкретные Обработчики либо обрабатывают запрос, либо передают его
следующему обработчику в цепочке.
"""


class MonkeyHandler(BasicHandler):
    def handle(self, request: Any) -> str:
        if request == "банан":
            return f"Манки любит {str(request).lower()}"
        else:
            return super().handle(request)


class SquirrelHandler(BasicHandler):
    def handle(self, request: Any) -> str:
        if request == "орешек":
            return f"Белка любит {request}"
        else:
            return super().handle(request)


class DogHandler(BasicHandler):
    def handle(self, request: Any) -> str:
        if request == "косточку":
            return f"Собачка любит {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    Обычно клиентский код приспособлен для работы с единственным обработчиком. В
    большинстве случаев клиенту даже неизвестно, что этот обработчик является
    частью цепочки.
    """

    for food in ["орешек", "Банан", "Кофе"]:
        food = str(food).lower()
        print(f"\nКто любит {food}?")
        result = handler.handle(food)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {food} никто не захотел", end="")


if __name__ == "__main__":
    # Обработчики (создаем зверюшек)
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    # Строим цепь
    monkey.set_next(squirrel).set_next(dog)

    # Клиент должен иметь возможность отправлять запрос любому обработчику, а не
    # только первому в цепочке.
    print("\nМанки > Белка > Собачка", end=" ")
    client_code(monkey)

    print("\n\nБелка > Собачка", end=" ")
    client_code(squirrel)

    print("\n\nЗамыкаем цепь (PEP 651 - 1М): ", end=" ")
    if input() == "+":
        setrecursionlimit(6)
        dog.set_next(monkey)
        client_code(monkey)
