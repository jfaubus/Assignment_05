#starts the BasicMath Operations class
class BasicMathOperations():
    #initializer
    def __init__(self):
        None

    #method for greeting someone with their firt and last name
    def Greet(self, first, last):
        return f"hello, {first} {last}"
    
    #method to return the sum of two numbers
    def AddNumbers(self, num1, num2):
        return int(num1) + int(num2)