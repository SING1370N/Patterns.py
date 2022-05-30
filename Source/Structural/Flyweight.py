# Легковес
from random import choice, randint
from sys import getsizeof

cars = {}


class Car(object):
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine


class CarFactory:

    @staticmethod
    def get_car(model, engine):
        global cars
        return cars.setdefault((model, engine), Car(model, engine))


class ColorCars(object):
    def __init__(self, color):
        self.color = color

    def see(self, cars: Car):
        return
        # print("Машинка: {} на {} [{}] цвета {} [{}]".format(cars.model, cars.engine, id(cars), self.color,
        #                                                           id(self)))


class DisassemblyCars(object):
    def __init__(self):
        self.cars_numb = 0
        self.catalog = {}

    def get_catalog(self, color):
        return self.catalog.setdefault(color, ColorCars(color))

    def add_car(self, model, engine, color):
        self.get_catalog(color).see(CarFactory.get_car(model, engine))
        self.cars_numb += 1

    def auto_input(self, numb):
        title = ["BWM", "Chevrolet", "Mercedes", "Mitsubishi", "Audi", "Wolksvagen", "Msaercedes", "Mitsubasdishi",
                 "Audsddsi", "Wolkssssvagen"]
        color = ["pink", "black", "red", "white", "blue", "gray"]
        for i in range(numb):
            self.add_car(choice(title), randint(8, 32) / 10, choice(color))


class ProblemCAR:
    def __init__(self, num=5000):
        self.title = []
        self.eng = []
        self.color = []
        self.auto_input(num)

    def auto_input(self, numb):
        title = ["BWM", "Chevrolet", "Mercedes", "Mitsubishi", "Audi", "Wolksvagen", "Msaercedes", "Mitsubasdishi",
                 "Audsddsi", "Wolkssssvagen"]
        color = ["pink", "black", "red", "white", "blue", "gray"]
        for i in range(numb):
            self.title.append(choice(title))
            self.eng.append(randint(8, 32))
            self.color.append(choice(color))


if __name__ == '__main__':
    DisassemblyCars().auto_input(5000)
    list_ = list(cars.keys())
    list_.sort()
    print("Легковес:", str(int(getsizeof(cars)/1024)) + " KB")
    # print("---------------")
    A = ProblemCAR(5000)
    print("Просто:", str(int((getsizeof(A.title)+getsizeof(A.eng))/1024)) + " KB")
