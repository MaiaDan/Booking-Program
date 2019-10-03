# Uses python3
import sys


def binary_search(a,low,high,key):
    if high < low:
        return -1

    mid = int(low + (high - low) / 2)

    if key == a[mid] :
        return mid
    elif key < a[mid]:
        return binary_search(a,low,mid-1,key)
    else:
        return binary_search(a,mid+1,high,key)

a = list(map(int, input().split()))
a_size = a.pop(0)
b = list(map(int, input().split()))
b_size = b.pop(0)
c= []
for key in b:
    c.append(binary_search(a, 0, a_size - 1, key))
print(*c)

