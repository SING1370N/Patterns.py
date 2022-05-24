from abc import ABC, abstractmethod


class Phone(ABC):
    """
    Интерфейс телефона объявляет общие операции.
    """

    @abstractmethod
    def call(self, number) -> None:
        pass

    @abstractmethod
    def open_files(self) -> None:
        pass


class Standard(Phone):
    """
    Реальный Субъект содержит некоторую базовую бизнес-логику. Как правило,
    Реальные Субъекты способны выполнять некоторую полезную работу, которая к
    тому же может быть очень медленной или точной – например, коррекция входных
    данных. Заместитель может решить эти задачи без каких-либо изменений в коде
    Реального Субъекта.
    """

    def call(self, number) -> None:
        print(" - Звоним на", number)

    def open_files(self) -> None:
        print("Файловая система(разблокирован): открыт доступ.")


class Pass(Phone):
    """
    Интерфейс заместителя в виде блокировки телефона идентичен интерфейсу реального разблокированого телефона.
    """

    def __init__(self, real_subject: Standard) -> None:
        self._real_subject = real_subject

    def call(self, number) -> None:
        numbers_express = (1, 2, 3, 4, 101, 102, 103, 104, 105, 106)
        if number in numbers_express:
            print(' - ! Срочный звонок на', number, "!")
        else:
            print(" - Звонок заблокирован - %s, разблокируйте телефон" % number)

    def open_files(self) -> None:
        """
        Наиболее распространёнными областями применения паттерна Заместитель
        являются ленивая загрузка, кэширование, контроль доступа, ведение
        журнала и т.д. Заместитель может выполнить одну из этих задач, а затем,
        в зависимости от результата, передать выполнение одноимённому методу в
        связанном объекте класса Реального Субъекта.
        """
        print("Файловая система(блок): доступ закрыт.")
        if self.check_access():
            self._real_subject.open_files()

    def check_access(self) -> bool:
        print("\n---> Разблокировка <---")
        return True


def using(subject: Phone) -> None:
    """
    Клиентский код
    Должен работать со всеми, как с реальными, так и заместителями через
    интерфейс Субъекта в нашем случае интерфейс телефона, чтобы поддерживать как реальные
    субъекты, так и заместителей.

    Для более просто можно реализовать заместителя из реального.
    """
    print("Звонки:")
    subject.call(454)
    subject.call(101)
    subject.call(999)
    subject.open_files()


if __name__ == "__main__":
    print("Без пароля:")
    standard_os = Standard()
    using(standard_os)

    print("")

    print("С паролем:")
    pass_os = Pass(standard_os)
    using(pass_os)
