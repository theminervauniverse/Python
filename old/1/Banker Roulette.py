import random
test_seed = int(input("Create a Seed : "))
random.seed(test_seed)

all_names = input("Give Everybody Names,separated by commas :")
names = all_names.split(",")
# print(names)

# choice = random.choice(names)

# print(choice + " will pay the bill")
number_of_el = len(names)
random_number = random.randint(0, number_of_el - 1)
payed_by = names[random_number]

print(payed_by + " will pay the bill")