# Author: Rodolfo
# Date: October 28th
# This script displays the major name and office location based on the student's major code.

# Student info
student_name = input("Enter the student's name: ")
student_major = input("Enter the student's major code (e.g., ENG): ").upper()  # Major code in uppercase

# Use conditional logic to find the major name and office location based on the code
if student_major == "ENG":
    major_name = "Engineering"
    office_location = "Building A"
elif student_major == "SCI":
    major_name = "Science"
    office_location = "Building B"
elif student_major == "BUS":
    major_name = "Business"
    office_location = "Building C"
elif student_major == "ART":
    major_name = "Art"
    office_location = "Building D"
elif student_major == "MED":
    major_name = "Medicine"
    office_location = "Building E"
else:
    major_name = "<unknown>"  # Unlisted codes
    office_location = ""      # No location for unknown majors

# Results
print(f"Student Name: {student_name}")
print(f"Major: {major_name}")
if office_location:
    print(f"Office Location: {office_location}")