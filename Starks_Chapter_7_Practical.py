fast_food_list = ["taco bell", "mcdonald's", "wendy's", "kfc", "burger king"]
fast_food = {}
max_input = 8
input_count = 0

while input_count < max_input:
    name = input("\nWhat is your name? ")

    if name not in fast_food_list:
        fast_food[name] = []

    while True:
        response = input("What is your favorite fast food place? ")
        fast_food[name] = response.append(fast_food)

        if response.strip().lower() not in (fast_food.lower() for fast_food in
                                            fast_food_list):
            fast_food_list.append(response)

        repeat = input(
            "Would you like to add another place? (yes)/(no): ").strip().lower()
        if repeat != 'yes':
            break

input_count += 1

print("\n--- Results ---")
for name, fast_food in fast_food.items():
    print(f"{name}'s favorite fast food places are {fast_food}")
