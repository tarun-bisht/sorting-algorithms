## Written by::: TARUN BISHT
##Binary Heap class
'''Arguments::::
    1:: Array to make heap
    2:: Type of heap
'''
class BinaryHeap:
    ##Constructor
    def __init__(self,array,type="max"):
        self.type=type
        self.__size=len(array)
        self.heap=array
        self.__build_Heap()
    ##Returns string representation for heap
    def __str__(self):
        string=""
        for h in self.heap:
            string=string+f"| {h} "
        return string
    ##Return Representation of heap object
    def __repr__(self):
        string=""
        for h in self.heap:
            string=string+f"| {h} "
        return string
    ##returns length of heap
    def __len__(self):
        return self.__size
    ##Heap Iterator using Generators
    def __iter__(self):
        for i in self.heap:
            yield i
    ## returns Parent Index of element at index
    def parent(self,index):
        p=index//2
        if p<0 or index>self.__size:
            raise Exception("index of parent element not Found")
        return p
    ## returns Left Index of element at index
    def left(self,index):
        l=2*index+1
        if l<1 or index>self.__size:
            raise Exception("index of left element not Found")
        return l
    ## returns Right Index of element at index
    def right(self,index):
        r=self.left(index)+1
        if r<1 or index>self.__size:
            raise Exception("index of right element not Found")
        return r
    ##returns Maximum element of heap
    def maximum(self):
        if self.type=="max":
            return A[0]
        elif self.type=="min":
            return A[self.__size-1]
    ## returns Minimum Index of element at index
    def minimum(self):
        if self.type=="max":
            return A[self.__size-1]
        elif self.type=="min":
            return A[0]
    ##Convert array to binary heap of type specified
    def __build_Heap(self):
        if self.type=="max":
            i=len(self.heap)//2-1
            while i>=0:
                self.max_heapify(i,self.__size)
                i=i-1
        elif self.type=="min":
            i=len(self.heap)//2-1
            while i>=0:
                self.min_heapify(i,self.__size)
                i=i-1
        else:
            raise TypeError("Wrong Heap Type Specified")
    '''
    Maxify the heap:: ie...
    make the parent of all elements maximum to their children
    arg::   index -> from where elements have to Maxify
            size -> till where to maxify
    '''
    def min_heapify(self,index,size):
        l=self.left(index=index)
        r=self.right(index=index)
        if l<size and self.heap[l]<self.heap[index]:
            minimum=l
        else:
            minimum=index
        if r<size and self.heap[r]<self.heap[minimum]:
            minimum=r
        if not minimum==index:
            self.swap(index,minimum)
            self.min_heapify(minimum,size)
    '''
    Maxify the heap:: ie...
    make the parent of all elements maximum to their children
    arg::   index -> from where elements have to Maxify
            size -> till where to maxify
    '''
    def max_heapify(self,index,size):
        l=self.left(index=index)
        r=self.right(index=index)
        if l<size and self.heap[l]>self.heap[index]:
            largest=l
        else:
            largest=index
        if r<size and self.heap[r]>self.heap[largest]:
            largest=r
        if not largest==index:
            self.swap(index,largest)
            self.max_heapify(largest,size)
    '''
    swap the elements of heap
    '''
    def swap(self,p,q):
        if p>self.__size or p<0 or q>self.__size or q<0:
            raise Exception("Index out of range:: Cannot swap elements in specifie index")
        c=self.heap[p]
        self.heap[p]=self.heap[q]
        self.heap[q]=c
##Main Function
if __name__=="__main__":
    a=[1,5,3,8,2,9]
    heap=BinaryHeap(a,type="max")
    print(heap)
