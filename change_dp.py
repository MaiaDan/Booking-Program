# Uses python3
import sys
import math


def get_change(money, coins):
    infiniteValue = money + 1
    minNum = [infiniteValue] * (money + 1)  # fill in the stack with  large amount temporally
    minNum.insert(0, 0)
    # get min number of coins for each cell (sub problem) and use it for the next cell until we reach the least cell which is
    # the wanted amount of money
    for m in range(money + 1):
        for i in range(len(coins)):  # checking all coins
            if m >= coins[i]:
                numCoins = minNum[m - coins[i]] + 1  # we subtracte the number from the coin and add 1 bcz using one coin from coins
                if numCoins < minNum[m]:  # if it is less than the current amount the replace it, we choose the min value
                    minNum[m] = numCoins

    return minNum[money]


# if __name__ == '__main__':
#     m = int(sys.stdin.read())
#     print(get_change(m))


# coins = list(map(int, input().split()))
m = int(input())
coins = [1, 3, 4]
print(get_change(m,coins))
# print(get_change(34, [1, 3, 4]))
