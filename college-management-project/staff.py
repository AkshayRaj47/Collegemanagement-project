from person import Person
class Staff(Person):
    def __init__(self, staffId,name,age,department,mobile,address):
        super().__init__(name,age,mobile,address)
        self.staffId=staffId
        self.department=department

    def toFileString(self):
        return f"{self.staffId},{self.name},{self.age},{self.department},{self.mobile},{self.address}\n"