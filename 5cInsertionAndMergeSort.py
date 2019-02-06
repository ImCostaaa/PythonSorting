import sys
def mergeandInsertSort(array, k):
    #if current array being sorted is bigger tha k value start merge sort
    if len(array) > k:
        #find the middle of the array by dividing length by 2 as
        middle = len(array) // 2  # Finding the mid of the array
        Leftsect = array[:middle]  # Dividing the array elements
        Rightsect = array[middle:]  # into 2 halves based on all leftsection of mid and rightsection of mid
        mergeandInsertSort(Leftsect,k)
        mergeandInsertSort(Rightsect,k)
        #recursively split array until  size k, do the insertion sort on the most leftsect then its right sec, then that as a whole left sec recursively
        #upward until the entire array has been sorted through insertion sort of arrays size k then mergesort of the remaining
        #set counters a signi
        a = b = c = 0

        #compare the data in temp arrays, compare first elem of both arrays and use a,b counters to check current comparable elem of the two halves
        while a < len(Leftsect) and b < len(Rightsect):
            #put smaller number into param array location
            if Leftsect[a] < Rightsect[b]:
                array[c] = Leftsect[a]
                a = a + 1
            else:
                array[c] = Rightsect[b]
                b = b + 1
            #increment c counter which represents current elem of both halves of this recursive call of the array
            c = c + 1
        #grab any left over values to compare since we may get through a full half of one aarray and only part of other
        while a < len(Leftsect):
            array[c] = Leftsect[a]
            a += 1
            c += 1
        #same as above but for case with other half
        while b < len(Rightsect):
            array[c] = Rightsect[b]
            b += 1
            c += 1
    else:
        #do insertion sort on given array of size k or less
        # go through index 1 to end of array
        for i in range(1, len(array)):
            # grab the elem to check (1.....size)
            elemtocheck = array[i]
            # let j be i-1 to get the elem prior
            j = i - 1
            # check if j is greater than 0 and the current elem to enter is less than the one prior move all neccassary elems one over starting with end elem
            # working downwards to make room for the smallest elem
            while j >= 0 and elemtocheck < array[j]:
                array[j + 1] = array[j]
                j = j - 1
            # then once all are moved one over insert smaller elem into the open spot
            array[j + 1] = elemtocheck
#fill the array reversely with this function by setting i = 1 and appending size (n) - i to fill every element reversly.
def fillArrayReverse(arr,n):
    i = 1
    while(i <= n):
        arr.append(n-i)
        i = i+1
def printarray(arr):
    count = 0
    while(count<20):
        print(arr[count])
        count += 1

user_number = input ("Enter number of elements: ")
size = int(user_number)
arr = []
fillArrayReverse(arr, size)
print("Before Sort: ")
printarray(arr)
k = 8
mergeandInsertSort(arr, k)
print("After Sort: ")
printarray(arr)