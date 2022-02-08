import copy


class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class SomeComponent:
    """
    Python предоставляет свой собственный интерфейс прототипа через `copy.copy` и
     `copy.deepcopy` И любой класс, который хочет реализовать пользовательские
     Реализации должны переопределить "__Copy__" и "__deepcopy__" Функции.
    """

    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    def __copy__(self):
        """
        Создайте неглубокую копию. Этот метод будет вызван всякий раз, когда кто-то вызывает
         `copy.copy` с этим объектом и возвращаемое значение возвращается как
         Новая неглубокая копия.
        """

        # First, let's create copies of the nested objects.
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)

        # Then, let's clone the object itself, using the prepared clones of the
        # nested objects.
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memo=None):
        """
        Создайте глубокую копию. Этот метод будет вызван всякий раз, когда кто-то звонит
         `copy.deepcopy` с этим объектом и возвращенным значением возвращается как
         Новая глубокая копия.

         Что такое использование аргумента `Memo` Memo - это словарь, который
         используется библиотекой «Deepcopy», чтобы предотвратить бесконечные рекурсивные копии в
         экземпляры круговых ссылок. Передайте его на все «глубокие звонки»
         Вы делаете в реализации «__deepcopy__», чтобы предотвратить бесконечное
         рекурсии.
        """
        if memo is None:
            memo = {}

        # First, let's create copies of the nested objects.
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)

        # Then, let's clone the object itself, using the prepared clones of the
        # nested objects.
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new


if __name__ == "__main__":

    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    component = SomeComponent(23, list_of_objects, circular_ref)
    circular_ref.set_parent(component)

    shallow_copied_component = copy.copy(component)

    # Let's change the list in shallow_copied_component and see if it changes in
    # component.
    shallow_copied_component.some_list_of_objects.append("другой объект")
    if component.some_list_of_objects[-1] == "другой объект":
        print(
            "Добавление элементов на `shallow_copied_component`'s "
            "some_list_of_objects добовляет его на `component`'s "
            "some_list_of_objects."
        )
    else:
        print(
            "Добавление элементов на `shallow_copied_component`'s "
            "some_list_of_objects НЕ добавляет его к `component`'s "
            "some_list_of_objects."
        )

    # Let's change the set in the list of objects.
    component.some_list_of_objects[1].add(4)
    if 4 in shallow_copied_component.some_list_of_objects[1]:
        print(
            "Изменение объектов в `component`'s some_list_of_objects "
            "изменяет этот объект в`shallow_copied_component`'s "
            "some_list_of_objects."
        )
    else:
        print(
            "Изменение объектов в `component`'s some_list_of_objects "
            "НЕ изменяет этот объект в`shallow_copied_component`'s "
            "some_list_of_objects."
        )

    deep_copied_component = copy.deepcopy(component)

    # Let's change the list in deep_copied_component and see if it changes in
    # component.
    deep_copied_component.some_list_of_objects.append("еще один объект")
    if component.some_list_of_objects[-1] == "еще один объект":
        print(
            "Добавляет элемент в `deep_copied_component`'s "
            "some_list_of_objects добовляет в `component`'s "
            "some_list_of_objects."
        )
    else:
        print(
            "Добавляет элемент в `deep_copied_component`'s "
            "some_list_of_objects НЕ добовляет в `component`'s "
            "some_list_of_objects."
        )

    # Let's change the set in the list of objects.
    component.some_list_of_objects[1].add(10)
    if 10 in deep_copied_component.some_list_of_objects[1]:
        print(
            "Изменение объектов в `component`'s some_list_of_objects "
            "изменяет этот объект в `deep_copied_component`'s "
            "some_list_of_objects."
        )
    else:
        print(
            "Изменение объектов в `component`'s some_list_of_objects "
            "НЕ изменяет этот объект в `deep_copied_component`'s "
            "some_list_of_objects."
        )

    print(
        f"id(deep_copied_component.some_circular_ref.parent): "
        f"{id(deep_copied_component.some_circular_ref.parent)}"
    )
    print(
        f"id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent): "
        f"{id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent)}"
    )
    print(
        "^^ Это показывает, что глубокие объекты содержат одинаковую ссылку, они "
        "несколько раз не клонированы. "
    )