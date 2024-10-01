group = input("How many people are in your dinner group? ")
group = int(group)


if group > 8:
    print("\nYou'll have to wait for a table.")
else:
    print("\nA table is available.")