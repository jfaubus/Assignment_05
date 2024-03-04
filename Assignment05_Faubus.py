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
    #method to return the area of a rectangle
    def AreaRect(self, width, height):
        return width * height 
    
    #method to return the power of a number
    def PowerOfNumber(self, num, power):
        return num**power
    
    #method to return the type of argument
    def TypeOfArgument(self, argument):
        return type(argument)
    
def main():
    #creates an instance of the BasicMathOperations class
    instance = BasicMathOperations()

    #prints the options
    print("Here are your options: Greet (click 1) \n Addnumbers (click 2) \n Pick an operation (click 3) \n Return the square (click 4) \n Return the factorial (click 5) \n Counting (click 6) \n Calculate the hypotenuse (click 7) \n Compute the area of a rectangle (click 8) \n Return the power of a number (click 9) \n Return the type of argument (click 10)")
    #lets the user choose by number
    choice = int(input(" What option do you pick? "))

    #if the user chooses 1
    if choice == 1:
        #gets the necessary arguments from the user
        name = input("What is your first name? ")
        lastname = input("What is your last name? ")
        #passes teh arguments to the Greet method in the BasicMathOperations class
        print(instance.Greet(name, lastname))
   #if the user chooses 2
    elif choice == 2:
        #loops until the user chooses a valid input
        looping = True
        while looping:
          try: 
              #tries to get the necessary arguments
              num1 = int(input("What is the first number you want to add? "))
              num2 = int(input("What is the second number you want to add? "))
              looping = False
              #if successful, calls the Addnumbers() method using the instance
              print(instance.AddNumbers(num1, num2))
          #catches a situation where the user doesnt input a valid data type
          except ValueError:
              print("This is not a number, please try again")

main()