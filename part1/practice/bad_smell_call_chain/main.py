# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Person:
    def __init__(self, room: int, population: int):
        self.__room = room
        self.__population = population

    def get_person_room(self):
        return self.__room

    def get_city_population(self):
        return self.__population


# сделать экземпляр класса person и вызвать новые методы.


some_person = Person(room=42, population=10500)
print(some_person.get_person_room())
print(some_person.get_city_population())
