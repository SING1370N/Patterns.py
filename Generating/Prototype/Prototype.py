import copy


class SelfReferencingEntity:
    def __init__(self):
        self.parent = None  # Родитель

    def set_parent(self, parents):
        self.parent = parents


class SomeComponent:
    """
    Python предоставляет свой собственный интерфейс прототипа через `copy.copy` и
     `copy.deepcopy` И любой класс, который хочет реализовать пользовательские
     Реализации должны переопределить "__Copy__" и "__deepcopy__" Функции.
    """

    def __init__(self, num_list, list_food, text, num, parents):
        self.num_list = num_list
        self.list_foods = list_food
        self.text = text
        self.num = num
        self.parent_ = parents


if __name__ == "__main__":

    MenuList = ["Пицца", "X", "Чай", "Стейк"]
    parent = SelfReferencingEntity()
    menu_list = SomeComponent(23, MenuList, "Text", 53, parent)
    parent.set_parent(menu_list)
    print("")
    copy_list = copy.copy(menu_list)
    print(copy_list.text==menu_list.text,"\n",copy_list.text, "- id:", id(copy_list.text), "  ", menu_list.text, "- id:", id(menu_list.text))
    copy_list.text = "New Text"
    print("")
    print(copy_list.text==menu_list.text,"\n",copy_list.text, "- id:", id(copy_list.text), "  ", menu_list.text, "- id:", id(menu_list.text))
    
    

    # Давайте изменим список на copy_list и посмотреть, изменяется ли он в компонент.
    copy_list.list_foods.append("copy")
    print("\n--- Copy ---\n", copy_list.list_foods)
    if menu_list.list_foods[-1] == "copy":
        print(
            "Добовляет элемент (COPY)\n"
        )
    else:
        print(
            "НЕ добовляет элемент (COPY)\n"
        )

    # Давайте изменим набор в списке объектов.
    menu_list.list_foods[1] = "AAA"
    print(copy_list.list_foods)
    if "AAA" in copy_list.list_foods[1]:
        print(
            "Изменяет объекты (COPY)\n"
        )
    else:
        print(
            "Изменяет объекты (COPY)\n"
        )

    deep_list = copy.deepcopy(menu_list)

    # Давайте изменим список в Deep_copied_Component и посмотрите, изменяется ли он в компонент.
    deep_list.list_foods.append("deep")
    print("\n--- DeepCopy ---\n", deep_list.list_foods, " vs ", menu_list.list_foods)
    if menu_list.list_foods[-1] == "deep":
        print(
            "Добавляет элемент (DEEP)\n"
        )
    else:
        print(
            "НЕ добавляет элемент (DEEP)\n"
        )

    # Давайте изменим набор в списке объектов.
    menu_list.list_foods[1] = "ZZZ"
    print(deep_list.list_foods, " vs ", menu_list.list_foods)
    if "ZZZ" in deep_list.list_foods[1]:
        print(
            "Изменяет этот объект (DEEP)\n"
        )
    else:
        print(
            "НЕ изменяет этот объект (DEEP)\n"
        )
