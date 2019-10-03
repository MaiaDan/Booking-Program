
def candies(n,arr):

    candies = [1] * (len(arr))


    # iterate from left to right from 1 to end the end of the array
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            candies[i] = candies[i - 1] + 1
    # iterate from right to left from n-2 to the begging  of the array
    for j in range(n-2, -1, -1):
        if arr[j] > arr[j + 1] and candies[j] < candies[j + 1] + 1:  # comparing candies also so that each child has the max number
            candies[j] = candies[j + 1] + 1

    total_candies = sum(candies)
    return  total_candies







n = int(input())
arr = []

for i in range(n):
    student_rate = int(input())
    arr.append(student_rate)

print(candies(n, arr))

