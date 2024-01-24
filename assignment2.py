class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self, employees):
        self.employees = employees

    def display_table(self):
        print("Employee Table:")
        print("Employee ID\tName\tAge\tSalary (PM)")
        for emp in self.employees:
            print(f"{emp.emp_id}\t\t{emp.name}\t{emp.age}\t{emp.salary}")

    def sort_table(self, sort_option):
        if sort_option == 1:
            self.employees.sort(key=lambda x: x.age)
        elif sort_option == 2:
            self.employees.sort(key=lambda x: x.name)
        elif sort_option == 3:
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid sorting option. Please choose 1, 2, or 3.")

# Sample data
employees_data = [
    Employee("161E90", "Ramu", 35, 59000),
    Employee("171E22", "Tejas", 30, 82100),
    Employee("171G55", "Abhi", 25, 100000),
    Employee("152K46", "Jaya", 32, 85000)
]

# Create EmployeeTable instance
employee_table = EmployeeTable(employees_data)

# Display the unsorted table
employee_table.display_table()

# Get user's sorting choice
sort_option = int(input("Enter sorting option (1. Age, 2. Name, 3. Salary): "))

# Sort and display the table based on the user's choice
employee_table.sort_table(sort_option)
print("\nSorted Employee Table:")
employee_table.display_table()
