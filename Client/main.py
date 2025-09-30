"""
main client script to demonstrate Pet and Item classes.
"""

from oopWorkshop.Pet.pet import Pet

def main():
    dog = Pet("Chop", 38, "dog")
    dog.age = 49
    print(dog.age)
    print(dog.make_sound())

if __name__ == "__main__":
    main()