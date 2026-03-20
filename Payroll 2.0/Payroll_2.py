#Second version of Payroll System
#List of employees working stored as objects
employee_list = []
overtime_rates = {}

#Get user's int inputs with limits to the range of the allowed inputs for navigation of the system
def get_menu_choice(min, max):
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
def pause_screen():
    input("Press any key to continue: ")

#Takes users float inputs 
def get_input_float(question):
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
    
        option = get_menu_choice(0, 3)
        if option == 0:
            break
        elif option == 1:
            print_employee_list()
        elif option == 2:
            add_employees()
        elif option == 3:
            remove_employee()

#prints the particulars of all employees
def print_employee_list():
    title("\nList of Employees")
    for item in employee_list:
        print(f"Name: {item.name.title()}")
        print(f"Base Salary: {item.base_pay}")
        print(f"OT Task completed: {item.task}")
        print("-" * 30)
    pause_screen()

#adds employee to the system
def add_employees():
    title("Add Employees")
    name = input("Enter New Employee's Name: ")
    base_pay = input("Enter New Employee's base salary: ")
    new_employee = Employee(name.lower(), base_pay, {})
    employee_list.append(new_employee)
    print(f"{name.title()} has been added to the system.")
    pause_screen()

#remove employee from the system
def remove_employee():
    if not employee_list:
        print("\nThere are no emplyees!")
        pause_screen()
    else:
        title("Remove Employee")
        for index, emp_name in enumerate(employee_list):
            emp_name = emp_name.name.title()
            print(f"{index + 1}. {emp_name}")
        employee_num = len(employee_list)
        choice = get_menu_choice(0, employee_num)
        index_employee_removed = int(choice - 1)
        if choice == 0:
            pass
        else:
            emp_name = employee_list[index_employee_removed].name
            employee_list.pop(index_employee_removed)
            print(f"{emp_name} has been removed from the system.")
            pause_screen()


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

        option = get_menu_choice(0, 3)
        
        if option == 0:
            break
        elif option == 1:
            title("Add Overtime Task")
            task_name = input("Enter name of new task: ")
            task_rate = get_input_float("Enter rate of new task: ")
            overtime_rates[task_name] = task_rate
            print(f"{task_name} has been successfully added to the system!")
            pause_screen()

        elif option == 2:
            title("Remove Overtime Task")
            overtime_task = list(overtime_rates.keys())
            num_overtime_task = len(overtime_task)
            if num_overtime_task == 0:
                print("There are no OVERTIME TASKS.")
            else:
                for index, task in enumerate(overtime_task):
                    print(f"{index}. {task}")
                choice = get_menu_choice(0, num_overtime_task - 1)
                task_removed = overtime_task[choice]
                overtime_rates.pop(task_removed)
                print(f"{task_removed} has been removed.")
                pause_screen()
        elif option == 3:
            title("Edit Overtime Rates.")
            overtime_task = list(overtime_rates.keys())
            num_overtime_task = len(overtime_task)
            for index, task in enumerate(overtime_task):
                print(f"{index}. {task}")
            choice = get_menu_choice(0,num_overtime_task)
            choice_name = overtime_task[choice]
            new_rate = float(input(f"Enter new rate for {choice_name}: "))
            overtime_rates[choice_name] = new_rate
            print(f"{choice_name} has been successfully updated.")
            pause_screen()
        elif option == 4:
            #view the current OT task
            pass
             
#Employee Class for employees
class Employee:
    def __init__(self, name, base_pay, task):
        self.name = name
        self.base_pay = base_pay
        self.task = task

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
    choice = get_menu_choice(0, 3)

    if choice == 0:
        title("Closing the System...")
        pause_screen()
        break

    elif choice == 1:
        manage_staff()

    elif choice == 2:
        manage_overtime_details()
    
    elif choice == 3:
        pass
