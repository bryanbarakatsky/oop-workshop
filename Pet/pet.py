"""
    defines the pet class with getters and setters
"""

class Pet:
    """
        class that represents a pet
    """
    def __init__(self, name: str, age: int, species: str):
        self._name = name
        self._age = age
        self._species = species

    #name
    @property
    def name(self) -> str:
        """ returns the name of the pet """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """ sets the name of the pet """
        if len(name) < 1:
            raise ValueError("Name cannot be empty")
        self._name = name

    #age
    @property
    def age(self) -> int:
        """ returns the age of the pet """
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        """ sets the age of the pet """
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age

    #species
    @property
    def species(self) -> str:
        return self._species

    @species.setter
    def species(self, species: str) -> None:
        """ sets the species of the pet """
        self._species = species

    def make_sound(self) -> str:
        """ makes the pet sound """
        sounds = {"dog": "woof", "cat": "meow"}
        return sounds[self._species]
