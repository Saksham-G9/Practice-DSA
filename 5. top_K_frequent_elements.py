nums = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
k = 2


def topKFrequent(nums: list[int], k: int) -> list[int]:
    from collections import Counter

    freq = Counter(nums)
    return [item for item, _ in freq.most_common(k)]


print(topKFrequent(nums, k))
