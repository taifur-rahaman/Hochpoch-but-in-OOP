
class Calculator:
    def __init__(self, *args):
        self.args = args
        
    def addition(self):
        return sum(self.args)
    
    def subtraction(self):
        self.sum = 0
        for arg in self.args:
            self.sum -= arg
        return self.sum
    
    def multiplication(self):
        self.product = 1
        for arg in self.args:
            self.product *= arg
        return self.product
    
    def division(self):
        if self.args[1] == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return self.args[0] / self.args[1]


# # Test Code
# if __name__ == "__main__":
#     try:
#         cal = []
#         numbers = Calculator(list(map(int, input("Enter numbers separated by spaces: ").split())))
#         cal = Calculator(*numbers)
#     except TypeError as e:
#         print(e)
#     except ZeroDivisionError as e:
#         print(e)

#     print(cal.addition())
#     print(cal.subtraction())
#     print(cal.multiplication())
#     print(cal.division())
