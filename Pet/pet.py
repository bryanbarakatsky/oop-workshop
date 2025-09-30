"""
    Defines the pet class with getters and setters
"""

class Pet:
    """
        A class that represents a pet
    """
    def __init__(self, name: str, age: int, species: str):
        self._name = name
        self._age = age
        self._species = species

    # Getters and Setters
    def get_name(self) -> str:
        """ Returns the name of the pet"""
        return self._name

    def set_name(self, name: str) -> None:
        """ Sets the name of the pet """
        if len(name) < 1:
            raise ValueError("Name cannot be empty")
        self._name = name

    def get_age(self) -> int:
        """ Returns the age of the pet"""
        return self._age

    def set_age(self, age: int) -> None:
        """ Sets the age of the pet """
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age

    def get_species(self) -> str:
        """ Returns the species of the pet"""
        return self._species

    def set_species(self, species: str) -> None:
        """ Sets the species of the pet """
        self._species = species

    def make_sound(self) -> str:
        """ Makes the pet sound"""
        sounds = {"dog" : "woof", "cat": "meow"}
        return sounds[self._species]
