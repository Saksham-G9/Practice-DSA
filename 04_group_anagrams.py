from collections import defaultdict

"""
Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    freq = [0] * 26

    for i in range(len(s)):
        freq[ord(s[i]) - ord("a")] += 1
        freq[ord(t[i]) - ord("a")] -= 1

    return all(x == 0 for x in freq)


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    res = []

    while len(strs):
        curr_res = []
        curr_res.append(strs.pop(0))
        j = 0
        while j < len(strs):
            if isAnagram(curr_res[0], strs[j]):
                curr_res.append(strs[j])
                strs.remove(strs[j])
            else:
                j += 1
        res.append(curr_res)

    return res


class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)

        for word in strs:
            freq = [0] * 26

            for c in word:
                freq[ord(c) - ord('a')] += 1

            groups[tuple(freq)].append(word)

        return list(groups.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
