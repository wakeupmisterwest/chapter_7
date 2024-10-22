fast_food_list = ["taco bell", "mcdonald's", "wendy's", "kfc", "burger king"]
fast_food = {}
max_input = 8
input_count = 0

while input_count < max_input:
    name = input("\nWhat is your name? ")

    if name not in fast_food:
        fast_food[name] = []

    while True:
        response = input("What is your favorite fast food place? ")

        if response.strip().lower() not in (place.lower() for place in
                                            fast_food_list):
            fast_food_list.append(response.strip())

        fast_food[name].append(response.strip())

        repeat = input(
            "Would you like to add another place? (yes)/(no): ").strip().lower()
        if repeat != 'yes':
            break

    input_count += 1

print("\n--- Results ---")
for name, places in fast_food.items():
    print(f"{name}'s favorite fast food places are {', '.join(places)}")