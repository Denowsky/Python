from task3 import Person

class Worker(Person):
    def __init__(self, id_number: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id_number = id_number
        self.lvl = sum(list(map(int, id_number))) % 7

work_1 = Worker("1254878", "Samuel", "Jackson", "28")
print(work_1.show_name())
print(work_1.lvl)