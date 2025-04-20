class Menu:
    def __init__(self):
        self._parent = None
        self.options: dict[int, str] = {}

    # added for future sub-menus
    @property
    def parent(self) -> None:
        return self._parent

    @parent.setter
    def parent(self, other: "Menu") -> None:
        self._parent = other

    def add_option(self, id: int, option: str) -> None:
        if option not in self.options.values():
            self.options[id] = option

    def __str__(self) -> str:
        return "\n".join(f"{id} - {value}" for id, value in self.options.items())

    def select_option(self) -> str:
        while True:
            try:
                option = input("Please select an option using numbers: ")
                if option not in self.options:
                    print("Please select a valid option.")
                else:
                    return option
            except ValueError:
                print("Please use numbers only.")
