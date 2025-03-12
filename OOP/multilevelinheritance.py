# multilevel inheritance

class Animal:
    def eat(self):
        print("Eating")

class Bird(Animal):
    def fly(self):
        super().eat()
        print("Flying")

class Eagle(Bird):
    def breed(self):
        super().fly()
        print("Breeding")

Eagle = Eagle()
Eagle.breed()