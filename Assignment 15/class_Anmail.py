class Animal:
    def __init__(self, species):
        self.species = species
    
    def speak(self):
        pass


class Mammal(Animal):
    def __init__(self, species, has_fur=True):
        super().__init__(species)
        self.has_fur = has_fur
    
    def give_birth(self):
        print(f"{self.species} is giving birth to live young.")


class Dog(Mammal):
    def __init__(self, breed, has_fur=True):
        super().__init__("Dog", has_fur)
        self.breed = breed
    
    def speak(self):
        return "Woof!"
    
    def wag_tail(self):
        print("Tail wagging!")
        

print("Creating instances")
animal = Animal("Unknown")
mammal = Mammal("Elephant")
dog = Dog("Labrador")

print("Using methods")
print(f"Animal species: {animal.species}")
print(f"Mammal species: {mammal.species}, Has fur: {mammal.has_fur}")
print(f"Dog species: {dog.species}, Breed: {dog.breed}, Has fur: {dog.has_fur}")

mammal.give_birth()
print(f"Dog says: {dog.speak()}")
dog.wag_tail()
