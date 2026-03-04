# [1,2,3,1]
# [5,6,7,8,9]


def brute_force(nums: list[int]):
    """
    T(C) = O(n^2)
    S(C) = O(1)
    """
    len_nums = len(nums)
    for i in range(len_nums):
        for j in range(i + 1, len_nums):
            if nums[i] == nums[j]:
                return True
    return False


def sorting_solution(nums: list[int]):
    """
    T(C) = O(nLogn)
    S(C) = O(1)
    """
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


def hashset_solution(nums: list[int]):
    """
    T(C) = O(n)
    S(C) = O(n)
    """
    seen = set()

    for el in nums:
        if el in seen:
            return True
        else:
            seen.add(el)
    return False


nums1 = [1, 2, 3, 1]
nums2 = [5, 6, 7, 8, 9]

print(brute_force(nums1))
print(brute_force(nums2))

print(sorting_solution(nums1))
print(sorting_solution(nums2))

print(hashset_solution(nums1))
print(hashset_solution(nums2))
