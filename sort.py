list = []
list1=[]

list_length = int(input("please enter length of list: "))

for i in range(list_length):
    numbers = int(input("please enter numbers of list: "))
    list.append(numbers)
    list1.append(numbers)

list1.sort()
if list == list1:
    print("Your list is sort")
else:
    print("Your lsit is not sort.")
