def divider():
    num1=int(input("enter two number:"))
    num2=int(input("enter two number:"))
    if num1==5:
        raise Exception("Input Number cannot be 5")    # divider ley 5 vanne number lidai na liye afno exception banako ho yo
        
    print(num1/num2)



while True:
    try:
        divider()
        
    except ZeroDivisionError:
        print('cannot divide any number by 0')
        
    except Exception as e:      #thanavako exception haru esari exception gari rakhna sakincha
        print('Something went wrong',e)
        
    #hamlai jati chaiyo teti exception rakhna sakchau
        
        
    
        
        