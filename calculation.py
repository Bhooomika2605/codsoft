
print("what operation you want to perform? ")
print("1.Addition (+)")
print("2.Substraction (-)")
print("3.Multiplication (*)")
print("4.Division (/)")


while True:
    a = int(input("Enter first digit: "))
    b = int(input("Enter second digit: ")) 
    
    cal = input("+,-,*,/: ")
    if cal == "+":
        c = a+b
        print("The result is",c)

    elif cal == "-":
        c = a-b
        print("The result is",c)
        
    elif cal == "*":
        c = a*b
        print("The result is",c)
        
        
    elif cal == "/":
        if b ==0:
          print("Sorry any number cannot be divide by zero(0)")
        else: 
            c = a/b
            print("The result is",c)
    
        
    else:
        print("Please! Enter a valid operation!!") 
        
    # ext = input("Enter 'Q' to exit or enter 'C' to contine ").lower()
    # if ext == "q":
    #   quit()

