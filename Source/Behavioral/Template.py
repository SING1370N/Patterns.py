from abc import ABC, abstractmethod
from random import randint
from datetime import datetime


class AbstractClass(ABC):
    def __init__(self, name_file: str = "File.pdf"):
        self.name_file = name_file

    def template_method(self) -> None:
        """
        Скелет алгоритма
        """
        print("Загрузка файла:", self.get_name_file())
        if not self.read_file():
            return
        self.get_size_file()
        self.hook_get()
        self.get_time_edit()
        self.write_file()
        self.hook_set()

    # Эти операции уже имеют реализации.

    def get_name_file(self) -> str:
        return self.name_file

    def get_size_file(self) -> str:
        print(f"{randint(1, 6000)}MB")
        return f"{self.name_file} : {randint(1, 6000)}MB"

    def get_time_edit(self) -> str:
        print(f"{self.name_file} : {randint(1, 28)}-{randint(1, 12)}-{randint(2002, 2022)}")
        return f"{randint(1, 28), randint(1, 12), randint(2002, 2022)}"

    # А эти операции должны быть реализованы в подклассах.

    @abstractmethod
    def read_file(self) -> None:
        pass

    @abstractmethod
    def write_file(self) -> None:
        pass

    # Это «хуки». Подклассы могут переопределять их, но это не обязательно,
    # поскольку у хуков уже есть стандартная (но пустая) реализация. Хуки
    # предоставляют дополнительные точки расширения в некоторых критических
    # местах алгоритма.

    def hook_get(self) -> None:
        pass

    def hook_set(self) -> None:
        pass


class FilePDF(AbstractClass, ABC):
    _name = "PDF"
    _name_file = ".pdf"

    def read_file(self):
        if self.name_file.lower().find(self._name_file) >= 0:
            print(f"Читаю файл: {self.name_file}")
            return True
        else:
            print(f"Файл {self.name_file} никак не {self._name}")
            return False

    def write_file(self):
        if self.name_file.lower().find(self._name_file) >= 0:
            print(f"Пишу в файл: {self.name_file} : {str(datetime.now())[:10]}")
            return True
        else:
            print(f"Файл {self.name_file} никак не {self._name}")
            return False


class FileDoc(AbstractClass, ABC):
    _name = "Doc"
    _name_file = ".docx"

    def read_file(self):
        if self.name_file.lower().find(self._name_file) >= 0:
            print(f"Читаю файл: {self.name_file}")
            return True
        else:
            print(f"Файл {self.name_file} никак не {self._name}")
            return False

    def write_file(self):
        if self.name_file.lower().find(self._name_file) >= 0:
            print(f"Пишу в файл: {self.name_file} : {str(datetime.now())[:10]}")
            return True
        else:
            print(f"Файл {self.name_file} никак не {self._name}")
            return False

    def hook_get(self) -> None:
        print(f"Работа hook_get из функции для {self._name}")


class FileXML(AbstractClass, ABC):
    _name = "XML"
    _name_file = ".xml"

    def read_file(self):
        if self.name_file.lower().find(self._name_file) >= 0:
            print(f"Читаю файл: {self.name_file}")
            return True
        else:
            print(f"Файл {self.name_file} никак не {self._name}")
            return False

    def write_file(self):
        if self.name_file.lower().find(self._name_file) >= 0:
            print(f"Пишу в файл: {self.name_file} : {str(datetime.now())[:10]}")
            return True
        else:
            print(f"Файл {self.name_file} никак не {self._name}")
            return False

    def hook_set(self) -> None:
        print(f"Работа hook_set из функции для {self._name}")


def client_code(abstract_class: AbstractClass) -> None:
    abstract_class.template_method()


if __name__ == "__main__":
    pr = "--------------------------------"
    client_code(FilePDF("file.pdf"))
    print(pr)
    client_code(FileDoc("fileees.pdf"))
    print(pr)
    client_code(FileDoc("fyles.docx"))
    print(pr)
    client_code(FileXML("feles.cx"))
    print(pr)
    client_code(FileXML("foles.XML"))
