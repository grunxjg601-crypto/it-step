
class Animal:
    def __init__(self, name="Unknown", age=0, color="black"):
        self.name = name
        self.age = age
        self.color = color

    def sound(self):
        return "Звук тварини"

class Dog(Animal):
    def __init__(self, name="Unknown", age=0, color="black", breed="Unknown"):
        super().__init__(name, age, color)
        self.breed = breed

    def sound(self):
        return "Гав-гав!"

class Cat(Animal):
    def __init__(self, name="Unknown", age=0, color="black", breed="Unknown"):
        super().__init__(name, age, color)
        self.breed = breed

    def sound(self):
        return "Няв-няв!"

dog = Dog("Бобік", 3, "коричневий", "Вівчарка")
cat = Cat("Мурчик", 2, "білий", "Британський")

print("Собака:")
print("Ім'я:", dog.name)
print("Вік:", dog.age)
print("Колір:", dog.color)
print("Порода:", dog.breed)
print("Звук:", dog.sound())

print("\nКіт:")
print("Ім'я:", cat.name)
print("Вік:", cat.age)
print("Колір:", cat.color)
print("Порода:", cat.breed)
print("Звук:", cat.sound())
