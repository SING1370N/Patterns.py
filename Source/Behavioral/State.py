from __future__ import annotations
from abc import ABC, abstractmethod


class Smartphone:
    """
    Контекст определяет интерфейс, представляющий интерес для клиентов. Он также
    хранит ссылку на экземпляр подкласса Состояния, который отображает текущее
    состояние Контекста.
    """

    _state = None
    _charging: bool = False

    def __init__(self, state: State) -> None:
        print("Телефон: Создан")
        self._state = state
        self._state.context = self

    def transition_to(self, state: State):
        """
        Контекст позволяет изменять объект Состояния во время выполнения.
        """
        print(f"Телефон: меняем состояние на {type(state).__name__}")
        self._state = state
        self._state.context = self

    """
    Контекст делегирует часть своего поведения текущему объекту Состояния.
    """

    def charging(self):
        self._charging = self._state.charging(self._charging)

    def button_power(self):
        self._state.button_power()

    def button_power_long(self):
        self._state.button_power_long()


class State(ABC):
    """
    Базовый класс Состояния объявляет методы, которые должны реализовать все
    Конкретные Состояния, а также предоставляет обратную ссылку на объект
    Контекст, связанный с Состоянием. Эта обратная ссылка может использоваться
    Состояниями для передачи Контекста другому Состоянию.
    """

    _context = None

    @property
    def context(self) -> Smartphone:
        return self._context

    @context.setter
    def context(self, context_phone: Smartphone) -> None:
        self._context = context_phone

    @abstractmethod
    def charging(self, func_print) -> bool:
        pass

    @abstractmethod
    def button_power(self) -> None:
        pass

    @abstractmethod
    def button_power_long(self) -> None:
        pass


"""
Конкретные Состояния реализуют различные модели поведения, связанные с
состоянием Контекста.
"""


class PowerOn(State):
    def button_power_long(self) -> None:
        print("Выключение...")
        self.context.transition_to(PowerOff())

    def button_power(self) -> None:
        print("Вкючается экран")
        self.context.transition_to(ScreenOn())

    def charging(self, func_print):
        if func_print:
            print("Зарядку отключено")
            self.context.transition_to(ScreenOn())
            return False
        else:
            print("Зарядку включено")
            self.context.transition_to(ScreenOn())
            return True


class PowerOff(State):
    def button_power_long(self) -> None:
        print("Включение...")
        self.context.transition_to(PowerOn())

    def button_power(self) -> bool:
        return False

    def charging(self, func_print):
        if func_print:
            print("Зарядку отключено")
            return False
        else:
            print("Зарядку включено")
            return True


class ScreenOff(State):
    def button_power_long(self) -> None:
        print("Вкючается экран")
        self.context.transition_to(ScreenOn())

    def button_power(self) -> None:
        print("Вкючается экран")
        self.context.transition_to(ScreenOn())

    def charging(self, func_print):
        if func_print:
            print("Зарядку отключено")
            self.context.transition_to(ScreenOn())
            return False
        else:
            print("Зарядку включено")
            self.context.transition_to(ScreenOn())
            return True


class ScreenOn(State):
    def button_power_long(self) -> None:
        action = str(input("Появляется меню:\n 1. Выключить\n 2. Выключить экран\n 3. Без звука"))
        if action == "1":
            self.context.transition_to(PowerOff())
        elif action == "2":
            self.context.transition_to(ScreenOff())

    def button_power(self) -> None:
        print("Выкючается экран")
        self.context.transition_to(ScreenOff())

    def charging(self, func_print):
        if func_print:
            print("Зарядку отключено")
            return False
        else:
            print("Зарядку включено")
            return True


if __name__ == "__main__":
    phone = Smartphone(PowerOff())
    phone.button_power()
    phone.button_power_long()
    phone.charging()
    phone.charging()
    phone.button_power()
    phone.charging()
    phone.charging()
    while True:
        try:
            exec(str(input("> ")))
        except BaseException:
            break
