from __future__ import annotations
from abc import ABC, abstractmethod
from random import choice
from typing import List


class Subscription(ABC):
    """
    Интферфейс издателя объявляет набор методов для управлениями подписчиками.
    """
    _video: str = None

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Присоединяет наблюдателя к издателю.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Отсоединяет наблюдателя от издателя.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Уведомляет всех наблюдателей о событии.
        """
        pass

    @property
    def video(self):
        return self._video


class YouTube(Subscription):

    _observers: List[Observer] = []
    """
    Список подписчиков. В реальной жизни список подписчиков может храниться в
    более подробном виде (классифицируется по типу события и т.д.)
    """

    def __init__(self):
        print("Великий ютуб создан")

    def attach(self, observer: Observer) -> None:
        print(" - Подписка", observer)
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        print(" - Отписка", observer)
        self._observers.remove(observer)

    """
    Методы управления подпиской.
    """

    def notify(self) -> None:
        """
        Запуск обновления в каждом подписчике.
        """
        print("Уведомление:")
        numb_good_upd = 0
        for observer in self._observers:
            if observer.update(self):
                numb_good_upd += 1
        if numb_good_upd == 0:
            print(f"!!! Никто не подписан на это уведомление ({self._video})")

    def logic(self) -> None:
        """
        Обычно логика подписки – только часть того, что делает Издатель.
        Издатели часто содержат некоторую важную бизнес-логику, которая
        запускает метод уведомления всякий раз, когда должно произойти что-то
        важное (или после этого).
        """
        ytb_list = ["мультики", "дача", "фильмы", "песни"]
        self._video = choice(ytb_list)
        print(f"\n ----- Выход нового видео: {self._video} -----\n")
        self.notify()


class Observer(ABC):
    """
    Интерфейс Наблюдателя объявляет метод уведомления, который издатели
    используют для оповещения своих подписчиков.
    """
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def update(self, subject: Subscription) -> bool:
        """
        Получить обновление от субъекта.
        """
        pass


"""
Конкретные Наблюдатели реагируют на обновления, выпущенные Издателем, к которому
они прикреплены.
"""


class Grandmother(Observer):
    def __str__(self):
        return "БАБУШКИ"

    def update(self, sub: Subscription) -> bool:
        ytb_list = ["дача", "фильмы", "песни"]
        if sub.video in ytb_list:
            print("Бабушке нравится новый выпуск про", sub.video)
            return True
        return False


class Grandson(Observer):
    def __str__(self):
        return "ВНУКА"

    def update(self, sub: Subscription) -> bool:
        ytb_list = ["мультики", "песни"]
        if sub.video in ytb_list:
            print("Внуку нравится новый выпуск про", sub.video)
            return True
        return False


if __name__ == "__main__":
    # Клиентский код.

    youtube = YouTube()

    grandm = Grandmother()
    youtube.attach(grandm)

    grans = Grandson()
    youtube.attach(grans)

    youtube.logic()
    youtube.logic()

    youtube.detach(grandm)

    youtube.logic()
    youtube.logic()
    youtube.logic()
    youtube.logic()
    youtube.logic()
    youtube.logic()
    youtube.logic()

