def insertion_sort(numbers):
    for i in range(1,len(numbers)):
        key=numbers[i]
        j=i-1
        while j>=0 and key < numbers[j] :
            numbers[j+1]=numbers[j]
            j=j-1
        numbers[j+1]=key

def main():
    numbers=[3,5,2,9,1,5,0,3]
    print("Actual List Entered:  ")
    print(numbers)
    insertion_sort(numbers)
    print("Sorted Order of List:  ")
    print(numbers)

if (__name__=="__main__"):
    main()
