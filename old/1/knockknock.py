print("welcome to knock knock!\n")
print('''__________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
ejm        |__________|
''')
start = input("You are in you room suddenly you hear a scream of a girl and then someone knocks on the door ,are you gonna open it ? or Yes or No .").lower()

if start == "yes" :
    print("there was a girl lying against your door ,blood all over the face.")
    second = input("you tried to help her get her inside yur room while you were treating her wounds,again there were more knocks on the door will you open it this time?, Yes or No . ").lower()
    if second == "no":
        print("You made the right choice by waiting ,then the girl woke up n said there's a killer roaming around killing people whoever open the door on him knocking ,")
        jump = input("She said we must get out of here now ,now you have three choices \n First ,Go out through your door \n Second ,Jump Through Ypur Window \n Third ,Wait in your room for help\n").lower()
        if jump == "second":
            print("Congrats You Beat your Death And Saved A life!")
        else :
            print("You Opened the Door someone stab a Knife in your Belly ,\n GAME OVER")
       
    else :
        print("You die")
    
else :
    print("you Waited this time but after some time again there was a knock on door n this time you opened it n you die \n GAME OVER")
