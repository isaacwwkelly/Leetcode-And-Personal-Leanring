def characterReplacement(s: str, k: int) -> int:
    count = {}
    res = 0

    l = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)

        while (r - l + 1) - max(count.values()) > k:
            # our window is too large. move the left pointer forward and decrement the dict
            count[s[l]] -= 1
            l += 1
        
        res = max(res, r-l+1)

    return res



s = "XYYX"
k = 2

# print(characterReplacement(s, k))


s = "AABABBA"
k = 1

print(characterReplacement(s, k))