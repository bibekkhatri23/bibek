class House:
    
    
    def __init__(self,name,window=1,door=2,color="red",price=200):
       self.price=price
       self.name=name
       self.window=window
       self.color=color
       self.door=door
    
    def __str__(self) -> str:
        return f"{self.name} ko ghar"
    
    def __eq__(self,value) -> bool:
        return self.window==value.window
    
    def __gt__(self,value) -> bool:
        return self.price==value.price
       
   
    def set_color(self,color):   #yo chai function ko color vaihalyo
        self.color=color  #yo class ko color ho
    
    def get_color(self):
        return self.color
    
    
    
ram_ko_ghar=House(name="ram") 
print(ram_ko_ghar)

babe_ko_ghar=House(name="babe",window=1,color="black")
 # ram_ko_ghar.set_color("green")
# print(ram_ko_ghar.get_color())
# print(babe_ko_ghar.get_color())

is_name=ram_ko_ghar.__gt__(babe_ko_ghar)
print(is_name)