class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:

            while left < right and not self.alphaNum(s[left]):
                left += 1
            while right > left and not self.alphaNum(s[right]):
                right -= 1

            # print(f"left: {s[left]} | right: {s[right]}")
            
            # check that left and right are equal
            if s[left].lower() != s[right].lower():
                # print(f"left: {s[left]} | right: {s[right]} | {s[left].lower()} != {s[right].lower()}")
                return False
            left += 1
            right -= 1
        
        return True
    
    def alphaNum(self, c):
        return (
            (ord('A') <= ord(c) <= ord('Z')) or
            (ord('a') <= ord(c) <= ord('z')) or
            (ord('0') <= ord(c) <= ord('9'))
        )
    

s = "Was it a car or a cat I saw?"
print(Solution().isPalindrome(s))