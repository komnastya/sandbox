# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
# Example 1:
# Input: nums = [3,2,3]
# Output: 3


def majority_element_for(nums):
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


def majority_element_while(nums):
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
