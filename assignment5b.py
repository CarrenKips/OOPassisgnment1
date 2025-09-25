# Base class (not required, but good practice)
class Mover:
    def move(self):
        pass  # placeholder method


# Vehicle classes
class Car(Mover):
    def move(self):
        print("Driving 🚗")


class Plane(Mover):
    def move(self):
        print("Flying ✈️")


class Bike(Mover):
    def move(self):
        print("Cycling 🚴")


# Animal classes
class Dog(Mover):
    def move(self):
        print("Running 🐕")


class Fish(Mover):
    def move(self):
        print("Swimming 🐟")


# Demonstration of polymorphism
if __name__ == "__main__":
    movers = [Car(), Plane(), Bike(), Dog(), Fish()]

    for m in movers:
        m.move()   # same method name, different behavior
