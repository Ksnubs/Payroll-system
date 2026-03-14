#Payroll system
#Overtime rates
ot_rates = {
    "delivery" : 20,
    "light sauce" : 2
}
#Function to ask for input
def get_user_input():
    while True:
        try:
            choice = int(input("\nEnter a Index: "))
            break
        except(ValueError):
            print("Please enter a valid Index")
    return(choice)

def pause():
    input("Press any key to continue: ")

def line_break(num):
    print("-" * num)

def title(title, num):
    print("-" * num,f" {title} ", "-" * num)

#Employee class
class Employee:
    def __init__(self, name, base, task):
        self.name = name
        self.base = base
        self.task = task
  
#Calculating total pay inclusive of OT     
    def calculate_pay(self, task_rates):
        total_pay = self.base

        for task_name, count in self.task.items():
            task_rate = task_rates.get(task_name, 0)
            total_pay += ( task_rate * count )
        
        return(total_pay)

#Employee List
employee_list = [
    Employee("Jia Jing", 3000, {})
]
#Welcome title
title("Welcome to BH HR system", 11)
#Program
while True:
#Main user interface
    line_break(49)
    print("Select the option you want by pressing the Index")
    print("0. Exit the system")
    print("1. Current Employee List")
    print("2. Edit Current Employee List")
    print("3. Overtime Matters")
    print("4. Salaries")
    
#User inputs in menu
    choice = get_user_input()

    if choice == 0:
        print("Closing the System. Thank you")
        pause()
        break
    
    elif choice == 1:
        title("Employee list", 10)
        for emp in employee_list:
            print(f"Name: {emp.name}")
            print(f"Base Salary: {emp.base}")
            print(f"Tasks: {emp.task}")
            print("-" * 10)
        pause()

#Adding new employee
    elif choice == 2:
        title("Choose an option", 10)
        print("1. Add an Employee")
        print("2. Remove an Employee")
        pick = get_user_input()
        if pick == 1:
            title("Add Employee", 15)
            new_emp_name = input("Enter the employee name: ")
            new_emp_base = int(input(f"Enter {new_emp_name} base salary: "))
#Add employee
            new_employee = Employee(new_emp_name, new_emp_base, {})
            employee_list.append(new_employee)
            print(f"\n{new_emp_name} has been added to the system")
            pause()
#Remove employee        
        elif pick == 2:
            title("Remove Employee", 10)
            for index, emp in enumerate(employee_list):
                print(f"{index}. {emp.name}")
            emp_index = int(input("\nEnter the Index: "))
            emp_name = employee_list[emp_index].name
            employee_list.pop(emp_index)
            print(f"\n{emp_name} has been removed from the system")
            pause()
#Adding Overtime task
    elif choice == 3:
        title("Add an OT", 15)
        for index, emp in enumerate(employee_list):
            name = emp.name
            print(f"{index}: {name}")

        emp_index = int(input("\nEnter employee's index: "))

        print("----- List of task -----")
        for index, task_name in enumerate(ot_rates):
            print(f"{index}. {task_name}")
        
        task_index = int(input("\nEnter the task index: "))
        task_key = list(ot_rates.keys())[task_index]
        amount = int(input("Enter amount: "))
#Adding to OT task to dictionary
        employee_list[emp_index].task[task_key] = amount
        pause()

#Calculate total salary
    elif choice == 4: 
        print("\n----- Total Pay -----")
        for emp in employee_list:
            name = emp.name
            total_pay = emp.calculate_pay(ot_rates)
            print(f"{name}: {total_pay}")
            print("-----")
        pause()