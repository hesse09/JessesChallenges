students = [
    {"name": "Taylor", "grades": [92, 88, 95, 100]},
    {"name": "Chris", "grades": [70, 75, 68, 80]},
    {"name": "Morgan", "grades": [85, 87, 90, 84]},
    {"name": "Jordan", "grades": [59, 62, 58, 65]},
    {"name": "Casey", "grades": [100, 98, 96, 99]},
]

def get_average(grades):
    number_in = len(grades)
    total = 0
    for i in grades:
        total += i
    return total / number_in

def get_letter_grade(average):
    if average <= 100 and average >= 90:
        return "A"
    elif average <= 89.99 and average >= 80:
        return "B"
    elif average <= 79.99 and average >= 70:
        return "C"
    elif average <= 69.99 and average >= 60:
        return "D"
    else:
        return "F"

def get_student_report(student):
    student_report: dict = {}
    for j in students:
        student_average = get_average(j["grades"])
        student_grade = get_letter_grade(student_average)

        student_report[j["name"]] = {"Grades": j["grades"],
                                     "Average": student_average,
                                     "Letter Grade": student_grade}

    
    return student_report


def get_class_average(students):
    temp: list = []
    #Extract
    for k in students:
        for i in students[k]["Grades"]:
            temp.append(i)
    
    lenT = len(temp)
    total = 0
    for iter in temp:
        total += iter
    
    return total / lenT 


def get_top_student(students):
    temp: list = []
    for k in students:
        temp.append((k, students[k]["Average"]))
    
    highest = 0
    highest_name = ""
    for i in temp:
        if i[1] > highest:
            highest = i[1]
            highest_name = i[0]
    return highest_name, highest


def get_failing_students(students):
    failing: list = []
    for k in students:
        if students[k]["Letter Grade"] == "F":
            failing.append(k)
    
    return failing

def print_gradebook_report(students):
    #first lets use students reoirt to make each kid a table and not. a massive list of tables
    student_report = get_student_report(students)
    print(student_report)
    #lets add grades and averages to the report
    
        
    print("GRADEBOOK REPORT\n----------------")
    for k in student_report:
        print("%s: %.2f%% - %s" % (k, student_report[k]["Average"], student_report[k]["Letter Grade"]))
    
    class_average = get_class_average(student_report)
    hN, h = get_top_student(student_report)
    failing_students = get_failing_students(student_report)
    print("\nClass Average: %.2f%%" % class_average)
    print("Top Student: %s - %.2f%%" % (hN, h))
    print("\nFailing Students:")
    if len(failing_students) == 0:
        print(None)
    else:
        for f in failing_students:
            print(f)
    
print_gradebook_report(students)

# GRADEBOOK REPORT
# ----------------
# Taylor: 93.75% - A
# Chris: 73.25% - C
# Morgan: 86.50% - B
# Jordan: 61.00% - D
# Casey: 98.25% - A
#
# Class Average: 82.55%
# Top Student: Casey - 98.25%
#
# Failing Students:
# None
