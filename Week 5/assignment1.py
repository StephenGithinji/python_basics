# Assignment 1: Design Your Own Class!
# We will create a class for a Superhero and then a more specific
# class that inherits from it.

class Superhero:
    """
    A base class representing a generic superhero.
    
    Attributes:
        name (str): The superhero's public name.
        power (str): The superhero's primary power.
        strength_level (int): A rating of the hero's strength (1-100).
    """
    def __init__(self, name, power, strength_level):
        """Initializes a new Superhero object."""
        self.name = name
        self.power = power
        # Using a private attribute to demonstrate encapsulation
        self.__strength_level = strength_level

    def introduce(self):
        """Prints an introduction for the superhero."""
        print(f"Greetings! I am {self.name}.")

    def use_power(self):
        """Simulates the superhero using their power."""
        print(f"{self.name} uses their {self.power} power!")

    def get_strength(self):
        """Safely retrieves the private strength_level attribute."""
        return self.__strength_level

# Inheritance: Speedster inherits from Superhero
class Speedster(Superhero):
    """
    A specialized class for superheroes whose power is super-speed.
    This class inherits from the Superhero class.

    Attributes:
        top_speed (int): The top speed the hero can run, in mph.
    """
    def __init__(self, name, strength_level, top_speed):
        """Initializes a new Speedster object."""
        # Call the parent class (Superhero) constructor
        super().__init__(name, "Super Speed", strength_level)
        self.top_speed = top_speed

    # Overriding the parent's method to add more detail
    def use_power(self):
        """A more specific version of using the power for a Speedster."""
        print(f"{self.name} zips by at {self.top_speed} mph!")

# --- Creating and using objects ---

# Create an object of the base class
aqua_hero = Superhero("Aqua Guardian", "Water Control", 85)
aqua_hero.introduce()
aqua_hero.use_power()
print(f"Strength Level: {aqua_hero.get_strength()}")

print("-" * 20) # Separator

# Create an object of the inherited class
velocity_vortex = Speedster("Velocity Vortex", 70, 800)
velocity_vortex.introduce()
velocity_vortex.use_power() # This will call the overridden method
print(f"Strength Level: {velocity_vortex.get_strength()}")
