# Base class
class Avenger:
    def __init__(self, name, power, weapon):
        self.name = name                # public attribute
        self._power = power             # protected attribute (encapsulation hint)
        self.__weapon = weapon          # private attribute (encapsulation)
    
    # Method to display Avenger's details
    def introduce(self):
        return f"I am {self.name}, and my power is {self._power}!"
    
    # Getter for private attribute
    def get_weapon(self):
        return self.__weapon
    
    # Setter for private attribute
    def set_weapon(self, new_weapon):
        self.__weapon = new_weapon
    
    # Method to demonstrate polymorphism
    def attack(self):
        return f"{self.name} attacks with {self.__weapon}!"
    

# Derived class (Inheritance)
class IronMan(Avenger):
    def __init__(self, name, power, weapon, suit_version):
        super().__init__(name, power, weapon)  # call parent constructor
        self.suit_version = suit_version
    
    # Overriding attack method (Polymorphism)
    def attack(self):
        return f"{self.name} uses his {self.suit_version} suit to fire repulsor blasts!"


class Thor(Avenger):
    def __init__(self, name, power, weapon, realm="Asgard"):
        super().__init__(name, power, weapon)
        self.realm = realm
    
    # Overriding attack method
    def attack(self):
        return f"{self.name} summons lightning with {self.get_weapon()}!"


# Example usage
if __name__ == "__main__":
    avenger1 = Avenger("Hawkeye", "Expert Marksman", "Bow and Arrows")
    ironman = IronMan("Tony Stark", "Genius-level intellect", "Repulsors", "Mark LXXXV")
    thor = Thor("Thor", "God of Thunder", "Mjolnir")

    # Introductions
    print(avenger1.introduce())
    print(ironman.introduce())
    print(thor.introduce())

    # Attacks (polymorphism in action)
    print(avenger1.attack())
    print(ironman.attack())
    print(thor.attack())

    # Encapsulation demo
    print(f"Thor's weapon: {thor.get_weapon()}")
    thor.set_weapon("Stormbreaker")
    print(f"Thor's new weapon: {thor.get_weapon()}")
