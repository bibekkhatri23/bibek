# a=10

# def  number():
#     a=11 
#     print(a)  # paila a laai funcn vitra khojcha na vetey ani bahira global variable bata access lincha
    
# number()
# print(a)


# a=10

# def  number():
#     global a
#     a=11 
#     print(a)  
    
# number()
# print(a)



# a=10
# def outer():
#     a=11
#     def inner():
#         print("inner sees a as",a)
#     inner()
#     print('outer sees a as',a)
    
# print('main sees a as',a)
# outer()
    
    
a=10
def outer():
    a=11
    def inner():
        global a
        print("inner sees a as",a)
    inner()
    print('outer sees a as',a)

outer()   
print('main sees a as',a)

    

