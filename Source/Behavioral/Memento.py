from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import uniform, choice


class Memento(ABC):
    """
    Интерфейс Снимка предоставляет способ извлечения метаданных снимка, таких
    как дата создания или название. Однако он не раскрывает состояние Создателя.
    """

    @abstractmethod
    def get_state(self):
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, value_1: float, action: str, value_2: float, answer) -> None:
        self._action: str = action
        self._value_1: float = value_1
        self._value_2: float = value_2
        self._answer = answer
        self._date = str(datetime.now())[10:22]

    def get_state(self):
        """
        Создатель использует этот метод, когда восстанавливает своё состояние.
        """
        backup_arr = [self._value_1, self._value_2, self._action, self._answer]
        return backup_arr

    def get_name(self) -> str:
        """
        Остальные методы используются Опекуном для отображения метаданных.
        """

        return f"{self._date} : {self._value_1} {self._action} {self._value_2} = {to_fixed(self._answer)}"

    def get_date(self) -> str:
        return self._date


class Calculator:
    """
    Создатель содержит некоторое важное состояние, которое может со временем
    меняться. Он также объявляет метод сохранения состояния внутри снимка и
    метод восстановления состояния из него.
    """
    _action: str = None
    _value_1: float = None
    _value_2: float = None
    _answer = None
    _backups = None
    _backups_bool = False

    def __init__(self, value_1: float = 1, value_2: float = 1, action: str = "+"):
        self._backups = Backup(self)
        self.logic(value_1, value_2, action)

    def get_info(self, info: bool = False):
        if info:
            f"Калькулятор: {self._value_1} {self._action} {self._value_2} = {to_fixed(self._answer)}"
        else:
            print(f"Калькулятор: {self._value_1} {self._action} {self._value_2} = {to_fixed(self._answer)}")

    def logic(self, value_1: float, value_2: float, action: str):
        if self._backups_bool:
            self._backups.backup()
        else:
            self._backups_bool = True
        self._action = action
        self._value_1 = value_1
        self._value_2 = value_2
        if self._value_1 == 0:
            self._answer = self._value_2
        elif self._value_2 == 0:
            self._answer = self._value_1
        else:
            exec(f"try:\n"
                 f"  self._answer = ({self._value_1} {self._action} {self._value_2})\n"
                 f"except Exception:\n"
                 f"  self._answer = 'N/A'")
            #
            # if action == "+":
            #     self._answer = (self._value_1 + self._value_2)
            # elif action == "-":
            #     self._answer = (self._value_1 - self._value_2)
            # elif action == "*":
            #     self._answer = (self._value_1 * self._value_2)
            # elif action == "/":
            #     self._answer = (self._value_1 / self._value_2)
            # else:
            #     self._answer = "N/A"
        self.get_info()

    def undo(self):
        self._backups.undo()

    def history(self):
        self._backups.show_history()
        print(f"---> {self} <---")

    def __str__(self):
        return f"{self._value_1} {self._action} {self._value_2} = {self._answer}"

    def __int__(self):
        try:
            return int(self._answer)
        except Exception:
            return 0

    def __float__(self):
        try:
            return float(self._answer)
        except Exception:
            return 0

    def calculator(self):
        print(" -- Действие --")
        self.logic(float(input("Num 1: ")), float(input("Num 2: ")), input("Action: "))

    def input(self, value_1, value_2, action):
        self.logic(float(value_1), float(value_2), action)

    def save(self) -> Memento:
        """
        Сохраняет текущее состояние внутри снимка.
        """
        return ConcreteMemento(self._value_1, self._action, self._value_2, self._answer)

    def restore(self, memento: Memento) -> None:
        """
        Восстанавливает состояние Создателя из объекта снимка.
        """
        backup = memento.get_state()

        self._value_1 = backup[0]
        self._value_2 = backup[1]
        self._action = backup[2]
        self._answer = backup[3]

        self.get_info()


class Backup:
    """
    Опекун не зависит от класса Конкретного Снимка. Таким образом, он не имеет
    доступа к состоянию создателя, хранящемуся внутри снимка. Он работает со
    всеми снимками через базовый интерфейс Снимка.
    """

    def __init__(self, originator: Calculator) -> None:
        self._mementos = []
        self._originator = originator

    def bool_memento(self) -> bool:
        if not len(self._mementos):
            return False
        else:
            return True

    def backup(self) -> None:
        print(" --- Смотритель: сохранение состояния... ---")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            print("Backup: пусто!")
            return
        memento = self._mementos.pop()
        print(f" --- Смотритель: восстановление: {memento.get_name()} --- ")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("\nСмотритель: all backups:")
        numb = 1
        for memento in self._mementos:
            print(f" {numb}:", memento.get_name())
            numb += 1
        if numb == 1:
            print("     Список пуст!")

    @property
    def mementos(self):
        return self._mementos


def to_fixed(numObj, digits=2):
    return f"{numObj:.{digits}f}"


def random(cs: Calculator, num=10):
    for _ in range(num):
        print(f"\n            Действие {_ + 2}:")
        cs.input(float(str(uniform(0, 20))[:5]), float(str(uniform(0, 20))[:5]), choice(["+", "-", "*", "/", "**"]))


if __name__ == "__main__":
    print("            Действие 1:")
    calculator_system = Calculator()
    random(calculator_system)
    calculator_system.history()
    for _ in range(15):
        print()
        calculator_system.undo()
    calculator_system.history()
