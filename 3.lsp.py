"""
Liskov Substitution Principle

A sub-class must be substitutable for its super-class.  The aim of this
principle is to ascertain that a sub-class can assume the place of its
super-class without errors.  If the code finds itself checking the type of class
then, it must have violated this principle.

Let’s use our Animal example.
"""

def animal_leg_count(animals: list):
    for animal in animals:
        if isinstance(animal, Lion):
            print(lion_leg_count(animal))
        elif isinstance(animal, Mouse):
            print(mouse_leg_count(animal))
        elif isinstance(animal, Pigeon):
            print(pigeon_leg_count(animal))
        
animal_leg_count(animals)

"""
To make this function follow the LSP principle, we will follow this LSP
requirements postulated by Steve Fenton:

If the super-class (Animal) has a method that accepts a super-class type
(Animal) parameter.  Its sub-class(Pigeon) should accept as argument a
super-class type (Animal type) or sub-class type(Pigeon type).  If the
super-class returns a super-class type (Animal).  Its sub-class should return a
super-class type (Animal type) or sub-class type(Pigeon).  Now, we can
re-implement animal_leg_count function:
"""

def animal_leg_count(animals: list):
    for animal in animals:
        print(animal.leg_count())
        
animal_leg_count(animals)

"""
The animal_leg_count function cares less the type of Animal passed, it just
calls the leg_count method.  All it knows is that the parameter must be of an
Animal type, either the Animal class or its sub-class.

The Animal class now have to implement/define a leg_count method.  And its
sub-classes have to implement the leg_count method:
"""

class Animal:
    def leg_count(self):
        pass


class Lion(Animal):
    def leg_count(self):
        pass


"""
When it’s passed to the animal_leg_count function, it returns the number of legs
a lion has.

You see, the animal_leg_count doesn’t need to know the type of Animal to return
its leg count, it just calls the leg_count method of the Animal type because by
contract a sub-class of Animal class must implement the leg_count function.
"""
