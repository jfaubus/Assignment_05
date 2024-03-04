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