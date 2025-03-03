import random
#گرفتن عدد اولیه از بازیکن
PlayerNUmber = int(input("Please Enter Your g Number : "))

#گرفتن عدد اولیه از رباط
number = random.randint(1, 3)

#تعریف متغیر برای امتیاز و تعداد حدث
Score = 1
count = 3

#ایجاد حلقه برای انجام بازی تا زمان بدست اوردن امتیاز کامل یا شکست
while True:
    
    #بررسی امتیاز بازیکن برای برد
    if Score == 4:
        print("--------------------------------")
        print("--------------------------------")
        print("Congrats You Win The Whole Game!!!!!!")
        print("--------------------------------")
        print("--------------------------------")
        break
    
    #بررسی امتیاز بازیکن برای باخت
    elif Score == 0:
        print("--------------------------------")
        print("--------------------------------")
        print("You Lost Sucker!!!!")
        print("--------------------------------")
        print("--------------------------------")
        print("--------------------------------")
        break
    
    #انجام بازی برای بدست اوردن یا از دست دادن امتیاز
    else:
        
        #ایجاد حلقه برای تعداد متعدد بازی
        while True:
            
            #زمانی که بازیکن عدد را درست حدث بزند
            if number == PlayerNUmber:
                print("--------------------------------")
                print("you did it good for you!!!!")
                print("your Score is : ", Score)
                print("The Number Was : ", number)
                
                #افزودن امتیاز
                Score += 1
                
                #باز گرداندن تعداد حدث
                count = 3
                
                #بررسی بدست آمدن امتیاز کامل
                if Score != 4:
                    
                    #گرفتن عدد جدید از رباط
                    number = random.randint(1, 3)
                    #گرفتن عدد جدید از کاربر
                    PlayerNUmber = int(input("Please Enter Your g Number : "))
                    print("--------------------------------")
                    break
                
                else:
                    break
                
            #زمانی که بازیکن دیگر شانسی برای حدث زدن ندارد
            elif count == 0:
                print("--------------------------------")
                print("You Loss || now you fuckedup")
                
                #کم کردن امتیاز
                Score -= 1
                
                #باز گرداندن تعداد حدث
                count = 3
                
                # بررسی امتیاز برای باخت کامل
                if Score != 0:
                    print("your Score is : ", Score-1)
                    print("The Number Was : ", number)
                    
                    #گرفتن عدد جدید از رباط
                    number = random.randint(1, 3)
                    
                    #گرفتن عدد جدید از بازیکن
                    PlayerNUmber = int(input("Please Enter Your g Number : "))
                    print("--------------------------------")
                    break
                
                else:
                    print("your Score is : ", Score)
                    print("The Number Was : ", number)
                    print("--------------------------------")
                    break
                
            #زمانی که بازیکن هنوز شانس برای حدث زدن دارد
            else:
                #کم کردن تعداد حدث
                count -= 1
                
                #بررسی اتمام تعداد حدث
                if count != 0:
                    print("--------------------------------")
                    print("Your Number Wasnt Right!!!! \nPlease Try Again")
                    print(f"You Have {count} More Chanse")
                    
                    #گرفتن عدد جدید از بازیکن
                    PlayerNUmber = int(input("Please Enter Your g Number : "))
                    print("--------------------------------")
                    
                else:
                    break
