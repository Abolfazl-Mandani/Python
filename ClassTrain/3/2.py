def tof (a,b):
    if a % b == 0:
        return True
    else:
        return False
    
num1=int(input("Enter Number 1: "))
num2=int(input("Enter Number 2: "))

if tof(num1,num2):
    print("Number ", num1," can be devided by Number ", num2)
else:
    print("Number ", num1," can't be devided by Number ", num2)
    
