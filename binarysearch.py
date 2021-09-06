# Returns index of elem in nums, or -1 if not found.
from typing import List


def binary_search(nums: List[int], elem: int) -> int:
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        x = nums[mid]
        if elem < x:
            hi = mid - 1
            continue
        if elem > x:
            lo = mid + 1
            continue
        return mid
    return -1
