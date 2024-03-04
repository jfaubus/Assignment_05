import math as m

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
    
    #method to perform the operation of the user's choosing
    def Operations(self, num1, num2, operation):
        if operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            return num1 / num2
        elif operation == "sum":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        else:
            print( "the operation was not valid")
            operation = input("Please enter either multiply, divide, sum, or subtract " )
            return BasicMathOperations.Operations(self, num1, num2, operation)
        
    #method to return the square of a number
    def square(self, num):
        return num**2
    

    #method to return the factorial of a number
    def factorial(self, num):
        factori = 1
        for i in range(1, num + 1):
            factori *= i
        return factori
    
    #method to count from the specifed first number to the specified second number
    def counting(self, start, end):
        for i in range(start, end + 1):
            print(i)

    #method to calculate the squar of a number
    def calculateSquare(self, num):
        return num**2
    
    #used the calculateSquare method to return the hypotenuse of a right triangle
    def calculateHypotenuse(self, Base, Height):
        return m.sqrt(BasicMathOperations.calculateSquare(Base) + BasicMathOperations.calculateSquare(Height))