"""
main client script to demonstrate Pet and Item classes.
"""

from oopWorkshop.Pet.pet import Pet
from oopWorkshop.Pet.item import Item
from oopWorkshop.Pet.dog import Dog

def main():
    dog = Pet("Chop", 38, "dog")
    item = Item("Ball", 20)
    dog.age = 49
    # print(dog.age)
    # print(dog.make_sound())
    # print(item.get_name(), item.get_value())

    my_dog = Dog(dog.name, dog.age, "Labrador")
    print(my_dog.age)
    print(my_dog.fetch("ball"))
    print(my_dog.make_sound())

if __name__ == "__main__":
    main()


