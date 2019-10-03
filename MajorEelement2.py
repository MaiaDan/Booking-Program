# Uses python3
from collections import Counter

def major_element(arr):
    arr.sort()
    Dict = Counter(arr)
    # print(Dict)
    size = len(arr)
    for (key, val) in Dict.items():
        if (val > (size / 2)):
            # print(key)
            return 1
    return 0


size = int(input())
arr = list(map(int, input().split()))
print(major_element(arr))

# print(major_element([3,3,4,2,4,4,2,4,4]))
