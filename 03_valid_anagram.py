from collections import Counter


def isAnagram_counter_sol(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


def isAnagram_sort_sol(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


def isAnagram_bucket_sol(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    freq = [0] * 26

    for i in range(len(s)):
        freq[ord(s[i]) - ord("a")] += 1
        freq[ord(t[i]) - ord("a")] -= 1

    return all(x == 0 for x in freq)


s = "anagram"
t = "nagaram"

isAnagram_bucket_sol(s, t)
