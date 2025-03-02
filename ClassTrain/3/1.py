def max (a,b,c):
    max = a if a>b else b
    max = max if max>c else c
    return max

num1=int(input("Enter Number 1: "))
num2=int(input("Enter Number 2: "))
num3=int(input("Enter Number 3: "))

print("Max Number is: ",max(num1,num2,num3))
    