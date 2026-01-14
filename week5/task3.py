class Person:
    def __init__(self, name):
        self._name = name
    def introduce(self):
        return f"Hi, my name is {self._name}"
class Student(Person):
    def __init__(self, name, university):
        super().__init__(name)
        self._university = university
    def introduce(self):
        return f"Hi, I am {self._name} and I study at {self._university}"
def demo():
    p1 = Person("Alice")
    s1 = Student("Bob", "AITU")
    people = [p1, s1]
    for p in people:
        print(p.introduce())
if __name__ == "__main__":
    demo()