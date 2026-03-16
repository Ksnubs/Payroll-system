#Second version of Payroll System
#Functions
#Gets user interger input that limits how big the int can be 
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

#Prints title in standard format of 50 units in length
def title(title):
    title_length = len(title)
    space = 50 - title_length
    if space % 2 == 0:
        sideline = int(space / 2)
        print("-" * sideline, f" {title} ", "-" * sideline)
    else:
        sideline = int((space -1) /2)
        print("-" * sideline, f" {title} ", "-" * (sideline + 1))

#Confrim user is done viewing the data
def exit():
    input("Press any key to continue: ")

#logic for the Manage system menu
def manage_staff():
    while True:
        title("Manage Staff")
        print("0. Main Menu.")
        print("1. View List of Employees.")
        print("2. Add an Employee.")
        print("3. Remove an Employee.")
    
        option = get_user_input_int(3)
        if option == 0:
            break
        elif option == 1:
            title("Employee List")
            for emp in employee_list:
                print(f"Name: {emp.name}")
                print(f"Base Salary: {emp.base_pay}")
                print(f"OT Worked: {emp.task}")
                print("-" * 30)
            exit()
        elif option == 2:
            title("Adding Employee")
            name = input("Enter New Employee's Name: ")
            base_salary = int(input("Enter New Employee's Base Salary: "))
            new_emp = Employee(name, base_salary, {})
            employee_list.append(new_emp)
            print(f"{name} has been added to the system.")
            exit()
        elif option == 3:
            title("Removing Employee")
            print("Enter the Employee's Index of the Employee you want to remove.")
            for index, name in enumerate(employee_list):
                print(f"{index}. {name.name}")
            num_of_emp = len(employee_list)
            index_remove = get_user_input_int(num_of_emp)
            name = employee_list[index_remove].name
            employee_list.pop(index_remove)
            print("-" * 30)
            print(f"\n{name} has been removed from the system.")

#Logic for the Manage Overtime Details Menu  
def manage_overtime_details():
    pass

#Employee Class for employees
class Employee:
    def __init__(self, name, base_pay, task):
        self.name = name
        self.base_pay = base_pay
        self.task = task

#List of employees working stored as objects
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
        manage_staff()

    if choice == 2:
        pass
