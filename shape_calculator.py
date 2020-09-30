class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # method for setting width
    def set_width(self, width):
        self.width = width
    # method for setting height
    def set_height(self, height):
        self.height = height
    
    # method to get area
    def get_area(self):
        area = self.width * self.height
        return area
    # method to get perimeter
    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter
    
    # method to get diagnol
    def get_diagonal(self):
        diagonal = ((self.width ** 2) + (self.height ** 2)) ** .5
        return diagonal
    
    # Method to draw shape
    def get_picture(self):
        if self.height > 50 or self.width >50:
            picture = 'Too big for picture.'
            return picture
        else:
            picture = '*' * self.width + '\n'
            picture = picture * self.height
            return picture
    
    # Method to check how many fit inside.
    def get_amount_inside(self, shape):
        amount = self.get_area() // shape.get_area()
     
        return amount
    
    # string output
    def __str__(self):
        output = f'Rectangle(width={self.width}, height={self.height})'
        return output
        





class Square(Rectangle):
    def __init__(self, length):
        self.width = length
        self.height = length
    
    # set side method
    def set_side(self, length):
        self.height = length
        self.width = length
    
    # set width and height
    def set_width(self, length):
        self.height = length
        self.width = length

    def set_height(self, length):
        self.height = length
        self.width = length
    
    # output string
    def __str__(self):
        output = f'Square(side={self.width})'
        return output
