class Solution:
    def findMin(self, nums: list[int]) -> int:
        res = nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            # if array[l] to array[r] is sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            # if the array l to r is not sorted
            m = (l + r) // 2
            res = min(res, nums[m])

            # search to the left or right?
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        return res
    


sol = Solution()
nums = [3,4,5,1,2]
print(sol.findMin(nums))

nums = [4,5,6,7,8,9,10,0,1,2]
print(sol.findMin(nums))