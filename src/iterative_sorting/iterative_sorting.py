# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        sorted_boundary = i
        smallest_index = sorted_boundary
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        # iterate through the unsorted portion of the array
        # finding the index of the smalllest element in the unsorted portion
        for unsorted_index in range(sorted_boundary, len(arr)):
            # if we find a value < smallest_index element,
            # update our smallest_index variable
            if arr[unsorted_index] < arr[smallest_index]:
                smallest_index = unsorted_index
        
        # we've found the smallest element in the unsorted portion
        # swap it with the element right next to the boundary
        arr[smallest_index], arr[sorted_boundary] = arr[sorted_boundary], arr[smallest_index]

        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr, unsorted_length):
    # Your code here
    # it traverses the array 
    # loop until no more swaps occur
    # swaps_occurred = True

    # while swaps_occurred:
    #     swaps_occurred = False

    #     for i in range (0, len(arr) - 1):
    #         #compare two elements
    #         if arr[i] > arr[i+1]:
    #             arr[i], arr[i+1] = arr[i+1], arr[i]
    #             swaps_occurred = True


    # return arr

    # recursive implementation of bubble sort
    # base case
    # what's the length of the unsorted portion of our array?
    # once we get to an empty sorted portion, thn everything is sorted

    # how are we moving closer to our base case

    for i in range(0, unsorted_length -1):
        #compare two elements
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    if unsorted_length > 0:
        bubble_sort(arr, unsorted_length - 1)

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
