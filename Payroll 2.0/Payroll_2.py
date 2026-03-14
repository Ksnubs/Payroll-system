#Second version of Payroll System

#Functions
def get_user_input_int(max_int):
    while True:
        try:
            entry = int(input("Enter an Index: "))
            if -1 < entry < max_int:
                return(entry)
            else:
                print("Please Enter a Valid Index.")
        except(ValueError):
            print("Please Enter a Value")
    
def title(title):
    title_length = len(title)
    space = 50 - title_length
    if space % 2 == 0:
        sideline = int(space / 2)
        print("-" * sideline, f" {title} ", "-" * sideline)
    else:
        sideline = int((space -1) /2)
        print("-" * sideline, f" {title} ", "-" * (sideline + 1))

#WELCOME TITLE
title("Welcome to Beluga HR system")

#Program loop
while True:
    print("\nPlease select the action you want to access.")
    print("0. Close the System.")

   
