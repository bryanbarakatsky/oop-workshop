"""
    defines the item class with getters and setters
"""

class Item:
    """
          class that represents an item
    """
    def __init__(self, name: str, value: int):
        self.__name = name
        self.__value = value

    #name
    def get_name(self) -> str:
        """ gets the name of the item """
        return self.__name

    def set_name(self, name: str) -> None:
        """ sets the name of the item """
        if len(name) < 1:
            raise ValueError("Name cannot be empty")
        self.__name = name

    #value
    def get_value(self) -> int:
        """ get the value of the item """
        return self.__value

    def set_value(self, value) -> None:
        """ sets the value of the item """
        if value < 0:
            raise ValueError("Value cannot be less than 0")
        self.__value = value

