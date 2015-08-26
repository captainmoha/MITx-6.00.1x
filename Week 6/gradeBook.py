import datetime

class Person(object):
    def __init__(self, name):
        self.name = name
        self.birthday = None
        # two ways to get the last name 
        self.lastName = name.split(' ')[-1]
            #lastBlank = self.name.rindex(' ') 
                #self.lastName = self.name[lastBlank + 1: ]
    def getLastName(self):
        return self.lastName
        
    def setBirthday(self, year, month, day):
        self.birthday = datetime.date(year, month, day)
            
    def getAge(self):
        if self.birthday is None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
        
    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
            
    def __str__(self):
        return self.name

class MITPerson(Person):
    nextIdNum = 0

    def __init__(self, name):
        # initialize person attributes
        Person.__init__(self, name) 
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum
    # sorting in MITPerson uses id not name
    def __lt__(self, other):
        return self.idNum < other.idNum

class Student(MITPerson):
    pass
class underGrad(Student):

    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year

class grad(Student):
    pass

def isStudent(obj):
    return isinstance(obj, Student)

class Grades(object):
    """A mapping from Students to a list of grades"""
    def __init__(self):
        self.students = [] # list of student objects
        self.grades = {}  # maps (idNum to list of grades)
        self.isSorted = True # true if self.students is sorted

    def addStudent(self, student):
        """Assumes student is of type student 
        add student to the grade book"""
        if student in self.students:
            raise ValueError("Duplicate student")
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
    def addGrade(self, student, grade):
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError("Student not in grade book")

    def getGrades(self, student):
        try:
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError("Student not in grade book")

    def allStudents(self):
        """Return a list of the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        for s in self.students:
            yield s
        # return self.students[:]
        # return copy of students list

def gradeReport(course):
    """Assumes course is of type grades"""
    report = []

    for s in course.allStudents():
        total = 0.0
        numGrades = 0
        for grade in course.getGrades(s):
            total += grade
            numGrades += 1
        try:
            average = total / numGrades
            report.append(str(s) + "\'s mean grade is " + str(average))
        except ZeroDivisionError:
            report.append(str(s) + "Has no grades")
    return "\n".join(report)


# tests
ug1 = underGrad("Mohamed Ali", 2017)
ug2 = underGrad("Joey Tribiany", 2017)
ug3 = underGrad("Monica Giller", 2017)
g1 = grad("Ross Giller")
g2 = grad("Phoebe Buffet")

friend101 = Grades()
friend101.addStudent(ug1)
friend101.addStudent(ug2)
friend101.addStudent(ug3)
friend101.addStudent(g1)
friend101.addStudent(g2)

# friend101.allStudents()
