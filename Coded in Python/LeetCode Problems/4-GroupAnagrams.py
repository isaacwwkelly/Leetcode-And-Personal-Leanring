from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    # a dict where the serial number is the key, and the value is a list of strings that are anagrams of each other
    # the serial number is the 0s and 1s of a string where 1s are at the spots where the letters are in alphabetical order

    anagrams = defaultdict(list)
    for s in strs:
        serialNumber = [0] * 26
        for c in s:
            serialNumber[ord(c) - ord("a")] += 1
        anagrams[tuple(serialNumber)].append(s)

    return list(anagrams.values())


# Time: O(n * m) where n is the number of strings and m is the length of each string
# Space: O(n * m)


strings = ["act","pots","tops","cat","stop","hat"]
print(groupAnagrams(strings))

s2 = ["ddddddddddg","dgggggggggg"]
print(groupAnagrams(s2))