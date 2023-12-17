# #always returns functon

# def sum_by_ten(a):
#     return a+10

# s=lambda a:a+10  #store garcha
# print(s(20))  #lambda lai normally aru function jastai call garna mildaina kina ki esle jaile return garcha

# #print(sum_by_ten(2))
    
    
# def myfunc(n):
#     return lambda x:x*n

# #lambda x:x*2
# doubler=myfunc(2)

# print(doubler(10))
# print(doubler(30))


def myfunc(n):
    return lambda x:x*x

#lambda x:x*x
tripler=myfunc(3)

print(tripler(10))
print(tripler(30))
       

