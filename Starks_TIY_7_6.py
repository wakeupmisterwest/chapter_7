#while loop and break
prompt = "How old are you?"
prompt += "\n(Enter 'quit' when you are done.) "

while True:
    age = input(prompt)

    if age == 'quit':
        break
    age = int(age)

    if age < 3:
            cost = 0
    elif age < 13:
        cost = 10
    else:
        cost = 15
    print(f"\nYour ticket costs {cost}$.")

