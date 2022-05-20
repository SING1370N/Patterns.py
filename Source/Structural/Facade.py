from __future__ import annotations
from time import sleep
from random import randint
from progress.bar import ShadyBar


# Доп. функционал
def progressbar(title, times=5):
    bar = ShadyBar("{:^9}".format(title), max=100)
    for item in range(100):
        bar.next()
        sleep(times / randint(100, 1000))
    bar.finish()


class BIOS:
    def __init__(self, cpu, ram, drive, video_card):
        print("{:^53}".format("BIOS: Ready!"))
        self._cpu = cpu
        self._ram = ram
        self._drive = drive
        self._video_card = video_card

    def testing_device(self):
        if self._cpu.testing() and self._ram.testing() and self._drive.testing() and self._video_card.testing():
            return True
        else:
            return False


class CPU:
    def __init__(self, cpu_core=4):
        print("\n" + "{:^53}".format("Процессор: включён"))
        self._cpu_core = cpu_core

    def read_bios(self, bios):
        bios.testing_device()

    def testing(self):
        progressbar("CPU")
        return True


class RAM:
    def __init__(self, size):
        self._size = size

    def load(self):
        print("{:^53}".format("RAM: " + str(self._size)))
        pass

    def testing(self):
        progressbar("RAM")
        return True


class GPU:
    def __init__(self, gpu_name):
        print("{:^53}".format("Видеокарта: включена"))
        self._gpu_name = str(gpu_name)

    def testing(self):
        progressbar("GPU")
        return True


class HardDrive:
    def __init__(self, size):
        self._size = size

    def read(self):
        print("{:^53}".format("Windows: Hello World")+"\n\n")
        pass

    def testing(self):
        progressbar("Drive")
        return True


# Button Power (PC) Facade
class POWER:
    def __init__(self):
        self._cpu = CPU()
        self._ram = RAM(2048)
        self._ram.load()
        self._gpu = GPU("1030")
        self._drive = HardDrive(100000)
        self._bios = BIOS(self._cpu, self._ram, self._drive, self._gpu)
        print("\n"+"{:^53}".format("Проверка системы"))
        self._cpu.read_bios(self._bios)
        print("\n" + "{:^53}".format("-> Запуск <-") + "\n")
        self._drive.read()


if __name__ == "__main__":
    # В клиентском коде могут быть уже созданы некоторые объекты подсистемы. В
    # этом случае может оказаться целесообразным инициализировать Фасад с этими
    # объектами вместо того, чтобы позволить Фасаду создавать новые экземпляры.
    POWER()

