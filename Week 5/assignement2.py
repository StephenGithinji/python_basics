# Activity 2: Polymorphism Challenge!
# This program demonstrates polymorphism using different vehicle types.
# Each vehicle has a 'move' method, but it behaves differently for each one.

class Vehicle:
    """A base class for all vehicles."""
    def __init__(self, name):
        self.name = name

    def move(self):
        """A generic move action. This will be overridden by child classes."""
        print(f"{self.name} is moving.")

class Car(Vehicle):
    """A class representing a car."""
    def move(self):
        """Overrides the parent move method for a car."""
        print(f"{self.name} is Driving 🚗")

class Plane(Vehicle):
    """A class representing a plane."""
    def move(self):
        """Overrides the parent move method for a plane."""
        print(f"{self.name} is Flying ✈️")

class Boat(Vehicle):
    """A class representing a boat."""
    def move(self):
        """Overrides the parent move method for a boat."""
        print(f"{self.name} is Sailing ⛵")

# --- Demonstrating Polymorphism ---

# Create instances of each vehicle class
my_car = Car("Sedan")
my_plane = Plane("Boeing 747")
my_boat = Boat("Sailboat")

# Create a list of different vehicle objects
vehicles = [my_car, my_plane, my_boat]

# Loop through the list and call the same 'move()' method on each object.
# Python automatically calls the correct method for each object type.
print("--- Demonstrating Polymorphic Behavior ---")
for vehicle in vehicles:
    vehicle.move()
