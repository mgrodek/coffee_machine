minimum = float('inf')
number = input()

while number != ".":
    minimum = min(minimum, float(number))
    number = input()

print(minimum)