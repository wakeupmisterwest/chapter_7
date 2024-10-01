sandwich_orders = ['BLT', 'club sandwich', 'grilled cheese sandwich', 'egg '
                   'sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Making your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)

print("\nThese sandwiches have been finished:")
for finished_sandwiches in finished_sandwiches:
    print(finished_sandwiches)