class Windows:
    def read_file(self) -> str:
        return "Windows может читать и понимать свои файлы"


class Linux:
    @staticmethod
    def read_ext4() -> str:
        return 'yp.weN_tcartsbA\nyp.tcartsbA\noiward.2\nlmx.1'


class Driver(Windows, Linux):
    def read_file(self) -> str:
        return f"Драйвер: \n{self.read_ext4()[::-1]}"


def view_files(OS: "Windows"):
    print(OS.read_file())


if __name__ == "__main__":
    windows = Windows()
    view_files(windows)

    adaptee = Linux()
    print("\nПроводник: Файлы ext4 не могут быть прочитаны Windows")
    print(adaptee.read_ext4())

    print("\nЧтение после установки драйвера:")
    adapter = Driver()
    view_files(adapter)
