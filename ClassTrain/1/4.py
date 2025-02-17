number=int(input("Enter Your Number :"))
R=S=0
i=0
while number != 0:
    R = number % 2
    number//=2
    S = S + R*(10**i)
    i+=1
    
print("Your Number In Binery Is : ",S)

S=bin(number)

print("Your Number In Binery(fun) Is : ",S)
    
