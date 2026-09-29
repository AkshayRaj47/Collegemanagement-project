from person import Person
class Faculty(Person):
    def __init__(self,facultyId,name,age,department,mobile,address):
        super().__init__(name,age,mobile,address)
        self.facultyId=facultyId
        self.department=department
    def toFileString(self):
        return f"{self.facultyId},{self.name},{self.age},{self.department},{self.mobile},{self.address}\n"