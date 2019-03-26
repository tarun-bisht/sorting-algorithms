length=eval(input("Enter Number of Elements to Enter: "))
print("- - - - -Insert Elements and press Enter to insert next element- - - - - -")
a=[]
for i in range(length):
    number=eval(input())
    a.append(number)
print("Entered List::::\n",a)
from insertion_sort import insertion_sort
insertion_sort(a)
print("Sorted List::::\n",a)
