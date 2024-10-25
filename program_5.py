# PSEUDOCODE
#Initialize a dictionary courses with the following course IDs and names:

#'COS 1001': 'Intro to Computer Science',
#'COS 2005': 'Python Programming'
#'COS 3002': 'Data Structures'
#'COS 4001': 'Web Development'
#'COS 5003': 'Machine Learning'
#'COS 6004': 'Artificial Intelligence'
#'MAT 1001': 'Calculus I'
#'MAT 1002': 'Calculus II'
#'MAT 2002': 'Linear Algebra'
#'MAT 3003': 'Statistics'
#'MAT 4004': 'Differential Equations'
#'ENG 1001': 'English Literature'
#'ENG 2002': 'Creative Writing'
#'ENG 4004': 'Shakespeare Studies'
#'PHY 1001': 'Physics I'
#'PHY 2002': 'Thermodynamics'
#'PHY 3003': 'Quantum Mechanics'
#'PHY 4004': 'Electromagnetism'
#'BIO 1001: 'General Biology'
#'BIO 2002': 'Genetics'
#'BIO 3003': 'Microbiology'
#'BIO 4004': 'Ecology'
#'CHE 1001': 'General Chemistry'
#'CHE 2002': 'Organic Chemistry'
#'CHE 3003': 'Physical Chemistry'
#Prompt the user to enter a subject code (e.g., "COS") and convert it to uppercase.
#Initialize a variable found to False to track if any courses match the subject.
#Display the message "Courses for subject [subject]:"
#Loop through each course_id and course_name in the courses dictionary:
#If course_id starts with subject:
#Print the course_id and course_name.
#Set found to True.
#If found is False:
#Print "No courses found for that subject."

# ACTUAL CODE
# Predefined dictionary of courses with their IDs and names (Made up)
courses = {
    'COS 1001': 'Intro to Computer Science',
    'COS 2005': 'Python Programming',
    'COS 3002': 'Data Structures',
    'COS 4001': 'Web Development',
    'COS 5003': 'Machine Learning',
    'COS 6004': 'Artificial Intelligence',
    'MAT 1001': 'Calculus I',
    'MAT 1002': 'Calculus II',
    'MAT 2002': 'Linear Algebra',
    'MAT 3003': 'Statistics',
    'MAT 4004': 'Differential Equations',
    'ENG 1001': 'English Literature',
    'ENG 2002': 'Creative Writing',
    'ENG 3003': 'Modern Poetry',
    'ENG 4004': 'Shakespeare Studies',
    'PHY 1001': 'Physics I',
    'PHY 2002': 'Thermodynamics',
    'PHY 3003': 'Quantum Mechanics',
    'PHY 4004': 'Electromagnetism',
    'BIO 1001': 'General Biology',
    'BIO 2002': 'Genetics',
    'BIO 3003': 'Microbiology',
    'BIO 4004': 'Ecology',
    'CHE 1001': 'General Chemistry',
    'CHE 2002': 'Organic Chemistry',
    'CHE 3003': 'Physical Chemistry'
}

# Ask the user for a subject to search for
subject = input("Enter a subject code to filter courses (e.g., COS, MAT, ENG, PHY, BIO, CHE.): ").strip().upper()

# Display the courses that match the subject
print(f"\nCourses for subject {subject}:")
found = False
for course_id, course_name in courses.items():
    # Check if the course ID starts with the subject code
    if course_id.startswith(subject):
        print(f"{course_id}: {course_name}")
        found = True

if not found:
    print("No courses found for that subject.")
