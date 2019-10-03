# Uses python3
import sys
import math

def get_change(m):

    coins = [10, 5, 1]
    n = len(coins)
    counter = 0
    for i in range(0,n):
    	
    	if m > 0:
    		counter += int(math.floor(m /coins[i]))
    		m = m%coins[i] 
    return counter
    

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

# print(get_change(5))
