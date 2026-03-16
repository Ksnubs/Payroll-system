#Second version of Payroll System
#Functions
def get_user_input_int(max_int):
    while True:
        try:
            entry = int(input("Enter an Index: "))
            if -1 < entry <= max_int:
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

def exit():
    input("Press any key to continue: ")
#Classes
class Employee:
    def __init__(self, name, base_pay, task):
        self.name = name
        self.base_pay = base_pay
        self.task = task

employee_list = []
    

#WELCOME TITLE
title("Welcome to Beluga HR system")

#Program loop
while True:
    print("\nPlease select the action you want to access.")
    print("0. Close the System.")
    print("1. Manage Staff.")
    print("2. Manage Overtime Details.")
    print("3. Edit Overtime Worked.")
#Input for users choice
    choice = get_user_input_int(3)

    if choice == 0:
        title("Closing the System...")
        exit()
        break

    if choice == 1:
        title("Manage Staff")
        print("1. Add an Employee.")
        print("2. Remove an Employee.")
        print("3. View list of Employees")
        
        option = get_user_input_int(3)
        if option == 1:
            title("Add an Employee")
            name = input("New Employee Name: ")
            base_pay = int(input("New Employee Base Pay: "))
            new_emp = Employee(name, base_pay, {})
            employee_list.append(new_emp)
            print(f"\n{name} has been added to the system")
            exit()
        
        elif option == 3:
            for emp in employee_list:
                title("Employee List")
                print(f"Name: {emp.name}")
                print(f"Base Salary: {emp.base_pay}")
                     
        