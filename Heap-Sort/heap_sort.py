## Start Taking Input
try:
    length=eval(input("Enter Number of Elements to Enter: "))
    print("- - - - -Insert Elements and press Enter to insert next element- - - - - -")
    a=[]
    for i in range(length):
        number=eval(input())
        a.append(number)
except Exception as e:
    print(f"Cannot take input there is a error::{e}")
print("Entered List::::\n",a)
## End Taking Input
##Importing Binary Heap Class
from binary_heap import BinaryHeap
##Creating binary heap object
heap=BinaryHeap(array=a)
##Sort Function using heap sort technique
def sort(heap):
    index=len(heap)-1
    while index>0:
        heap.swap(index,0)
        index=index-1
        heap.max_heapify(0,index)
##printing heap object
print("Original Heap: ",heap)
##Sorting
sort(heap)
print("Sorted Array using Heap Sort: ",heap)
##Accessing all elements of heap
for i in heap:
    print(i)
