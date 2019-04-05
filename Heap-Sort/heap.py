class Heap:
    def __init__(self,array,type="max"):
        self.type=type
        self.size=len(array)
        self.heap=array
        self.__build_Heap()
    def __str__(self):
        string=""
        for h in self.heap:
            string=string+f"| {h} "
        return string
    def __repr__(self):
        string=""
        for h in self.heap:
            string=string+f"| {h} "
        return string
    def __le__(self):
        return self.size
    def parent(self,index):
        return index//2
    def left(self,index):
        return 2*index
    def right(self,index):
        return 2*index+1
    def maximum(self):
        if self.type=="max":
            return A[0]
        elif self.type=="min":
            return A[self.size-1]
    def minimum(self):
        if self.type=="max":
            return A[self.size-1]
        elif self.type=="min":
            return A[0]
    def sort(self):
        index=self.size-1
        while index>0:
            self.__swap(index,0)
            index=index-1
            self.__max_heapify(0,index)
    def __build_Heap(self):
        if self.type=="max":
            i=len(self.heap)//2-1
            while i>=0:
                self.__max_heapify(i,self.size)
                i=i-1
        elif self.type=="min":
            i=len(self.heap)//2-1
            while i>=0:
                self.__min_heapify(i,self.size)
                i=i-1
        else:
            raise TypeError("Wrong Heap Type Specified")
    def __min_heapify(self,index,size):
        l=self.left(index=index)
        r=self.right(index=index)
        if l<size and self.heap[l]<self.heap[index]:
            minimum=l
        else:
            minimum=index
        if r<size and self.heap[r]<self.heap[minimum]:
            minimum=r
        if not minimum==index:
            self.__swap(index,minimum)
            self.__min_heapify(minimum,size)
    def __max_heapify(self,index,size):
        l=self.left(index=index)
        r=self.right(index=index)
        if l<size and self.heap[l]>self.heap[index]:
            largest=l
        else:
            largest=index
        if r<size and self.heap[r]>self.heap[largest]:
            largest=r
        if not largest==index:
            self.__swap(index,largest)
            self.__max_heapify(largest,size)
    def __swap(self,p,q):
        c=self.heap[p]
        self.heap[p]=self.heap[q]
        self.heap[q]=c

if __name__=="__main__":
    a=[1,5,3,8,2,9]
    heap=Heap(a,type="max")
    print(heap)
