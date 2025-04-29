def twoSum(nums: list[int], target: int) -> list[int]:
    pair = {}
    for n, i in enumerate(nums):
        remainder = target - i
        if remainder in pair:
            return[pair[remainder], n]
        pair[i] = n

    return []


    # Time: O(n)
    # Space: O(n)

nums_list = [3,4,5,6]
target_param = 7

print(twoSum(nums_list, target_param))