class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if n is the beginning of a sequence
            if (n - 1) not in numSet:
                length = 0 # initialize the length of this set
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest) # keep the longest length
        return longest

        # Time: O(n)

sol = Solution()
nums = [100,4,200,1,3,2]
print(sol.longestConsecutive(nums))