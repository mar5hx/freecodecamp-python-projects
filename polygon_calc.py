import math#used for get diagonal (sqrt specifically)

class Rectangle:#parent

    
    def __init__(self, width, height):#Initializes the rectangle 
    #with width and height attributes
        self.width = width 
        self.height = height
    
    def set_width(self, new_width):#Sets the width of the rectangle
        self.width = new_width

    def set_height(self, new_height):#Sets the height of rectangle
        self.height = new_height
    
    def get_area(self):#returns area
        return self.height * self.width

    def get_perimeter(self):
        return 2 * (self.width + self.height)#returns the perimeter 
    
    def get_diagonal(self):#returns the diagonal
        return math.sqrt(self.width**2 + self.height**2)

    def get_picture(self):#Shows width as "*" on x axis / "*" y axis for height
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        lines = []
        for line in range(self.height):
            lines.append(self.width * "*" + "\n")
        return "".join(lines)
    
    def get_amount_inside(self, another_shape):#get the amount another shape can fit in shape 1 horizontally
    #same applies vertically, the total for x and y and then multiplied and returned
        fit_height = self.height // another_shape.height
        fit_width = self.width // another_shape.width
        return fit_height * fit_width 
    
    def __str__(self):#Prints rectangle with height and width
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):#Child class(inheritance)
    
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, side):#Sets width must use self.width and self.height 
    #Square has equal sides, changing a side will change height and width)
        self.width = side
        self.height = side
    
    def set_height(self, side):#Same rule as set width
        self.height = side
        self.width = side

    def set_side(self,side): #Same rule as height and width
    #Differnt way to write it (could also be written this way for height)
        self.set_width(side)
    
    def __str__(self):#width or height with work here behind self bc square
        return f"Square(side={self.width})"
    
