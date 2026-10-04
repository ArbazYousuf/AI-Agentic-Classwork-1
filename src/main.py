
from models.student import Student
from report import print_report
from services.calculate import calculate
from utils.validate import nameCheck, validation

def main():

    name = input("Enter student name: ") 

    # Validate name 
    nameCheck(name)
 
    marks = int(input("Enter marks: ")) 
    
    # Validate marks 
    validation(marks)
        
    # Calculate grade 
    grade = calculate(marks)

    student = Student(name, marks, grade)

    print_report(student.name, student.marks, student.grade)

main()