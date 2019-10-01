for i in range(7):
     if i==0 or i==6:
        for j in range(4):
            print("*", end="")
   

     elif i==3:
        for j in range(i):
            print("*", end="")
     else:
        print("*", end="")
     print()
