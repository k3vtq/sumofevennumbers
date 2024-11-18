my_sum = 0
for number in range(1, 101):
    if number % 2 == 0:
        my_sum += number

print(f"Sum of even number from 1 to 100 is: {my_sum}")

# Extra Credit.  Put down below

for number in range(1, 301):
    if number % 3 == 0 and number % 7 == 0:
        print(f"Charlie Brown")
    elif number % 3 == 0:
        print(f"Brown")
    elif number % 7 == 0:
        print(f"Charlie")
    else: print(number)