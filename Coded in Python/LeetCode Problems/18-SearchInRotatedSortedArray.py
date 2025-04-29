def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums)-1
    while l <= r:
        guess_i = (l + r) // 2
        guess = nums[guess_i]

        if guess == target:
            return guess_i
        
        if nums[l] <= nums[guess_i]:
            # then we know we're in the "left" portion of the array, left meaning we're to the left of the highest number that was rotated
            if target > nums[guess_i] or target < nums[l]:
                l = guess_i + 1
            else:
                r = guess_i - 1
        else:
            # if we're in the "right" portion of the array, right meaning we're to the right of the highest number that was rotated
            if target < nums[guess_i] or target > nums[r]:
                r = guess_i - 1
            else:
                l = guess_i + 1
    return -1



nums = [3,4,5,6,1,2]
target = 1

print(search(nums, target))


nums = [1]
target = 1

print(search(nums, target))