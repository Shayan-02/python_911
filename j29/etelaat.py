class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def introduce(self):
        return f"My name is {self.name} and I'm {self.age} years old."


class Student(Person):
    def __init__(self, name, age, job="daneshamooz", student_id=""):
        super().__init__(name, age, job)
        self.student_id = student_id

    def introduce(self):
        return super().introduce() + f" My student ID is {self.student_id}."


class Baby(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
