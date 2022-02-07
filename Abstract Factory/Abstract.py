from __future__ import annotations
from abc import ABC, abstractmethod

class First(ABC):
    @abstractmethod
    def get_price(self):
        pass

class Second(ABC):
    @abstractmethod
    def get_price(self):
        pass

class Third(ABC):
    @abstractmethod
    def get_price(self):
        pass

# //////////////////
# ////// Food //////
# //////////////////

# Premium
class Carbonara(First):
    def get_price(self):
        print("Карбонара (П)\nЦена: 220 грн.\n----------------")

class Azu(Second):
    def get_price(self):
        print("Азу (П)\nЦена: 120 грн.\n----------------")

class Brownie(Third):
    def get_price(self):
        print("Брауни (П)\nЦена: 150 грн.\n----------------")

# ////////////////////////////////
# Standard
class VegetableSoup(First):
    def get_price(self):
        print("Овощной суп (O)\nЦена: 50 грн.\n----------------")

class SaladCaesar(Second):
    def get_price(self):
        print("Салат <<Цезарь>> (O)\nЦена: 70 грн.\n----------------")

class CakeVocational(Third):
    def get_price(self):
        print("Тортик (O)\nЦена: 45 грн.\n----------------")

# ////////////////////////////////
# Cheap
class HomemadePizza(First):
    def get_price(self):
        print("Пицца <<Домашняя>> (Д)\nЦена: 12 грн.\n----------------")

class Tomatojuice(Second):
    def get_price(self):
        print("Сок томатный (Д)\nЦена: 8 грн.\n----------------")

class Cake(Third):
    def get_price(self):
        print("Кекс (Д)\nЦена: 9 грн.\n----------------")


# Абстрактная фабрика
class Menu(ABC):
    @abstractmethod
    def get_first(self) -> First:
        pass

    @abstractmethod
    def get_second(self) -> Second:
        pass

    @abstractmethod
    def get_third(self) -> Third:
        pass

# Премиум еда
class Premium_Food(Menu):
    def get_first(self) -> Carbonara:
        return Carbonara()

    def get_second(self) -> Azu:
        return Azu()

    def get_third(self) -> Brownie:
        return Brownie()

# Стандартная еда
class Standard_Food(Menu):
    def get_first(self) -> VegetableSoup:
        return VegetableSoup()

    def get_second(self) -> SaladCaesar:
        return SaladCaesar()

    def get_third(self) -> CakeVocational:
        return CakeVocational()


# Стандартная еда
class Cheap_Food(Menu):
    def get_first(self) -> HomemadePizza:
        return HomemadePizza()

    def get_second(self) -> Tomatojuice:
        return Tomatojuice()

    def get_third(self) -> Cake:
        return Cake()

def saloon(store: Standard_Food):
    # Независимое от реализации
    store.get_first().get_price()
    store.get_second().get_price()
    store.get_third().get_price()

if __name__ == '__main__':
    print("\nПремиум еда:\n")
    saloon(Premium_Food())
    print("\n-----------------------------------\nОбычная еда:\n")
    saloon(Standard_Food())
    print("\n-----------------------------------\nДешёвая еда:\n")
    saloon(Cheap_Food())



