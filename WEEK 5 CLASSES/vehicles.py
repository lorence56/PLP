class Vehicle:
    def move(self):
        print("The vehicle moves...")

class Car(Vehicle):
    def move(self):
        print("🚗 The car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("✈️ The plane is flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("⛵ The boat is sailing on the water.")

# Demonstration of polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Each class defines move() differently
