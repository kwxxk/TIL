class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return int(self.width * self.height)

    def calculate_perimeter(self):
        return int(2*(self.width+self.height))

    def print_info(self):
        print(f'Width: {self.width}\nHeight: {self.height}\nArea: {self.calculate_area()}\nPerimeter: {self.calculate_perimeter()}')

    def __str__(self):
        return f'Shape: width={self.width}, height={self.height}'
shape1 = Shape(5, 3)
print(shape1)

