# Selection Sort

def findSmallestElement(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    copiedArr = list(arr)
    
    for i in range(len(copiedArr)):
        smallestElement = findSmallestElement(copiedArr)
        newArr.append(copiedArr.pop(smallestElement))
    
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))