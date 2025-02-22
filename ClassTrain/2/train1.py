num= int(input("Enter number :"))
sum =0
while True :
    if num==0:
        break
    else :
        num=num**3
        sum+=num
        print (num)
        print("-------------------------")
        num= int(input("Enter number (enter 0 to exit):"))

print("Sum Of Numbers",sum)