import re

def abstract_information(text):
    information = {}
    lines = text.split("\n")
    for line in lines:
        if "Student(s):" in line:
            Student = line.split(":")[1].strip()
            information["Student(s)"] = Student
        elif "Email:" in line:
            email = line.split(":")[1].strip()
            information["Email"] = email
        elif "Date:" in line:
            date = line.split(":")[1].strip()
            information["Date"] = date
        elif "Begin:" in line:
            begin = line.split(":")[1].strip()
            information["Begin"] = begin
        elif "End:" in line:
            end = line.split(":")[1].strip()
            information["End"] = end
    return information
