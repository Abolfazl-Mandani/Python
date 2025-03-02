def fug(a,b,c):
        if c != 0:
            print(a)
            a,b=b,a+b
            fug(a,b,c-1)



num1=int(input("Enter Number 1: "))
fug(1,1,num1)