#Payroll system
#Overtime rates
ot_rates = {
    "delivery" : 20,
    "light sauce" : 2
}

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

def pause():
    input("Press any key to continue: ")

#Employee List
employee_list = [
    Employee("Jia Jing", 3000, {})
]
#Program
while True:

#Main user interface
    print("-" * 5, "Welcome to BH Employee Payroll system", "-" * 5)
    print(f"""
Select the corrosponding value to view:
0. Exit the system
1. Current employees
2. Add / Remove an employee
3. Overtime matters
4. Total Salary
""")
#User inputs in menu
    choice = int(input("Enter the corrosponding Index: "))

    if choice == 0:
        break
    
    elif choice == 1:
        print("\n----- Employee List -----")
        for emp in employee_list:
            print(f"Name: {emp.name}")
            print(f"Base Salary: {emp.base}")
            print(f"Tasks: {emp.task}")
            print("-" * 10)
        pause()

#Adding new employee
    elif choice == 2:
        pick = int(input("\nWould you like to 1. add or 2. remove an employee? Enter the Index: "))
        if pick == 1:
            print("\n----- Add an employee -----")
            new_emp_name = input("Enter the employee name: ")
            new_emp_base = int(input(f"Enter {new_emp_name} base salary: "))
#Add employee
            new_employee = Employee(new_emp_name, new_emp_base, {})
            employee_list.append(new_employee)
            print(f"\n{new_emp_name} has been added to the system")
            pause()
#Remove employee        
        elif pick == 2:
            print("\n----- Employee List -----")
            for index, emp in enumerate(employee_list):
                print(f"{index}. {emp.name}")
            emp_index = int(input("\nEnter the Index: "))
            emp_name = employee_list[emp_index].name
            employee_list.pop(emp_index)
            print(f"\n{emp_name} has been removed from the system")
#Adding Overtime task
    elif choice == 3:
        print("\n----- Adding employee OT -----")
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

#Calculate total salary
    elif choice == 4: 
        print("\n----- Total Pay -----")
        for emp in employee_list:
            name = emp.name
            total_pay = emp.calculate_pay(ot_rates)
            print(f"{name}: {total_pay}")
            print("-----")
        pause()