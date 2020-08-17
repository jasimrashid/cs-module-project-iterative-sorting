arr = [4,0,5,2,3,1]

# O(n)
def find_num(arr, target_num):
    for x in arr:
        if x == target_num:
            return x
        return -1

# arr = [0, 1, 2, 3, 4, 5, 98, 99]

arr = [98,99,5,2,3,1,4,0]

def insertion_sort(arr):
    # start looping at the second element
    for i in range(1, len(arr)):
        # pick up the current element and hold it
        current_element = arr[i]
        current_i = i
        # while current element is less than left sibling
        while current_i > 0 and current_element < arr[current_i - 1]:
            # copy left sibling to the right
            arr[current_i] = arr[current_i - 1]
            # decrement index
            current_i -= 1
        # finally put our currrent element down
        arr[current_i] = current_element

insertion_sort(arr)   
print(arr)
# time complexity