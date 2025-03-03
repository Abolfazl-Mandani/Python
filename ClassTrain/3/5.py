def max(*a):
    max=0
    for num in a:
        max = num if num > max else max
    return max

nums=[]
num1=int(input("Enter Number 1: "))
for num in range(num1):
    a=int(input("Enter Number: "))
    nums.append(a)
print(max(*nums))