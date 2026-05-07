#Calculator 
while True:
      
    a = int(input("Enter a 1st Number for calculation:"))
    b = int(input("Enter 2nd Number for calculation:"))
    choice = (input("Enter your number of your choice to perfom calculation\n "
                "1. Addition\n"
                "2. Subtraction\n"
                "3. Multiplication\n"
                "4. Division\n"
                "5. Modulus\n"
                "6. Square\n"
                "7. Square root\n"))

    def add(a,b):
        result = a+b
        print("The result of addition is :",result)
    def sub(a,b):
        result = a-b
        print("The result of subtraction:",result)
    def mult(a,b):
        result = a*b
        print("The result of multiplication is :",result)
    def divison(a,b):
        try:
              result = a/b
              print("The result of Divison is : ",result)
        except ZeroDivisionError: 
              print("Can't Divide By Zero")


    def module(a,b):
        result = a%b
        print("The result of Modulus is: ",result)
    def square(a,b):
      result = a*a
      result1 = b*b
      print("The sqaure for 1st num is: ",result)
      print("Square for 2nd num is : ",result1)
    def sqroot(a,b):
      result = a**0.5
      result1 = b**0.5
      print("The sqaure root for 1st num is: ",result)
      print("The square root for 2nd num is : ",result1)



    if choice == "1":
        add(a,b)

    elif choice == "2":
     sub(a,b)

    elif choice == "3":
        mult(a,b)

    elif choice== "4":
      divison(a,b)

    elif choice== "5":
        module(a,b)
    elif choice == "6":
      square(a,b)
    elif choice =="7":
      sqroot(a,b)
    else:
        print("Entered choice is invalid")

    c = input("If user wishes to continue? (yes or no)")
    if c == "no":
        break
      


