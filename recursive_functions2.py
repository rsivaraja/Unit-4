def exponent(x,y):
    if y==1:
        return x
    else:
        return x*exponent(x,y-1)
    
print(exponent(2,5))