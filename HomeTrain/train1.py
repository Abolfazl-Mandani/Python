# لیست برای ذخیره کارها
do_list = []

# پرسیدن برای کار مورد نیاز

print("Add : for enter new do list\nRemove : for delete an do job\nShow : for show all do list\nexit : for exit from app")
request = input("Enter what you need: ").lower()
print("---------------------------------")

while True:
    # خارج شدن از برنامه
    if request == "exit":
        break

    elif request == "add":
        # گرفتن اطلاعات از کاربر
        title = input("Enter the title: ")
        job = input("Enter the job you should do: ")
        deadline = input("Enter the deadline time: ")

        # اضافه کردن اطلاعات به لیست
        do_list.append({
            "title": title,
            "job": job,
            "deadline": deadline
        })
        print("---------------------------------")
        
        # پرسش برای کار بعدی
        print("Add : for enter new do list\nRemove : for delete an do job\nShow : for show all do list\nexit : for exit from app")
        request = input("Enter what you need: ").lower()
        print("---------------------------------")

    elif request == "remove":
        # حذف کردن کار از لیست
        index = int(input("Enter number of job you want to delete: "))
        do_list.pop(index)
        print("Remove successfuly done!!!")
        print("---------------------------------")
        
        # پرسش برای کار بعدی
        print("Add : for enter new do list\nRemove : for delete an do job\nShow : for show all do list\nexit : for exit from app")
        request = input("Enter what you need: ").lower()
        print("---------------------------------")

    elif request == "show":
        # نمایش اطلاعات لیست
        i=0
        print("Do List Information:")
        for task in do_list:
            print(f"index: {i} , Title: {task['title']} , Job: {task['job']} , Deadline: {task['deadline']}")
            i+=1
        print("---------------------------------")
        
        # پرسش برای کار بعدی
        print("Add : for enter new do list\nRemove : for delete an do job\nShow : for show all do list\nexit : for exit from app")
        request = input("Enter what you need: ").lower()
        print("---------------------------------")
    else:
        #بررسی درست بودن کار درخواستی
        print("WRONG COMMAND!!!")
        print("Please Enter command correctly")
        print("---------------------------------")
        
        # پرسش برای کار بعدی
        print("Add : for enter new do list\nRemove : for delete an do job\nShow : for show all do list\nexit : for exit from app")
        request = input("Enter what you need: ").lower()
        print("---------------------------------")
