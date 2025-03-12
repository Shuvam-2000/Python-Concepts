# multiple inheritance

class Animal:
    def eat(self):
        print("Eating")

class Bird:
    def fly(self):
        print("Flying")

class Eagle(Animal, Bird):
    def breed(self):
        print("Breeding")

Eagle = Eagle()
Eagle.breed()