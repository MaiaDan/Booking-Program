# determine the minimum number of miles Marc must walk to maintain his weight. Note that he can eat the cupcakes in any order.


import sys
def marcsCakewalk(calorie):
    value =0
    calorie.sort(reverse=True) # sort the calorie cupcake in decnding order to get the bi number first
    for i in range(len(calorie)):
        value += (2**i )* calorie[i]   # multiply the biggest number in calorie with least one to get the smallest value and so on

    return value

n = int(input())

calorie = list(map(int, input().strip().split()))
result = marcsCakewalk(calorie)

print(result)
