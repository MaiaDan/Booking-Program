#python 3
import sys
def fibonacci (n):
	a = []
	a.insert(0,0)
	a.insert(1,1)
	for i in range (2,n+1):
		a.append(a[i-1] + a[i-2])

	#return a[-1] 
	return a[n] 

print(fibonacci(7))

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n = int(input)
#     print(fibonacci(n))

