def linear_search(arr, target):
    # Your code here
    counter = 0 
    while len(arr) > counter:
        if arr[counter] == target:
            return counter
        else: 
            counter += 1
        


    return -1   # not found

sum_array = [2,3,5,12,14,15,23,34,54]

print(linear_search(sum_array, 23), 'The result of invoking linear_search')


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here    


    low = 0
    high = len(arr) -1

    while low <= high:

        mid = (low + high) // 2 # gives us middle 

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1

    # first I will get the length of the array
    # then I will made a pointer called mid that takes the length of the array
    # and finds the mid point of it. I will have to round down however incase i run into an odd lengthed array
    # then I will have one for the beginning
    # I will then have one for the end

    # then I will have certain cases to work through (if statements)
    # I will make my statement that stops all my work, in other workds my success
    # i will make a statement that says if the middle index of the array is equal to the target we are searching
    # then return that 


    return -1  # not found
