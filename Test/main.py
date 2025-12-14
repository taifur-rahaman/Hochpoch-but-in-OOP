class Reactangle:
    
    count = 0
    
    def __init__(self, width = 1, height = 1):
        self._width = width
        self._height = height
        Reactangle.count += 1
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, new_width):
        if new_width >= 0:
            self._width = new_width
        else:
            print("Width Can't be equal or less to Zero")
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, new_height):
        if new_height >= 0:
            self._height = new_height
        else:
            print("Height Can't be equal or less to Zero")
    
    def area(self):
        print(f"{self._width * self._height}")

r1 = Reactangle()
r1.height = -5
r1.width = -4
