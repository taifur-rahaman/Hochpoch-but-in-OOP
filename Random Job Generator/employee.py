

class Employee:
    _emp_id = 1000
    count = 0
    def __init__(self, name="John Doe", salary=0, designation="None"):
        self._name = name
        self._salary = salary
        self._designation = designation
        Employee._emp_id += 1
        self._emp_id = Employee._emp_id
        Employee.count += 1
    
    @property
    def emp_id(self):
        return self._emp_id

    def emp_count():
        return Employee.count
    
    def __str__(self):
        return f"Name: {self._name}\nSalary: {self._salary}\nDesignation: {self._designation}\nEmployee ID: {self._emp_id}\n"
