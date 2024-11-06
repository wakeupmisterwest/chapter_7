import csv

# Pull in the CSV file
filename = 'Chapter_7Challenge.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Loop through the csv file and create two lists
    names = []
    candy_type_1 = []
    candy_type_2 = []
    candy_price_1 = []
    candy_price_2 = []
    new_candy = []
    new_price = []
    removed_candy = []
    student_info = {}

    for row in reader:
        name = row[1]
        candy_1 = row[2]
        candy_2 = row[4]
        price_1 = float(row[3])
        price_2 = float(row[5])
        names.append(name)
        candy_type_1.append(candy_1)
        candy_type_2.append(candy_2)
        candy_price_1.append(price_1)
        candy_price_2.append(price_2)
        for i in range(len(names)):
            student_info.update({names[i]: {candy_type_1[i].strip().lower(), candy_price_1[i],
                                            candy_type_2[i].strip().lower(),
                                            candy_price_2[i]}})
        # add the code here that will append each variable above into the correct list.

    # Print each list
name_input = input("What is your name? ").strip().lower()

for name, info in student_info.items():
    if name.strip().lower() == name_input:
      while True:
        response = input(
            "\nDo you want to add or remove a new candy? (add)/(remove) ").strip().lower()
        if response == 'add':
            new_candy = input(
                "What candy do you want to add? ").strip().lower()
            new_price = input("How much does it cost? ")
            student_info[name].add(new_candy)
            student_info[name].add(new_price)
            print(info)
        if response == 'remove':
            removed_candy = input("What candy do you want to remove? ").strip().lower()
            removed_price = input("How much did it cost? ")
            student_info[name].remove(removed_candy)
            print(info)
        repeat = input(
            "\nDo you want to repeat? (yes)/(no) ")
        if repeat != 'yes':
            print(student_info)
            break









