# Exersises
# 4.1 
def sumOfNumbers(l: list[int]) -> int:

    if len(l) == 0:
        return 0
    
    return l[0] + sumOfNumbers(l[1:])


# print("4.1: (Recursive) sumOfNumbers([1, 2, 3, 4, 5]): ", sumOfNumbers([1, 2, 3, 4, 5]))


# 4.2
def countOfItems(l: list[int]) -> int:

    if len(l) == 0:
        return 0
    
    return 1 + countOfItems(l[1:])


# print("\n4.2: (Recursive) countOfItems([1, 2, 3, 4, 5]): ", countOfItems([1, 2, 3, 4, 5]))


# 4.3
def maximumInList(l: list[int]) -> int:

    if len(l) == 1:
        return l[0]
    
    maxElement = l[0] if l[0] > l[1] else maximumInList(l[1:])
    # we can use the max() function as well
    return maxElement


# print("\n4.3: (Recursive) maximumInList([1, 2, 3, 4, 5]): ", maximumInList([1, 2, 3, 4, 5]))


# 4.4 Recursive binary search
def binarySearch(arr, target):
    if len(arr) == 1 and arr[0] != target:
        return None
    
    middle = len(arr) // 2
    focusedElement = arr[middle]

    if focusedElement == target:
        return middle
    elif focusedElement < target:                   # if the focused element is less than the target, search the right side
        return binarySearch(arr[middle:], target)
    else:                                           # if the focused element is greater than the target, search the left side
        return binarySearch(arr[:middle], target)
    

# print("\n4.4: (Recursive) binarySearch([1, 2, 3, 4, 5], 3): ", binarySearch([1, 2, 3, 4, 5], 3))
# print("4.4: (Recursive) binarySearch([1, 2, 3, 4, 5], 6): ", binarySearch([1, 2, 3, 4, 5], 6))


# Divide and Conquer approach
# Split plot of land into equally sized squares problem
def splitPlot(dimensions: list[int]) -> list[int]:

    smaller = min(dimensions[0], dimensions[1])
    bigger = max(dimensions[0], dimensions[1])

    if bigger % smaller == 0: # if the bigger is a multiple of the smaller, then the smaller dimension can be used as the x and y length to make squares in this current plot, which means we can fit that x and y size of square in the whole plot
        return [smaller, smaller]

    return splitPlot([bigger % smaller, smaller])


# print("\n(Recursive) splitPlot([10, 8]): ", splitPlot([10, 8]))
# print("(Recursive) splitPlot([1680, 640]): ", splitPlot([1680, 640]))


# Quick Sort
# Worst case time complexity: O(n^2)
# Average case time complexity: O(n log n)
def quickSort(l: list[int]) -> list[int]:
    if len(l) < 2:
        return l
    
    else:    
        pivotIndex = len(l) // 2
        pivot = l[pivotIndex]

        l.pop(pivotIndex) # I am removing the pivot from the list so it's not included in the recursion. Alternatively, we could set the pivot to the last or first element of the list. We could also set the pivot to a random element of the list

        left = [x for x in l if x <= pivot] # If we did an alternative, we could exclude the pivot from the left and right lists
        right = [x for x in l if x > pivot] # for example, if set the pivot to the first element of the list, right would = [x for x in l[1:] if x < pivot], so that the pivot would not be included

        return quickSort(left) + [pivot] + quickSort(right)

# testArray = [3, 9, 3, 8, 7, 6, 2, 5, 4, 3, 2, 1]
# print(f"\n(Recursive) quickSort({testArray}) --> {quickSort(testArray)}")


print("")