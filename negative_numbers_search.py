# Counts the number of negative numbers in the given matrix.

def count_negative_numbers(nums):
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
