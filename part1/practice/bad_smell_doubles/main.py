# Как то вечером три разработчика написали 
# три метода класса `SomeClass`, каждый под себя. 
# Методы по сути своей почти одинаковые.
#
# Напишите свой метод `sorted_func`, 
# учитывая особенности всех представленных методов


class SomeClass:
    def __init__(self):
        self.list = [3, 2, 1, 4, 2, 1]

    def sorted_func(self):
        self.list = sorted(self.list, reverse=False)
        return self.list


if __name__ == "__main__":
    some_sorted = SomeClass()
    print(some_sorted.sorted_func())

