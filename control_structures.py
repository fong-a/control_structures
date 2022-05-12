# This brief class will consider the various 'control structures' you should be familiar with
# These include:
#       1 Sequence
#       2 Binary Selection
#       3 Multiway Selection
#       4 Repetition (pre-test, post-test, counted)
#       5 Subroutines/Functions

# ⚠️ Tip - To quickly uncomment code, use the shortcut 'Ctrl + /'. Works to comment out and uncomment blocks of code quickly!

# 1 Sequence
# x = 1
# y = 2
# x = 3
# y = 4
# print(x + y)

# 2 Binary Selection
# if (4 + 5 == 10):
#     print("TRUE")
# else:
#     print("FALSE")

# 3 Multiway Selection
# trains_per_day = 9
# if trains_per_day == 8:
#     print("There are exactly 8 trains per day")
# elif trains_per_day > 6 and trains_per_day < 20:
#     print("There are more than 6 but less than 20 trains per day")
# elif trains_per_day <7:
#     print("There are less than 7 trains per day")
# else:
#     print("There are 20 or more trains per day")

# 4a Pre-test Repetition WHILE

# names = [] # creates empty list called names
# data_entry_complete = False
# while data_entry_complete == False:
#     name = input("Enter a name, or leave blank when done: ")
#     name = name.strip()
#     if (name == ""):
#         data_entry_complete = True
#     else:
#         names.append(name)
# print(names)

# 4b Post-test Repetition
# REPEAT UNTIL Doesn't exist in Python! 😊
# What is the alternative?

# 4c Counted Loops
# for i in range(100):
#   print("And my Axe! 🪓")

# 5 Subroutines/Functions - subroutines don't have return values, functions do
# def and_my(weapon):
#     print("Gimli shouts out...", " AND MY ....", weapon)

# and_my("🪓")

# def and_my(weapon):
#     return "Gimli shouts out...", " AND MY ....", weapon

# battle_cry = and_my("Double Barrel Shotgun")
# print(battle_cry)

# Task - ensure you have examples of each of the above loops in a file within your SDD folder
