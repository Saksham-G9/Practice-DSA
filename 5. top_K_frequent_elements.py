nums = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
k = 2


def topKFrequent(nums: list[int], k: int) -> list[int]:
    from collections import Counter

    freq = Counter(nums)
    return [item for item, _ in freq.most_common(k)]


def topKFrequent_bucket(nums: list[int], k: int) -> list[int]:
    """Bucket sort approach: O(n) time, O(n) space.

    Build buckets where index = frequency, then collect from high->low.
    """
    from collections import Counter

    freq = Counter(nums)
    if k <= 0:
        return []

    maxf = max(freq.values())
    buckets = [[] for _ in range(maxf + 1)]

    for num, cnt in freq.items():
        buckets[cnt].append(num)

    res = []
    for f in range(len(buckets) - 1, 0, -1):
        for num in buckets[f]:
            res.append(num)
            if len(res) == k:
                return res

    return res


print(topKFrequent_bucket(nums, k))
