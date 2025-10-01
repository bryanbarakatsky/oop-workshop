"""
    defines the dog class
"""
from Pet.pet import Pet

class Dog(Pet):

    """
        dog class inherits from Pet class and adds behaviour
    """

    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age, "Dog")
        self.breed = breed

    def make_sound(self) -> str:
        """ makes dog make a sound (overrides method from superclass) """
        return "Bark!!"

    def fetch(self, item: str) -> str:
        """ makes dog fetch item """
        return f"{self.name}, go fetch the {item}"