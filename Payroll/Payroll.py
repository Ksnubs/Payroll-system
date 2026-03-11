#Payroll system

#Employee List
employee_list = [
    {"name" : "Jia Jing",
    "base" : 2000,
    "task" : {}}
]

#Overtime rates
ot_rates = {}

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
            task_rate = ot_rates.get(task_name, 0)
            total_pay += ( task_rate * count )
        
        return(total_pay)
    
#Program
while True:

#Main user interface
    print("-" * 5, "Welcome to BH Employee Payroll system", "-" * 5)
    print(f"""
Select the corrosponding value to view:
0. Exit the system
1. View current employees
2. Add / Remove an employee
3. Overtime matters
""")
#User inputs in menu
    choice = int(input("Enter the number: "))

    if choice == 0:
        break
    
    elif choice == 1:
        print("\n----- Employee List -----")
        for emp in employee_list:
            print("-" * 25)
            for key, value in emp.items():
                print(f"{key} | {value}")
        exit = input("Press any key to continue: ")

#Adding new employee
    elif choice == 2:
        print("\n----- Add an employee -----")
        new_emp_name = input("Enter the employee name: ")
        new_emp_base = int(input(f"Enter {new_emp_name} base salary: "))
#New employee
        new_emp = {"name" : new_emp_name,
                   "base" : new_emp_base,
                   "task" : {} }
        employee_list.append(new_emp)
        print(f"\n{new_emp_name} has been added to the system")
        exit = input("Press any key to continue: ")

#Adding Overtime task
    elif choice == 3:
        print("\n----- Adding employee OT -----")
        for index, emp in enumerate(employee_list):
            name = emp["name"]
            print(f"{index + 1}: {name}")
        exit = input("To continue press any key: ")