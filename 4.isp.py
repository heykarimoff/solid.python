"""
Interface Segregation Principle
Make fine grained interfaces that are client specific
Clients should not be forced to depend upon interfaces that they do not use.
This principle deals with the disadvantages of implementing big interfaces.

Let’s look at the below IShape interface:
"""

class IShape:
    def draw_square(self):
        raise NotImplementedError
    
    def draw_rectangle(self):
        raise NotImplementedError
    
    def draw_circle(self):
        raise NotImplementedError

"""
This interface draws squares, circles, rectangles. class Circle, Square or Rectangle implementing the IShape 
interface must define the methods draw_square(), draw_rectangle(), draw_circle().
"""

class Circle(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass
    
    def draw_circle(self):
        pass

class Square(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass
    
    def draw_circle(self):
        pass

class Rectangle(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass
    
    def draw_circle(self):
        pass

"""
It’s quite funny looking at the code above. class Rectangle implements methods (draw_circle and draw_square) it has no use of, 
likewise Square implementing draw_circle, and draw_rectangle, and class Circle (draw_square, draw_rectangle).

If we add another method to the IShape interface, like draw_triangle(),
"""

class IShape:
    def draw_square(self):
        raise NotImplementedError
    
    def draw_rectangle(self):
        raise NotImplementedError
    
    def draw_circle(self):
        raise NotImplementedError
    
    def draw_triangle(self):
        raise NotImplementedError


"""
the classes must implement the new method or error will be thrown.

We see that it is impossible to implement a shape that can draw a circle but not a rectangle or a square or a triangle. 
We can just implement the methods to throw an error that shows the operation cannot be performed.

ISP frowns against the design of this IShape interface. clients (here Rectangle, Circle, and Square) should not be forced to depend on methods that they do not need or use. 
Also, ISP states that interfaces should perform only one job (just like the SRP principle) any extra grouping of behavior should be abstracted away to another interface.

Here, our IShape interface performs actions that should be handled independently by other interfaces.

To make our IShape interface conform to the ISP principle, we segregate the actions to different interfaces.
Classes (Circle, Rectangle, Square, Triangle, etc) can just inherit from the IShape interface and implement their own draw behavior.
"""

class IShape:
    def draw(self):
        raise NotImplementedError

class Circle(IShape):
    def draw(self):
        pass

class Square(IShape):
    def draw(self):
        pass

class Rectangle(IShape):
    def draw(self):
        pass

"""
We can then use the I -interfaces to create Shape specifics like Semi Circle, Right-Angled Triangle, Equilateral Triangle, Blunt-Edged Rectangle, etc.
"""