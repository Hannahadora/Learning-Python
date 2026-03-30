def reportCardGenerator(name, grade):
    if grade >= 90:
        letter_grade = 'A'
    elif grade >= 80:
        letter_grade = 'B'
    elif grade >= 70:
        letter_grade = 'C'
    elif grade >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    
    return f"{name} received a grade of {letter_grade}."


if __name__ == "__main__":
    print("Welcome to the Report Card Generator!")
    command = input("Enter a command (start, exit): ")
    while command != "exit":
        student_name = input("Enter the student's name: ")
        try:
            student_grade = float(input("Enter the student's grade (0-100): "))
            if 0 <= student_grade <= 100:
                report_card = reportCardGenerator(student_name, student_grade)
                print(report_card)
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for the grade.")