#! /usr/bin/python3

def fibonachi(num):
    a =0
    b=1
    result=[]
    for i in range(num):
        c=a+b
        a=b
        b=c
    return c
        
    
    #return result
#fibonachi(5)   
      
print(fibonachi(8))
