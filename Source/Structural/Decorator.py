class Skeleton:
    """
    Базовый интерфейс Компонента определяет поведение, которое изменяется
    декораторами.
    """

    def operation(self) -> str:
        pass


# The body of a woman
class BodyW(Skeleton):
    """
    Конкретные Компоненты предоставляют реализации поведения по умолчанию. Может
    быть несколько вариаций этих классов.
    """

    def operation(self) -> str:
        return "(Девочка) Тело"


# The body of a guy
class BodyG(Skeleton):
    """
    Конкретные Компоненты предоставляют реализации поведения по умолчанию. Может
    быть несколько вариаций этих классов.
    """

    def operation(self) -> str:
        return "(Мальчик) Тело"


class Decorator(Skeleton):
    """
    Базовый класс Декоратора следует тому же интерфейсу, что и другие
    компоненты. Основная цель этого класса - определить интерфейс обёртки для
    всех конкретных декораторов. Реализация кода обёртки по умолчанию может
    включать в себя поле для хранения завёрнутого компонента и средства его
    инициализации.
    """

    _component: Skeleton = None

    def __init__(self, component: Skeleton) -> None:
        self._component = component

    @property
    def component(self) -> Skeleton:
        """
        Декоратор делегирует всю работу обёрнутому компоненту.
        """

        return self._component

    def operation(self) -> str:
        return self._component.operation()


# Голова
class Head(Decorator):
    """
    Конкретные Декораторы вызывают обёрнутый объект и изменяют его результат
    некоторым образом.
    """

    def operation(self) -> str:
        """
        Декораторы могут вызывать родительскую реализацию операции, вместо того,
        чтобы вызвать обёрнутый объект напрямую. Такой подход упрощает
        расширение классов декораторов.
        """
        return f"{self.component.operation()} + голова"


# Ноги
class Legs(Decorator):
    """
    Конкретные Декораторы вызывают обёрнутый объект и изменяют его результат
    некоторым образом.
    """

    def operation(self) -> str:
        """
        Декораторы могут вызывать родительскую реализацию операции, вместо того,
        чтобы вызвать обёрнутый объект напрямую. Такой подход упрощает
        расширение классов декораторов.
        """
        return f"{self.component.operation()} + ноги"


# Руки
class Arms(Decorator):
    """
    Декораторы могут выполнять своё поведение до или после вызова обёрнутого
    объекта.
    """

    def operation(self) -> str:
        return f"{self.component.operation()} + руки"


def client_code(component: Skeleton) -> None:
    """
    Клиентский код работает со всеми объектами, используя интерфейс Компонента.
    Таким образом, он остаётся независимым от конкретных классов компонентов, с
    которыми работает.
    """
    print(component.operation())


if __name__ == "__main__":
    # Простые компоненты
    Woman = BodyW()
    Guy = BodyG()
    print("Просто компонент:")
    client_code(Woman)
    client_code(Guy)

    # //////////////////////////////////////
    print()

    WomanH = Head(Woman)
    WomanHA = Arms(WomanH)

    GuyA = Arms(Guy)
    GuyAH = Head(GuyA)
    GuyAHL = Legs(GuyAH)

    print("Человек с декоратором: ")
    client_code(WomanHA)
    client_code(GuyAHL)
