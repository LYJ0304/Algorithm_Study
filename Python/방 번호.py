N = list(map(int, input()))
numbers = [0] * 10 


for num in N:
    numbers[num] += 1


numbers[6] = (numbers[6] + numbers[9] + 1) // 2
numbers[9] = 0


result = max(numbers)
print(result)
