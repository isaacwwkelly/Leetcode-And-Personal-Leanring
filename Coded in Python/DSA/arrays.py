class QuickSort:
    def partition(self, arr, left, right):
        i = left
        j = right - 1
        pivot = arr[right]
        while i < j:
            while i < right and arr[i] < pivot:
                i += 1
            while j > left and arr[j] > pivot:
                j -= 1
            if i < j: # if the pointers have not crossed each other 
                arr[i], arr[j] = arr[j], arr[i] # swap the values at index i and j
        
        if arr[i] > pivot: # if the value at index i is greater than pivot
            arr[i], arr[right] = arr[right], arr[i] # swap the value at index i with the pivot value

        return i # return the index of the pivot
    
    def quicksort(self, arr, left, right):
        if left < right:
            pivot = self.partition(arr, left, right)
            self.quicksort(arr, left, pivot - 1)
            self.quicksort(arr, pivot + 1, right)
        return arr

    
# Quick Sort
# my_array = [22,11,88,66,55,77,33,44]
# print("\nQuick Sort\nUnsorted array:\t", my_array)
# sorter = QuickSort()
# sorter.quicksort(my_array, 0, len(my_array) - 1)
# print("Sorted array:\t", my_array)


class MergeSort:
    def mergeSort(self, array):
        
        if len(array) > 1:
            left_arr = array[:len(array)//2]
            right_arr = array[len(array)//2:]

            # recursive calls
            self.mergeSort(left_arr)
            self.mergeSort(right_arr)

            # merge the two sorted arrays
            i = 0 # left array index
            j = 0 # right array index
            k = 0 # merged array index
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    array[k] = left_arr[i]
                    i += 1
                else:
                    array[k] = right_arr[j]
                    j += 1
                k += 1
            while i < len(left_arr):
                array[k] = left_arr[i]
                i += 1
                k += 1
            while j < len(right_arr):
                array[k] = right_arr[j]
                j += 1
                k += 1

my_array = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
print("\n\nMerge Sort\nUnsorted array:\t", my_array)
sorter = MergeSort()
sorter.mergeSort(my_array)
print("Sorted array:\t", my_array)