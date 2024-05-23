class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        if self.width == self.height:
            representation = 'Square(side={})'.format(self.width)
            return representation
        else:
            representation = 'Rectangle(width={}, height={})'.format(self.width, self.height)
            return representation

    def set_width(self, width):
        self.width = width
        return True

    def set_height(self, height):
        self.height = height
        return True

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        picture = ''

        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        for line in range(1, self.height + 1):
            picture += '*' * self.width + '\n'

        return picture

    def get_amount_inside(self, other_shape):
        if (other_shape.width > self.width) and (other_shape.width > self.height):
            return 0
        elif (other_shape.height > self.width) and (other_shape.height > self.height):
            return 0
        else:
            num_of_fit = self.get_area() // other_shape.get_area()
            return num_of_fit

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        representation = 'Square(side={})'.format(self.width)
        return representation

    def set_side(self, side):
        self.width = side
        self.height = side
        return True

    def set_width(self, side):
        self.width = side
        self.height = side
        return True

    def set_height(self, side):
        self.width = side
        self.height = side
        return True
