#user defined module
def fact(x):
    y=1
    if x==1 or x==0:
        return y
    
    else:
        y=x*fact(x-1)
        return y
