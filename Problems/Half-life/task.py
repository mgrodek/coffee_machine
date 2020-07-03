initial_quantity = int(input())
final_quantity = int(input())

days = 0
while final_quantity <= initial_quantity:
    days += 12
    initial_quantity = initial_quantity / 2

print(days)