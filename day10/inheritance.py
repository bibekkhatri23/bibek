class GrandFather:
    house="luxury house"
    def __init__(self)-> None:
        print("GrandFather")
    
    def get_house(self):
        return(self.house)
 
class Grandmother:
    def __init__(self)-> None:
        print("Grandmother")
    
    jwellery="sun wala diamond"
 
    
class Father(GrandFather,Grandmother):
    
    def __init__(self)-> None:   #mathi ko init method(constructor) override huncha ani last ma jun init lekhe huncha tei init override vayera output dincha
        print("Father")
    car="mercedes"
    
    def get_house(self):
        print(super().get_house()) #ek step mathi ko parent ko method lai trigger garcha super ley ani mathi ko method ni print garcha
        return("hency ghar")
    
    
class Son(Father):
    console="ps5"
    



father=Father()
print(father.get_house())
# son=Son()
# print(son.console)

print(isinstance(Grandmother,object))    #isinstance lai object ni vanchan ani kunai pani object ya instance kun class ma belong garcha vanera check garcha
    
# # print(father.jwellery)
    
