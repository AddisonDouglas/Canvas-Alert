# Import the Canvas class
from canvasapi import Canvas

# Canvas API URL
API_URL = "https://canvas.uw.edu"
# Canvas API key
API_KEY = "10~2fyu2iLVjm1XSaW5uc8QAQf8voBcevOCDQOwQNsQOaCeUw27VpOGic01sNETQWbp"

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)
# course = canvas.get_course(1714771)
# assignments = course.get_assignments(bucket='unsubmitted')

# for assignment in assignments:
#     print(assignment)


user = canvas.get_user(4432959)
courses = user.get_courses()
for courses in courses:
    assignments = user.get_assignments(courses);
    for assignments in assignments:
        print(assignments)