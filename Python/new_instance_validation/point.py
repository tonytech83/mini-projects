class Point2D:

    def __new__(cls, x, y):
        if isinstance(x, int) and isinstance(x, int):
            # Allocate memory and return a new object
            # only when the if-condition is True
            print('Creating Object!')
            return super().__new__(cls)  # Return new object
        else:
            raise ValueError('x and y must be integers')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print('Object was initialized!')


p1 = Point2D(1, 2)
# Creating Object!          # from __new__() method
# Object was initialized!   # from __init__() method

p2 = Point2D(1.2, 2.5)
# ValueError: x and y must be integers  # form __new__() method