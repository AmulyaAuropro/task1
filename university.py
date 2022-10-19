from operator import __le__


class Person:
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age
    
   # Prints the full name
    def print_name(self):
        print(f'FullName : {self.fname} {self.lname}')

class Student(Person):
    def __init__(self,fname,lname,age):
        super().__init__(fname,lname,age)
        self.lectures = []

    # List the lectures, which the student attends
    def list_lectures(self):
        print("Listing all the lectures :")
        for lecture in  self.lectures:
            print(lecture)
    
    # Add new lectures to the lectures list (attend a new lecture)
    def add_lecture(self,lecture):
        print(f'New lecture({lecture}) added...')
        self.lectures.append(lecture)

    def remove_lecture(self,lecture):
        print(f'Lecture({lecture}) removed..')
        self.lectures.remove(lecture)

    pass
    
class Professor(Person):
    def __init__(self,fname,lname,age):
        super().__init__(fname,lname,age)
        self.subjects = []

    # List the subjects
    def list_subjects(self):
        print("Listing all the subjects :")
        for subject in  self.subjects:
            print(subject)
    
    # Add new subject to the subjects list
    def add_subject(self,subject):
        print(f'New subject({subject}) added...')
        self.subjects.append(subject)

    def remove_subject(self,subject):
        print(f'Subject ({subject}) removed..')
        self.subjects.remove(subject)
    pass

class Lecture:
    def __init__(self,name,max_students,duration):
        self.name = name
        self.max_students = max_students
        self.duration = duration
        self.professors = []

    def print_lecture_info(self):
        print(f'Lecture Name : {self.name}')
        print(f'Duration : {self.duration}')

    def add_professor(self,professor):
        self.professors.append(professor)


s1 = Student("Amulya","Kanaparthi",22)
s1.print_name()
s1.add_lecture("python")
s1.add_lecture("linux")
s1.remove_lecture("python")
s1.list_lectures()

p1 = Professor("Manoj","Reddy",30)
p1.print_name()
p1.add_subject("python")
p1.add_subject("linux")
p1.list_subjects()

l1 = Lecture("Python",20,120)
l1.print_lecture_info()



OUTPUT:
 FullName : Amulya Kanaparthi
New lecture(python) added...
New lecture(linux) added...
Lecture(python) removed..
Listing all the lectures :
linux
FullName : Manoj Reddy
New subject(python) added...
New subject(linux) added...
Listing all the subjects :
python
linux
Lecture Name : Python
Duration : 120
