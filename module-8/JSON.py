import json

# Function to load student data from the JSON file
def load_students():
    try:
        with open('student.json', 'r') as file:
            students = json.load(file)  # Load the content of the JSON file
        return students
    except FileNotFoundError:
        print("Error: student.json file not found.")
        return []

# Function to print the student list in the specified format
def print_student_list(students):
    print("Original Student List:")
    for student in students:
        print(f"{student['first_name']} {student['last_name']} : ID = {student['id']} , Email = {student['email']}")
    print("\n")

# Function to append a new student to the list
def append_student(students, first_name, last_name, student_id, email):
    new_student = {
        "first_name": first_name,
        "last_name": last_name,
        "id": student_id,
        "email": email
    }
    students.append(new_student)  # Add the new student to the list

# Function to update the student.json file with the new data
def update_json_file(students):
    with open('student.json', 'w') as file:
        json.dump(students, file, indent=4)  # Write the updated list back to the file

# Main program logic
def main():
    # Load the original student list from the JSON file
    students = load_students()

    # Check if the file loaded successfully
    if not students:
        print("Exiting due to missing or empty student list.")
        return

    # Print the original list of students
    print_student_list(students)

    # Prompt user to add their fictional student data
    first_name = "John"  # Example first name
    last_name = "Doe"    # Example last name
    student_id = "99999"  # Example ID
    email = "johndoe@example.com"  # Example email

    # Append the new student to the list
    append_student(students, first_name, last_name, student_id, email)

    # Print the updated list of students
    print("Updated Student List:")
    print_student_list(students)

    # Update the student.json file with the new data
    update_json_file(students)

    # Notify the user that the file has been updated
    print("The student.json file has been updated.")

if __name__ == "__main__":
    main()
