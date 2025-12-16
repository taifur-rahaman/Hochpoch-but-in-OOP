from employee import Employee
import random

try:
    with open("jobTitles.txt", "r") as file:
        job_titles = file.read().splitlines()
except FileNotFoundError:
    print("File Not Found. Please Try Again.")

employees = {}

emp_qty = int(input("Enter the number of Employees to add: "))

for i in range(emp_qty):
    while True:
        emp_name = input("Enter Employee Name: ")
        if emp_name == "":
            print("Invalid Input. Please Try Again.")
            continue
        elif emp_name.isdigit():
            print("Must be a String. Please Try Again.")
            continue
    
        emp_designation = random.choice(job_titles)
        emp_salary = random.randint(25000, 75000)
        
        employees[Employee.count] = Employee(emp_name, emp_salary, emp_designation)
        print(f"Employee {Employee.count} Added Successfully\n")
        break

for id, emp in employees.items():
    print(f"\nEmployee Number - {id}\n{emp}\n")