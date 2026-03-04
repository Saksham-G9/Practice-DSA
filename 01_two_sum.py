def brute_force(nums: list[int], target: int):
    """
    Nested loop to check if target exists
    T(C) -> O(n^2)
    S(C) -> O(1)
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return nums[i], nums[j]

    return -1, -1


# nums = [3,2,4], target = 6
def optimized_approach1(nums: list[int], target: int):
    nums.sort()

    i, j = 0, len(nums) - 1

    while i < j:
        if nums[i] + nums[j] == target:
            return i, j
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1


def optimized_approach2(nums: list[int], target: int):
    seen = {}

    for idx, el in enumerate(nums):
        complement = target - el

        if complement in seen:
            return seen[complement], idx

        seen[el] = idx

    return -1, -1

print(optimized_approach2([-3, 4, 3, 90], 0))
