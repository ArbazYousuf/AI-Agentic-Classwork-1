from models.student import Student
from report import print_report
from services.calculate import calculate
from utils.validate import nameCheck, validation
from utils.logger import logger

def main():
    logger.info("Program started")

    name = input("Enter student name: ")

    # Validate name
    if not nameCheck(name):
        return

    try:
        marks = int(input("Enter marks: "))
    except ValueError:
        print("Marks must be a number")
        logger.error("Marks entered were not a number")
        return

    # Validate marks
    if not validation(marks):
        return

    # Calculate grade
    grade = calculate(marks)
    logger.info(f"{name} got {marks} marks, grade {grade}")

    student = Student(name, marks, grade)

    print_report(student.name, student.marks, student.grade)
    logger.info("Program finished")

main()
