age = input("How old are you? ")
age = int(age)

if age < 3:
    price = 0
elif age < 13:
    price = 10
else:
    price = 15

print(f"\nYour ticket costs {price}$.")