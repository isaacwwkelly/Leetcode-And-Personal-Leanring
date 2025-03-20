def twoSum(numbers: list[int], target: int) -> list[int]:

    left, right = 0, len(numbers) - 1

    while left < right: # numbers[left] + numbers[right] != target
        currentSum = numbers[left] + numbers[right] 

        if currentSum < target:
            left += 1
        elif currentSum > target:
            right -= 1
        else:
            return [left + 1, right + 1]
        
numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))