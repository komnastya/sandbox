# Counts the number of negative numbers in the given matrix.
from typing import List


def count_negative_numbers(nums: List) -> int:
    count = 0
    width = len(nums[0])
    i = width
    for row in nums:
        while i > 0 and row[i - 1] < 0:
            i -= 1
        count += width - i
    return count


# each next row has MORE negative numbers than the previous one
# (or to say it more accurate NOT LESS)
# the right border of negative numbers is shrinking to the left
# optimize by skiping elemetns which you know for sure are negative
#  1  1  1  1 |  1  1
#  1  1  1  1 |  1 -1
#  1  1  1  1 | -1 -1
#  1  1  1 -1 | -1 -1 <-- we are on this row
#  1 -1 -1 -1 | -1 -1

def count_negative_numbers_2(nums: List) -> int:
    negatives = 0

    def counter(nums):
        length = len(nums)

        if length == 0:
            return 0
        if nums[0] < 0:
            return length
        if nums[length - 1] > 0:
            return 0
        lo = 0
        hi = length - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid + 1] < 0 and nums[mid] >= 0:
                return length - 1 - mid
            elif nums[mid] > 0:
                lo = mid + 1
            elif nums[mid] < 0:
                hi = mid - 1

    for num in nums:
        negatives += counter(num)

    return negatives
