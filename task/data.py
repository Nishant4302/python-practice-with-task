import names
import random

subjects = ["Python","Java","Html","Ruby","C"]

data = dict()

for i in range(100):
    student_name = names.get_full_name()
    marks = random.randint(1,99)
    sub = random.choice(subjects)

    d = {
        "rollno":i+1,
        "name":student_name,
        "marks":marks,
        "subject":sub
    }
    data[i+1] = d


print("{:6} | {:20} | {:10} | {:5}".format("rollno","name","subejct","marks"))
for i in data:
    print("{:6} + {:20} + {:10} + {:5}".format("------","--------------------","----------","-----"))
    print("{:6} | {:20} | {:10} | {:5}".format(data[i]["rollno"],data[i]["name"],data[i]["subject"],data[i]["marks"]))