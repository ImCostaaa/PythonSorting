import sys
#array to fill and size of array are given as params
def fillArrayReverse(arr,n):
    # fill array by setting i to one and appending n which is size of array -1 to fill every spot from 0 - n-1 in reverse order
    i = 1
    while(i <= n):
        #while i less than or = size of array append n-i, when i=1 fills last spot of array, when i = n it fills first spot 0.
        arr.append(n-i)
        i = i+1
#simple print function to print first 20 elems of array
def printarray(arr):
    count = 0
    while(count < 20):
        print(arr[count])
        count += 1
def insertionSort(array, size):
    # go through index 1 to end of array
    for i in range(1, len(array)):
        #grab the elem to check (1.....size)
        elemtocheck = array[i]
        #let j be i-1 to get the elem prior
        j = i - 1
        #check if j is greater than 0 and the current elem to enter is less than the one prior move all neccassary elems one over starting with end elem
        # working downwards to make room for the smallest elem
        while j >= 0 and elemtocheck < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        # then once all are moved one over insert smaller elem into the open spot
        array[j + 1] = elemtocheck
#code to be ran to sort array once its filled. pseudo main function.
size = int(input ("Enter number of elements : "))
size = size
array = []
fillArrayReverse(array, size)
print("Before Sort: ")
printarray(array)
insertionSort(array, size)
print("After Sort: ")
printarray(array)
print(len(array))