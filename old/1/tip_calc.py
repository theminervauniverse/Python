print("Welcome to the Tip Calculator")
bill = input("What Was the total Bill? $")
percentage = input("what percentage tip would you like to give? 10,12,15? ")
split = input("how many people to split the bill?")

bill_int = int(bill)
perc_int = int(percentage)
split_int = int(split)

tip = bill_int*(perc_int/100)
split_result = (bill_int + tip)/split_int

round = round(split_result,2)

print(f"each person should pay : ${round}")

