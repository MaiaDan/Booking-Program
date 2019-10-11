
# This fibonaci solution requires less memory than recursion , memoization and iterative solutions.
# Using Dynamic Programming

def Fib(n) :
    if n <=1:
        return n
    previous , current = 0,1
    for i in range(n-1):
        new_current = previous + current
        previous , current = current , new_current
    return current

print(Fib(100))