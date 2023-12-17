from abc import ABC,abstractmethod  #abstractmethod vannne decorator import gareko 

class Computer(ABC):
    def run(self,app):
        self.process(app)
        
@abstractmethod
def process(self,app):
    pass

class Mobile(Computer):
    def run(self,app):
        print("Mobile is running",app)
  
class Laptop(Computer):
    def run(self,app):
        print("Laptop is running",app)      

samsung=Mobile()
samsung.run("PUBG")

