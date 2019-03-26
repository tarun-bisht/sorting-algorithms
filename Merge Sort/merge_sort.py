import math
def __merge(A,L,R):
    i=j=k=0
    a_len=len(A)
    l_len=len(L)
    r_len=len(R)
    while i<l_len and j<r_len:
        if L[i]<=R[j]:
            A[k]=L[i]
            i=i+1
        else:
            A[k]=R[j]
            j=j+1
        k=k+1
    while k<a_len:
        if(i<l_len):
            A[k]=L[i]
            i=i+1
        elif(j<r_len):
            A[k]=R[j]
            j=j+1
        k=k+1
def merge_sort(A):
    if len(A)>1:
        q=len(A)//2
        L=A[:q]
        R=A[q:]
        merge_sort(L)
        merge_sort(R)
        __merge(A,L,R)
def main():
    a=[8,6,9,4,2,3,7,2]
    sort(a)
    print(a)
if __name__=="__main__":
    main()
