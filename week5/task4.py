class Employee:
    def __init__(self, salary):
        self._salary = salary
    def salary(self):
        return self._salary
    def role(self):
        return "Employee"
class Manager(Employee):
    def __init__(self, salary, bonus):
        super().__init__(salary)
        self._bonus = bonus
    def role(self):
        return "Manager"
    def bonus(self):
        return self._bonus
def info(employees):
    for e in employees:
        print(f"Role: {e.role()}, Salary: {e.salary()}")
if __name__ == "__main__":
    e1 = Employee(1000)
    e2 = Employee(1500)
    m1 = Manager(3000, 500)
    staff = [e1, e2, m1]
    info(staff)
