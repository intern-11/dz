
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Животное издает звук")

    def eat(self):
        print(f"{self.name} ест")

class Bird(Animal):
    def __init__(self, name, age, can_fly=True):
        super().__init__(name, age)
        self.can_fly = can_fly

    def make_sound(self):
        print(f"{self.name} чирикает")


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} рычит")


class Reptile(Animal):
    def __init__(self, name, age, is_venomous=False):
        super().__init__(name, age)
        self.is_venomous = is_venomous

    def make_sound(self):
        print(f"{self.name} шипит")


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} добавлен в зоопарк")

    def add_staff(self, employee):
        self.staff.append(employee)
        print(f"{employee.name} принят на работу")

class Employee:
    def __init__(self, name):
        self.name = name
class ZooKeeper(Employee):
    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")
        animal.eat()
class Veterinarian(Employee):
    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")

zoo = Zoo("Городской зоопарк")

lion = Mammal("Лев", 4, "коричневый")
parrot = Bird("Попугай", 2)

keeper = ZooKeeper("Алексей")
vet = Veterinarian("Ирина")

zoo.add_animal(lion)
zoo.add_animal(parrot)

zoo.add_staff(keeper)
zoo.add_staff(vet)

keeper.feed_animal(lion)
vet.heal_animal(parrot)
