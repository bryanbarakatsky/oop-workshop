"""
main client script to demonstrate Pet and Item classes.
"""

from oopWorkshop.Pet.pet import Pet
from oopWorkshop.Pet.item import Item

def main():
    dog = Pet("Chop", 38, "dog")
    item = Item("Ball", 20)
    dog.age = 49
    print(dog.age)
    print(dog.make_sound())
    print(item.get_name(), item.get_value())

if __name__ == "__main__":
    main()

