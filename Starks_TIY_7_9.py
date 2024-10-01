sandwich_orders = ['BLT', 'pastrami', 'grilled cheese sandwich',
                   'pastrami', 'club sandwich', 'pastrami']
finished_sandwiches = []

print("We have ran out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Making your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)

print("\nThese sandwiches have been finished:")
for finished_sandwiches in finished_sandwiches:
    print(finished_sandwiches)