"""
Python Alchemy

Module:
chapters.chapter_05_organizing_data.mini_project

University Student Information System (USIS)
Demonstrates: list, tuple, set, dict, and string operations
"""

# Step 1: Using a dictionary to store student data
students = {
    101: {"name": "Ivaan", 
	"courses": ["Math", "Biology", "Chemistry"], "year": 1},
    102: {"name": "Laisha", 
	"courses": ["History", "Economics", "Math"], "year": 2},
    103: {"name": "Eve", 
	"courses": ["Physics", "Math", "Computer Science"], "year": 1}
}

# Step 2: Add a new student (dictionary + list)
students[104] = {"name": "Dravid",
	 "courses": ["English", "Economics"], "year": 3}

# Step 3: Use tuple for fixed data (university details)
university_info = ("Global Institute of Technology", 
			"Spring Semester 2025", 
			"Dean: Dr. Rachel Moore")

# Step 4: Use a set to find unique courses offered
all_courses = set()
for data in students.values():
    all_courses.update(data["courses"])

# Step 5: Generate a formatted report (string operations)
print("=" * 50)
print(f"Welcome to {university_info[0]}")
print(f"Academic Term: {university_info[1]}")
print(university_info[2])
print("=" * 50)

# Step 6: Display student details
for sid, info in students.items():
    print(f"\nStudent ID: {sid}")
    print(f"Name      : {info['name']}")
    print(f"Year      : {info['year']}")
    print(f"Courses   : {', '.join(info['courses'])}")

# Step 7: Display summary analytics using sets and lists
print("\n" + "-" * 50)
print(f"Total Students Enrolled: {len(students)}")
print(f"Unique Courses Offered : {len(all_courses)}")
print("List of All Courses    :", ", ".join(sorted(all_courses)))

# Step 8: Search feature demonstration (string and dict)
search_name = input("\nEnter a student’s name to search: ").strip().title()
found = False
for sid, info in students.items():
    if search_name in info['name']:
        print(f"\nRecord Found → ID: {sid}, Year: {info['year']}, Courses: {info['courses']}")
        found = True
if not found:
    print("No record found for the entered name.")

print("\n" + "=" * 50)
print("End of Report — Data processed successfully!")
print("=" * 50)