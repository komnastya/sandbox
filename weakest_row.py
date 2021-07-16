# My solution for https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/ using binary search (it isn't the best solution for this task)

# Example 1:

# Input: mat =
# [[1,1,0,0,0],
#  [1,1,1,1,0],
#  [1,0,0,0,0],
#  [1,1,0,0,0],
#  [1,1,1,1,1]],
# k = 3
# Output: [2,0,3]


def kWeakestRows(mat, k):
    def counter(row):
        lo = 0
        hi = len(row) - 1
        if row[hi] == 1:
            return len(row)
        elif row[0] == 0:
            return 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if row[mid] == 0 and row[mid - 1] == 1:
                return mid
            if row[mid] == 0:
                hi = mid - 1
                continue
            if row[mid] == 1:
                lo = mid + 1
                continue
            return mid

    result = sorted([[counter(mat[row]), row] for row in range(len(mat))])

    return [result[i][1] for i in range(k)]


print(
    kWeakestRows(
        [
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1],
        ],
        3,
    )
)
