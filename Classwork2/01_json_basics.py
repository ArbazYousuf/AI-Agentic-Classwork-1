# Phase 3 A/B - JSON basics and JSON -> Python

import json

# a JSON object (like the response of GET /students/101)
student_json = '{"id": 101, "name": "Arbaz", "program": "MS AI", "courses": ["Agentic AI", "NLP"]}'

# a JSON array of objects
students_json = """
[
    {"id": 101, "name": "Arbaz", "gpa": 3.6},
    {"id": 102, "name": "Ali", "gpa": 3.2},
    {"id": 103, "name": "Sara", "gpa": 3.9}
]
"""

# JSON object -> python dict
student = json.loads(student_json)
print(type(student))
print("Name:", student["name"])
print("Program:", student["program"])
print("First course:", student["courses"][0])

# JSON array -> python list of dicts
students = json.loads(students_json)
print("\n", type(students), "with", len(students), "students")
for s in students:
    print(f"  {s['id']} - {s['name']} - GPA {s['gpa']}")

# python dict -> JSON string (what we send in a POST body)
new_student = {"name": "Usman", "program": "MS AI"}
print("\nAs JSON:", json.dumps(new_student))
