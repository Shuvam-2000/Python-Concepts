# Self Parameter - identify the particular function on which it is passed

class Tata:
    def service(self):
        print("Servicing done")


class Mahindra:
    def service(self):
        print("Car Servicing done")

    def allService(self, other):
        self.service()
        other.service()


Harrier = Tata()
Scorpio = Mahindra()

Scorpio.allService(Harrier)
