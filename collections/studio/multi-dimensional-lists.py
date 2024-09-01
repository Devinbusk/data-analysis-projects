food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
food = (food.split(","))
food.sort()
print(food)
equipment = (equipment.split(","))
equipment.sort()
pets = (pets.split(","))
pets.sort()
sleep_aids = (sleep_aids.split(","))
sleep_aids.sort()

# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.


cargo_hold = [food, equipment, pets, sleep_aids]
print(cargo_hold)
# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.
# user_input = int(input("Enter a number from 0 to 3:")) 

# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.
# if user_input <= 3: print(cargo_hold[user_input]) 
# else: print("Error number not within range, select a number from 0 to 3")


# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”
user_input = int(input("Enter a cabinet index number from 0 to 3:")) 
if cargo_hold[user_input] in cargo_hold:
     second_user_input = int(input("Now select an item index number from 0 to 3:"))
     if cargo_hold[user_input] in cargo_hold: 
         cargo_hold_items = "Cabinet {0} DOES contain {1}."
         print(cargo_hold_items.format(cargo_hold[user_input], cargo_hold[user_input][second_user_input] ))
     else: 
         cargo_hold_items = "Cabinet {0} DOES NOT contain {1}."
         print(cargo_hold_items.format(cargo_hold[user_input], cargo_hold[user_input][second_user_input] ))

          
else: print("Select a different number from 0 to 3")






