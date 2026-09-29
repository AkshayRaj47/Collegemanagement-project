from array import array
from person import Person
class Student(Person):
    def __init__(self,studentId,name,department,age,mobile,address,fees,marksList):
        super().__init__(name,age,mobile,address)
        self.studentId = studentId
        self.department = department
        self.fees = fees
        self.marks = array("d", [float(m) for m in marksList if str(m).strip()])
    def calculateAverage(self):
        if len(self.marks)==0:
            return 0.0
        return sum(self.marks)/len(self.marks)
    def calculateGrade(self):
        avg=self.calculateAverage()
        if avg>=90:
            return "A+"
        elif avg>=80:
            return "A"
        elif avg>=70:
            return "B"
        elif avg>=60:
            return "C"
        elif avg>=50:
            return "D"
        else:
            return "F"
    def toFileString(self):
        marksStr=";".join([str(m) for m in self.marks])
        return f"{self.studentId},{self.name},{self.department},{self.age},{self.mobile},{self.address},{self.fees},{marksStr}\n"