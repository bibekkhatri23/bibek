# print("Calculator")
# print("1.Add")
# print("2.Substract")
# print("3.Multiply")
# print("4.Divide")

# # input 
# ch=int(input("Choose(1-4): "))  #choose

# if ch==1:
#     a=int(input("Enter A:"))
#     b=int(input("Enter B:"))
#     c=a+b
#     print("Sum = ",c)
# elif ch==2:
#     a=int(input("Enter A:"))
#     b=int(input("Enter B:"))
#     c=a-b
#     print("Difference = ",c)
# elif  ch==3:
#     a=int(input("Enter A:"))
#     b=int(input("Enter B:"))
#     c=a*b
#     print("Product = ",c)
# elif ch==4:
#     a=int(input("Enter A:"))
#     b=int(input("Enter B:"))
    
    
#     if b !=0:
#         c= a/b
#         print("Result :",c)
#     else:
#         print("Error:Division by zero is not allowed .")
        
    
# else:
#     print("Invalid Choice")





def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: Division by zero is not allowed.")
        return None

def calculator():
    print("Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Input
    ch = int(input("Choose (1-4): "))  # choose

    if ch in (1, 2, 3, 4):
        a = int(input("Enter A: "))
        b = int(input("Enter B: "))

        if ch == 1:
            result = add(a, b)
            print("Sum =", result)
        elif ch == 2:
            result = subtract(a, b)
            print("Difference =", result)
        elif ch == 3:
            result = multiply(a, b)
            print("Product =", result)
        elif ch == 4:
            result = divide(a, b)
            if result is not None:
                print("Result :", result)
    else:
        print("Invalid Choice")

# Call the calculator function
calculator()
