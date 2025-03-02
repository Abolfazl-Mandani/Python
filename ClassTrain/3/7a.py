def fug(a,b,c):
    for num in range(c):
        print(a)
        a,b=b,a+b



num1=int(input("Enter Number 1: "))
fug(1,1,num1)