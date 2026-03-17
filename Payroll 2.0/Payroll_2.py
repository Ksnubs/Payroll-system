#Second version of Payroll System
#Functions
#Get user's int inputs with limits to the range of the allowed inputs for navigation of the system
def navigation(min, max):
    while True:
        try:
            entry = int(input("\nEnter an Index: "))
            if min > entry or entry > max:
                print("Please Enter a value within the Range!")
            else: 
                break
        except (ValueError):
            print("Please enter a Int Value!")
    return(entry)

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

#Takes users float inputs 
def input_float(question):
    while True:
        try:
            num = float(input(question))
            break
        except (ValueError):
            print("Please enter a value!")
    return(num)
            
#logic for the Manage system menu
def manage_staff():
    while True:
        title("Manage Staff")
        print("0. Main Menu.")
        print("1. View List of Employees.")
        print("2. Add an Employee.")
        print("3. Remove an Employee.")
    
        option = navigation(0, 3)
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
            base_salary = input_float("Enter New Employee's base salary: ")
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
            index_remove = navigation(0, num_of_emp)
            name = employee_list[index_remove].name
            employee_list.pop(index_remove)
            print("-" * 30)
            print(f"\n{name} has been removed from the system.")
            exit()

#Logic for the Manage Overtime Details Menu 
# Add overtime task
# remove overtime task
# edit overtime pay 
def manage_overtime_details():
    while True:
        title("Manage Overtime Details")
        print("0. Main Menu.")
        print("1. Add Overtime Task.")
        print("2. Remove Overtime Task.")
        print("3. Edit Overtime Rates.")

        option = navigation(0, 3)
        
        if option == 0:
            print("Returning to Main Menu....")
            exit()
            break
        elif option == 1:
            title("Add Overtime Task")
            task_name = input("Enter name of new task: ")
            task_rate = input_float("Enter rate of new task: ")
            overtime_rates[task_name] = task_rate
            print(f"{task_name} has been successfully added to the system.")
            exit()

        elif option == 2:
            title("Remove Overtime Task")
            overtime_task = list(overtime_rates.keys())
            num_overtime_task = len(overtime_task)
            if num_overtime_task == 0:
                print("There are no OVERTIME TASKS.")
            else:
                for index, task in enumerate(overtime_task):
                    print(f"{index}. {task}")
                choice = navigation(0, num_overtime_task - 1)
                task_removed = overtime_task[choice]
                overtime_rates.pop(task_removed)
                print(f"{task_removed} has been removed.")
                exit()
        elif option == 3:
            title("Edit Overtime Rates.")
            overtime_task = overtime_rates.keys()
            num_overtime_task = len(overtime_task)
            for index, task in enumerate(overtime_task):
                print(f"{index}. {task}")
            choice = navigation(0,num_overtime_task)
             
#Employee Class for employees
class Employee:
    def __init__(self, name, base_pay, task):
        self.name = name
        self.base_pay = base_pay
        self.task = task

#List of employees working stored as objects
employee_list = []
overtime_rates = {}

#WELCOME TITLE
title("Welcome to Beluga-MAMA HR system")

#Program loop
while True:
    title("MAIN MENU")
    print("\nPlease select the action you want to access.")
    print("0. Close the System.")
    print("1. Manage Staff.")
    print("2. Manage Overtime Details.")
    print("3. Edit Overtime Worked.")
#Input for users choice
    choice = navigation(0, 3)

    if choice == 0:
        title("Closing the System...")
        exit()
        break

    elif choice == 1:
        manage_staff()

    elif choice == 2:
        manage_overtime_details()
    
    elif choice == 3:
        pass
