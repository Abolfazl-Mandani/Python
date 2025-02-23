i=1
number=1
sum=0
sumfull=1
for num in range(1,10):
    number=num
    while number>0:
        sum+=num*(number-1)
        number -=1
        print(sum)
    # sumfull+=i/sum
print(sumfull)