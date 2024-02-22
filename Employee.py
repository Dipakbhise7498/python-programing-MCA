class Employee:
    def __init__(self, emp_id, emp_name,emp_address,emp_salary):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_address=emp_address
        self.emp_salary=emp_salary
    
    def show_info(self):
        print(f"Employee Id is {self.emp_id}")
        print(f"Employee Name is {self.emp_name}")
        print(f"Employee Address is {self.emp_address}")
        print(f"Employee Salary is {self.emp_salary}")

    def __del__(self):
        print("Destructor created, Employee deleted")
e1=Employee(111,"Raj","Pune",70000.99)
e1.show_info()