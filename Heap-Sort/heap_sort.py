from heap import Heap
if __name__=="__main__":
    a=[1,5,3,8,2,9,3,8,4,6,7,1,6,4]
    heap=Heap(array=a)
    print("Original Array Heap: ",heap)
    heap.sort()
    print("Sorted Array using Heap Sort: ",heap)
