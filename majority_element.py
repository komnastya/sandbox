from typing import List, Optional


# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
# Example 1:
# Input: nums = [3,2,3]
# Output: 3


def majority_element_for(nums: List) -> Optional[int]:
    if len(nums) == 0:
        return None
    major = 0
    major_counter = 0
    for major_element in nums:
        counter = 0
        for element in nums:
            if major_element == element:
                counter += 1
        if counter > major_counter:
            major_counter = counter
            major = major_element
    return major


def majority_element_while(nums: List) -> Optional[int]:
    if len(nums) == 0:
        return None
    major = 0
    major_counter = 0
    i = 0
    j = 0
    while i < len(nums):
        counter = 0
        j = 0
        while j < len(nums):
            if nums[i] == nums[j]:
                counter += 1
            j += 1
        if counter > major_counter:
            major_counter = counter
            major = nums[i]
        i += 1
    return major


def majority_element_count(nums: List) -> Optional[int]:
    for element in nums:
        counter = nums.count(element)
        if counter > len(nums) / 2:
            return element
    return None


def majority_element_dict(nums: List) -> Optional[int]:
    counters = {nums.count(element): element for element in nums}
    major = max(counters.keys())
    return counters.get(major)


# Boyer–Moore majority vote algorithm


def majority_element(nums: List) -> Optional[int]:
    counter = 0
    for x in nums:
        if counter == 0:
            majority_element = x
            counter = 1
        elif majority_element == x:
            counter += 1
        else:
            counter -= 1
    return majority_element
