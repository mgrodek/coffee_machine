numbers = []

while True:
    number = int(input())
    numbers.append(number)
    if sum(numbers) == 0:
        break

if numbers[0] == 0:
    print(numbers[0])
else:
    squares_sum = 0
    for i in numbers:
        squares_sum += i ** 2
    print(squares_sum)
