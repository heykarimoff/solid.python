"""
Single Responsibility Principle

“…You had one job” — Loki to Skurge in Thor:
Ragnarok

A class should have only one job.  If a class has more than one responsibility,
it becomes coupled.  A change to one responsibility results to modification of
the other responsibility.
"""

class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    def save(self, animal: Animal):
        pass

"""
The Animal class violates the SRP.

How does it violate SRP?

SRP states that classes should have one responsibility, here, we can draw out
two responsibilities: animal database management and animal properties
management.  The constructor and get_name manage the Animal properties while the
save manages the Animal storage on a database.

How will this design cause issues in the future?

If the application changes in a way that it affects database management
functions. The classes that make use of Animal properties will have to be
touched and recompiled to compensate for the new changes.

You see this system smells of rigidity, it’s like a domino effect, touch one
card it affects all other cards in line.

To make this conform to SRP, we create another class that will handle the sole
responsibility of storing an animal to a database:
"""

class Animal:
    def __init__(self, name: str):
            self.name = name
    
    def get_name(self):
        pass


class AnimalDB:
    def get_animal(self, id) -> Animal:
        pass

    def save(self, animal: Animal):
        pass

"""
When designing our classes, we should aim to put related features together, so
whenever they tend to change they change for the same reason.  And we should try
to separate features if they will change for different reasons. - Steve Fenton
"""

"""
The downside of this solution is that the clients of the this code have to deal
with two classes.  A common solution to this dilemma is to apply the Facade
pattern.  Animal class will be the Facade for animal database management and
animal properties management.
"""

class Animal:
    def __init__(self, name: str):
        self.name = name
        self.db = AnimalDB()

    def get_name(self):
        return self.name

    def get(self, id):
        return self.db.get_animal(id)
    
    def save(self):
        self.db.save(animal=self)


"""
The most important methods are kept in the Animal class and used as Facade for
the lesser functions.
"""