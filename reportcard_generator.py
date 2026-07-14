#objectives
'''1. To create a report card generator that takes student details and their marks in various subjects, calculates total marks, percentage, grade, and result, and generates individual and class report cards in CSV format.

2. To ensure that the marks entered for each subject are within the valid range (0-100) and handle invalid inputs appropriately.

3. To provide an option for the user to add multiple students and generate a comprehensive class report card that includes all students' details and their respective marks, grades, and results.

4. To create a dedicated report card in which it has all the details of the student, we can save the report card to another CSV file'''


import pandas as pd

subjects = ["English", "Maths", "Science", "SST", "Hindi", "EVS"]
class_report= []
# scores = []

print("==== REPORT CARD GENERATOR ====")



while True:

    name = input("Enter Student Name: ").title()
    enroll_no = input("Enter Enrollment Number: ")

    scores = []


     # Entering marks for each subject
    for subject in subjects:

        score = int(input(f"Enter marks in {subject} (0-100): "))

        while score < 0 or score > 100:
            print("Marks should be between 0 and 100.")
            score = int(input(f"Enter marks in {subject} (0-100): "))

        scores.append(score)


        # Calculations
        total_marks = len(subjects) * 100
        marks_obtained = sum(scores)
        percentage = (marks_obtained / total_marks) * 100

        # Grade
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

# Result
        if percentage >= 40:
            result = "PASS"
        else:
            result = "FAIL"

# Create DataFrame
    report_card = pd.DataFrame({
    "Subject": subjects,
    "Marks": scores
})

     # Store student details
    student = {
        "Name": name,
        "Enrollment No": enroll_no
    }

    # Add subject marks
    for i in range(len(subjects)):
        print(subjects[i], ":", scores[i], "/100")

    # Add summary
    student["Total Marks"] = marks_obtained
    student["Percentage"] = round(percentage, 2)
    student["Grade"] = grade
    student["Result"] = result

    # appending student to class report
    class_report.append(student)

    # printing individual report
    print("\n========== REPORT CARD ==========")
    print(f"Student Name      : {name}")
    print(f"Enrollment Number : {enroll_no}")

    print("\nSubject-wise Marks")

    for i in range(len(subjects)):
        print(subjects[i], ":", scores[i], "/100")

    print("\nTotal Marks    :", marks_obtained, "/", total_marks)
    print(f"Percentage     : {percentage:.2f}%")
    print("Grade          :", grade)
    print("Result         :", result)

    # Ask for another student
    choice = input("\nDo you want to add another student? (yes/no): ").lower()

    if choice != "yes":
        break

# Create DataFrame for entire class
class_df = pd.DataFrame(class_report)

#saving the detailed report to CSV
class_df.to_csv("Class_Report_Card.csv", index=False)

print("\n\n")
print("Class Report Card Generated Successfully!")
print("Saved as 'Class_Report_Card.csv'")
print("\n\n")

# Display complete class report
print("\nComplete Class Report")
print(class_df)


report_card.to_csv(f"{name.replace(' ', '_')}_report_card.csv", index=False)

print(f"\nReport card for {name} has been saved as '{name.replace(' ', '_')}_report_card.csv'.")



