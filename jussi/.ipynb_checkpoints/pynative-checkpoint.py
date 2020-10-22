"""for z in range(8):
    for a in range(z):
        print(z,end="")
    print("")"""

"""for a in range(7,0,-1):
    for b in range(a):
        print(a ,end="")
    print("")"""

for a in range(7):
    for b in range(a):
        print("0",end="")
    
    for c in range((7-a)*2):
        print(" " ,end="")
   
    for d in range(a):
         print("0",end="")
    print(" ")
