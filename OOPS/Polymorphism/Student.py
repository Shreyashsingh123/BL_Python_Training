class Student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def display(self):
        return f"{self.name}, Roll no{self.roll} marks{self.marks}"
    
class Classroom:
    def __init__(self):
        self.students={}#roll number key and student object is value
    
    def add(self,student):
        if student.roll in self.students:
            print("Student with this roll already exist")
        else:
            self.students[student.roll]=student
            print("student added successfully")
    def remove(self,roll):
        if roll in self.students:
            del self.students[roll]
            print("student deleted successfully")
        else:
            print("no student found")

    def search(self,roll):
        if roll in self.students:
            print(self.students[roll].display())
        else:
            print("invalid student")
    def displayAll(self):
        if not self.students:
            print("no student found")
            return
        else:
            print("all student details are: ")
            for i in self.students.values():
                print(i.display())
c1=Classroom()
s1=Student("shreyash",18,95)
s2=Student("Ram",17,90)
s3=Student("Aman",25,85)

c1.add(s1)
c1.add(s2)
c1.add(s3)
c1.displayAll()
c1.search(18)
c1.remove(17)
c1.displayAll()