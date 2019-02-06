import sys
def mergeSort(array):
    if len(array) > 1:
        # find the middle of the array by dividing length by 2 as
        middle = len(array) // 2  # Finding the mid of the array
        Leftsect = array[:middle]  # Dividing the array elements
        Rightsect = array[middle:]  # into 2 halves based on all leftsection of mid and rightsection of mid
        mergeSort(Leftsect)
        mergeSort(Rightsect)
        # recursively split array until  size k, do the insertion sort on the most leftsect then its right sec, then that as a whole left sec recursively
        # upward until the entire array has been sorted through insertion sort of arrays size k then mergesort of the remaining
        # set counters a signi
        a = b = c = 0

        # compare the data in temp arrays, compare first elem of both arrays and use a,b counters to check current comparable elem of the two halves
        while a < len(Leftsect) and b < len(Rightsect):
            # put smaller number into param array location
            if Leftsect[a] < Rightsect[b]:
                array[c] = Leftsect[a]
                a = a + 1
            else:
                array[c] = Rightsect[b]
                b = b + 1
            # increment c counter which represents current elem of both halves of this recursive call of the array
            c = c + 1
        # grab any left over values to compare since we may get through a full half of one aarray and only part of other
        while a < len(Leftsect):
            array[c] = Leftsect[a]
            a += 1
            c += 1
        # same as above but for case with other half
        while b < len(Rightsect):
            array[c] = Rightsect[b]
            b += 1
#fill the array reversely with this function by setting i = 1 and appending size (n) - i to fill every element reversly.
def fillArrayReverse(arr,n):
    i = 1
    while(i <= n):
        arr.append(n-i)
        i = i+1
def printarray(arr):
    count = 0
    for i in arr:
        if count < 20:
            print(i)
        count += 1

size = 2000
arr = []
fillArrayReverse(arr, size)
print("Before Sort: ")
printarray(arr)
mergeSort(arr)
print("After Sort: ")
printarray(arr)