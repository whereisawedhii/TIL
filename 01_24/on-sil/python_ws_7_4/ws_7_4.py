# 아래 클래스를 수정하시오.
class Shape: 

    def __init__(self, width, height) :
        self.width = width
        self.height = height
        self.area = self.width * self.height
        self.perimeter = (self.width + self.height) * 2
    
    def print_info(self):
        print(f'Width : {self.width}\nHeight: {self.height}\nArea: {self.area}\nPerimeter: {self.perimeter}')


shape1 = Shape(5, 3)
shape1.print_info()
