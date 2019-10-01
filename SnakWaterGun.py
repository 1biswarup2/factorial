import random
g=1
c=0
d=0
while g<=10:
    l=["s","w","g"]
    b=random.choice(l)
    

    a=input("enter s for snake;w for water;g for gun\n")
    if b=="s" and a=="w":
        print(b)
        print("you lose")
        g=g+1
        c+=1
    elif b=="s" and a=="g":
        print(b)
        print("you win")
        g=g+1
        d+=1
    elif b=="w" and a=="g":
        print(b)
        print("you lose")
        g=g+1
        c+=1
    elif b=="w" and a=="s":
        print(b)
        print("you win")
        g=g+1
        d+=1
    elif b=="g" and a=="s":
        print(b)
        print("you lose")
        g=g+1
        c+=1
    elif b=="g" and a=="w":
        print(b)
        print("you win")
        g=g+1
        d+=1
    else:
        print("draw")

if c>d:
    print("computer wins")
else:
    print("you are the winner bro.")
  
        
        
