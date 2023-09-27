class faculty():
        def __init__(self,facultyname,facultyleacture,facultyphonenumber, facultysalary):
            self.facultyphonenumber=facultyphonenumber
            self.facultyname=facultyname
            self.facultyleacture=facultyleacture
            self.facultysalary=facultysalary
       

f=[
faculty("Ravi", "English", 9409156704, 25),
    faculty("Sarah", "Mathematics", 1234567890, 30),
    faculty("John", "History", 9876543210, 35),
    faculty("Lisa", "Science", 5555555555, 28),
    faculty("David", "Computer Science", 9998887777, 40),
    faculty("Emily", "Art", 1111222233, 32),
    faculty("Michael", "Physics", 7777777777, 27),
    faculty("Sophia", "Chemistry", 8888888888, 29),
    faculty("William", "Music", 6666666666, 33),
    faculty("Olivia", "Physical Education", 4444333322, 36)
]
print("-----------------------------------------------------------------------------------")
print("| {:15} | {:20} | {:20} | {:15} |".format("Faculty Name","FAculty Leacture","Faculty PhoneNumber","Faculty Salary"))
print("-----------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------")

for i in f:
    print("| {:15} | {:20} | {:20} | {:15} |".format(i.facultyname, i.facultyleacture, i.facultyphonenumber, i.facultysalary))
    print("-----------------------------------------------------------------------------------")

# print("-----------------------------------------------------------------------------------")
