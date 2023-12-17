class Person:
    def __init__(self,name,age,password):
        self.name=name
        self._age=age
        self._password=password
    
    @property
    
        
    def get_password(self):
        return self.__password
    
    
    # @password.setter
    def set_password(self,password):
        self.__password=password
    
    
    # password=property(get_password,set_password)
        
person=Person('ram',12,'passw123')
print(person.name)
print(person._age)
# person.set_password('123')
person.password=123
print(person.password)