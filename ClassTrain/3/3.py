def gcd (a,b):
    for num in range (1,a+1):
        if a % num == 0:
            max1 = num
        for num in range (1,b+1):
            if b % num == 0:
                max2 = num
            if max1==max2:
                shared = max1
    return shared

num1=int(input("Enter Number 1: "))
num2=int(input("Enter Number 2: "))

print("Shared number is: ",gcd(num1,num2))
    