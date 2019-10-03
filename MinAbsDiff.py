
# -----  Description ----- #

# The function should return an integer that represents the minimum absolute difference between any pair of elements.
# minimumAbsoluteDifference has the following parameter(s):
# n: an integer that represents the length of arr
# arr: an array of integers


def minimumAbsoluteDifference(arr):
    arr.sort()
    n = len(arr)
    min = arr[-1] - arr[0]
    for i in range(1,n):
        if arr[i] - arr[i-1] < min:
            min = arr[i] - arr[i-1]
    return min

