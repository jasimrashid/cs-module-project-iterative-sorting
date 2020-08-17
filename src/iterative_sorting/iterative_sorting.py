# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    # for i in range(0, len(arr) - 1):
    #     cur_index = i
    #     smallest_index = cur_index
    #     # TO-DO: find next smallest element
    #     # (hint, can do in 3 loc)
    #     # Your code here

    for i in range(len(arr),1,-1):
        # print(arr[i-1])
        print(i-1)
        print(arr[:i])
        max_i = arr.index(max(arr[:i]   ))
        print(max_i)
        arr[max_i], arr[i-1] = arr[i-1], arr[max_i]
        # print(max(arr[:i]))
        # arr[i-1] = max(arr[:i])
        print(arr)
        print('-')
        # print(i-1)
        # for j in range(i-1):
        #     print(arr[j])
        #     if arr[j] > arr[j+1]:
        #         # swap elements
        #         arr[j], arr[j+1] = arr[jp+1], arr[j]
        # print('-')


        # TO-DO: swap
        # Your code here

    return arr

arr = [5,3,7,0,11,55,2,77]
print(arr)
selection_sort(arr)
print(arr)


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # step 1: loop through array. compare each element to its neighbor. swap if not ascending. at the end of this "pass", the largest element will be at the end
    # step 2: repeate step 1 but from 0 to len(arr) minus 1
    # step 2: if no swaps, stop. else go back to element at index 0 athisnd repeat step 1

    for i in range(len(arr),1,-1):
        # print(arr[i-1])
        print(i-1)
        for j in range(i-1):
            print(arr[j])
            if arr[j] > arr[j+1]:
                # swap elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print('-')
                

    return arr


# arr = [5,3,7,0,11,55,2,77]
# print(arr)
# bubble_sort(arr)
# print(arr)

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
