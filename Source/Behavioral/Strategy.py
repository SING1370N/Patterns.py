from __future__ import annotations
from abc import ABC, abstractmethod


class Strategy(ABC):
    # Интерфейс Стратегии
    @abstractmethod
    def convert(self, data):
        pass


class ConvertInt(Strategy):
    def convert(self, data) -> int:
        return int(data)


class ConvertFloat(Strategy):
    def convert(self, data) -> float:
        return float(data)


class ConvertStr(Strategy):
    def convert(self, data) -> str:
        return str(data)


class Converter:
    # Контекст определяет интерфейс, представляющий интерес для клиентов.
    def __init__(self, strategy: Strategy = None) -> None:
        """
        Обычно Контекст принимает стратегию через конструктор, а также
        предоставляет сеттер для её изменения во время выполнения.
        """
        if not strategy:
            self._strategy = None
        else:
            self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    # getter and setter
    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def input(self, data):
        if not self._strategy:
            print("Нету стратегии! Установите стратегию!")
        else:
            result = self._strategy.convert(data)
            print(f"Тип: {type(result)} из {type(data)}")
            print(f"Значение: {result}")


if __name__ == "__main__":
    converter = Converter()
    converter.input(15.00)
    converter.input(15.955)
    converter.input(15)
    converter.input("15")
    converter.strategy = ConvertInt()
    converter.input(15.00)
    converter.input(15.955)
    converter.input(15)
    converter.input("15")
    converter.strategy = ConvertFloat()
    converter.input(15)
    converter.input(15.955)
    converter.input(15)
    converter.input("15")
