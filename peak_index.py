# Let's call an array arr a mountain if the following properties hold:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

# Example 1: arr = [0,1,0] -> 1
# Example 1: arr = [0,1,2,0] -> 2
# Example 1: arr = [0,1,2,3,5,7,11,6,4] -> 6
from typing import List


def peak_index(nums: List) -> int:
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid - 1] < nums[mid] < nums[mid + 1]:
            lo = mid + 1
        elif nums[mid - 1] > nums[mid] > nums[mid + 1]:
            hi = mid - 1
        elif nums[mid - 1] < nums[mid] > nums[mid + 1]:
            return mid
    raise ValueError
