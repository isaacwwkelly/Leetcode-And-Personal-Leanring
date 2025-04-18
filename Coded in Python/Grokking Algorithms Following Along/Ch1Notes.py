

# Binary Search

# Time complexity: O(log n)

def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        guess = arr[middle]

        if guess == target:
            return middle
        elif guess < target:
            left = middle + 1
        else:
            right = middle - 1
    
    return None

my_list = [1, 3, 5, 7, 9]
print(binarySearch(my_list, 3))
print(binarySearch(my_list, -1))

# for a list with n elements, the time complexity is O(log n)

# Excerises
# 1.1 For a list with 128 elements, the time complexity is O(log 128). log 128 = 7 because 128 = 2^7. It would take 7 steps to find the target element
# 1.2 For a list with 256 elements, the time complexity is O(log 256). log 256 = 8 because 256 = 2^8. It would take 8 steps to find the target element
# 1.3 Given a name, finding the name in a phone book will take O(log n) time, where n is the number of names in the phone book
# 1.4 Given a phone number, finding the associated name in the phone book will take O(n) time, where n is the number of names in the phone book, because the phone book is sorted by the names in alphabetical order
# 1.5 To read the numbers of every person in the phone book, it will take O(n) time, where n is the number of names in the phone book
# 1.6 To read the names of every person's name that starts with "A", it will take O(n/26) => which simplifies to O(n), where n is the number of names in the phone book. This is because #1, we can't guarantee that every person's name doesn't start with "A", and #2, constants are ignored in big O notation
