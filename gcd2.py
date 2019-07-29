#python3
import sys
def gcd(a,b):

	
	# if b == 0 :
	# 	return a

	# else :
	# 	return gcd (b,a % b)

	
	#___________________

	while b:
		a,b = b, a % b

	return a 


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))

# print(gcd(28851538 ,1183019))