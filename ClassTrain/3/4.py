def sort(a):
    if a==0:
        return 
    else:
        print(a)
        sort(a-1)

num1=int(input("Enter Number 1: "))
sort(num1)
