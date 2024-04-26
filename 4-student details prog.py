student_data = {
"101": {"name": "kavya", "marks": 75},
"102": {"name": "akhila", "marks": 99},
"103": {"name": "subbi", "marks": 90},
"104": {"name": "durga", "marks": 35},
"105": {"name": "Sany", "marks": 80}
}
# Function to check if a user exists and print their details
def check_user(roll_number):
   if roll_number in student_data:
       student = student_data[roll_number]
       name = student["name"]
       marks = student["marks"]
       result = "Pass" if marks >= 50 else "Fail"
       print(f"Student Name: {name}")
       print(f"Roll Number: {roll_number}")
       print(f"Marks: {marks}")
       print(f"Result: {result}")
   else:
       print("Student not found!")
# Example usage
roll_number = input("Enter student's roll number: ")
check_user(roll_number)