class Menu:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not Menu._instance:
            Menu._instance = super(Menu, cls).__new__(cls, *args, **kwargs)
        return Menu._instance

    def __init__(self):
        self._servers = []

    def addObject(self, NameObj):
        self._servers.append(NameObj)

    def addPackObject(self, Num=4):
        for i in range(1, Num):
            self._servers.append("Блюдо " + str(i))

    def Magic(self, Name="Чай"):
        self._servers.pop()
        self._servers.append(Name)


def see(OBJ):
    for i in range(len(OBJ._servers)):
        print(" ", OBJ._servers[i])


T1 = Menu()
T2 = Menu()
T3 = Menu()

T1.addPackObject(6)

print("Проверка переменной 1:")
see(T1)

T2.Magic()

print("\nПроверка переменной 2:")
see(T2)

print("\n", T1, "\n", T2, "\n", T3, sep='')
print("Однин и тот же:", T1 == T2 == T3)