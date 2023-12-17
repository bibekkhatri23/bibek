# def sum(*numbers):
#     total=0
#     for number in numbers:
#         total+=number
#     print(total)
    
# sum(1,2,3,4)    
        
#for a single person

# def person(name):
#     print("My name is {}" .format(name))
    
# names=input("Enter your name:")
# person(names)

#for multiple persons
def person_names(names):
    for name in names:
        print("My name is {}" .format(name))
    
names_list={"bibek","bipin","mamta"}
person_names(names_list)

        
    