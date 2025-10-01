"""
main client script to demonstrate Pet and Item classes.
"""
from Pet.PetAgeError import PetAgeError
from Pet.pet import Pet
from Pet.item import Item
from Pet.dog import Dog

def main():
    dog = Pet("Chop", 10, "dog")
    item = Item("Ball", 20)

    try:
        dog.age = 55
    except PetAgeError as e:
        print(f"Error: {e}")
    else:
        print(f"Pet age {dog.age} is valid")
    finally:
        print("Age validation complete")


    # print(dog.age)
    # print(dog.make_sound())
    # print(item.get_name(), item.get_value())

    # my_dog = Dog(dog.name, dog.age, "Labrador")
    # print(my_dog.age)
    # print(my_dog.fetch("ball"))
    # print(my_dog.make_sound())

if __name__ == "__main__":
    main()


