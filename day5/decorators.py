def hashtag(func):
    def don():
        print("#"*10)
        print("*"*10)
        func()
        print("*"*10)
        print("#"*10)
    return don
# @hashtag    
# def hello():
#     print('hello')

@hashtag
def world():
    print('world')
    
# hello()    
world()
    
    
