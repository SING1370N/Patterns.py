from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


class BaseIterator(Iterator):
    """
    У итератора может быть множество других полей для хранения состояния итерации,
    особенно когда он должен работать с определённым типом коллекции.
    """
    # Поля для хранения состояния итерации
    _position: int = None
    _reverse: bool = False

    # инициализация
    def __init__(self, Collection, reverse: bool = False) -> None:
        self._collection = Collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value


class Collection(Iterable):
    """
    Конкретные Коллекции предоставляют один или несколько методов для получения
    новых экземпляров итератора, совместимых с классом коллекции.
    """

    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> BaseIterator:
        return BaseIterator(self._collection)  # Метод __iter__() возвращает объект итератора

    def get_reverse_iterator(self) -> BaseIterator:
        return BaseIterator(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)

    def sort(self):
        self._collection.sort()

    def sort_reverse(self):
        self._collection.reverse()


if __name__ == "__main__":
    # Клиентский код может знать или не знать о Конкретном Итераторе или классах
    # Коллекций, в зависимости от уровня косвенности, который вы хотите
    # сохранить в своей программе.
    collection = Collection()
    collection.add_item(1)
    collection.add_item(2)
    collection.add_item(9)
    collection.add_item(5)
    collection.add_item(0)
    collection.sort()

    print("Прямо:")
    print(" ".join(map(str, collection)))
    print("\nРеверс:")
    print(" ".join(map(str, collection.get_reverse_iterator())))

