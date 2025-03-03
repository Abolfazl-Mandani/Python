
def calculate_sum(a, s):
    if a == 0:
        return s
    else:
        s += a
        return calculate_sum(a - 1, s)  

num1 = int(input("Enter Number 1: "))
print(calculate_sum(num1, 0))  