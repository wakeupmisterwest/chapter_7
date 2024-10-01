#active flag
prompt = "\nEnter the toppings you want on your pizza:"
prompt += "\n(Enter 'quit' when you are finished.) "

active = True
while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print(f"Adding {topping}.")