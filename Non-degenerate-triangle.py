# Description #

# Given an array of stick lengths, use 3 of them to construct a non-degenerate triange with the maximum possible perimeter.
# Print the lengths of its sides as 3 space-separated integers in non-decreasing order.

def maximumPerimeterTriangle(sticks):
    n = len(sticks)
    if n < 3:
        return -1

    sticks.sort(reverse=True)
    alist = []


    for i in range(len(sticks) -2):
        if sticks[i] + sticks[ i+1] > sticks[i +2] and sticks[i+1] + sticks[i+2] > sticks[i] and sticks[i+2] + sticks[i] > sticks[i+1]:
            alist.append(sticks[i])
            alist.append(sticks[i+1])
            alist.append(sticks[i+2])
            alist.sort()

            return " ".join(map(str, alist))
    return -1

sticks_size = int(input())

sticks = list(map(int,input().strip().split()))

print(maximumPerimeterTriangle(sticks))