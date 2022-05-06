print("leap year")
year = int(input("which year do you want to check?\n"))

if year % 4 == 0 :
    print("This is a Leap Year")
elif year % 100 == 0:
    print("this is not a leap year")
elif year % 400 == 0:
    print("this is a leap year")
else :
    print("this is not a leap year")