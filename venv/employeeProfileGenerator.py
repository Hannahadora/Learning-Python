all_employees = []
welcome_message = '''Welcome to the Employee Profile Generator!
          This program will help you create a profile for an employee by asking you a series of questions about their information and preferences.'''

def addEmployeeProfile():
    employee_name = input("Enter the employee's name: ")
    employee_age = input("Enter the employee's age: ")
    employee_department = input("Enter the employee's department: ")
    employee_position = input("Enter the employee's position: ")
    employee_hobbies = input("Enter the employee's hobbies (comma separated): ")
    
    profile = f"Employee Name: {employee_name}\nAge: {employee_age}\nDepartment: {employee_department}\nPosition: {employee_position}\nHobbies: {employee_hobbies}"
    
    print("\nGenerated Employee Profile:")
    print(profile)
    all_employees.append(profile)
    print(f"\nTotal employees generated: {len(all_employees)}")

def editEmployeeProfile():
    if len(all_employees) == 0:
        print("No employee profiles to edit, please add some first.")
    else:
        print("\nEmployee Profiles:")
        for i, profile in enumerate(all_employees, start=1):
            print(f"{i}. {profile.splitlines()[0]}")  # Display only the employee name
        command = input("\nEnter the employee number to edit (1, 2, ...): ")
        employee_to_edit = int(command) - 1
        if 0 <= employee_to_edit < len(all_employees):
            print(f"\nEditing profile for {all_employees[employee_to_edit].splitlines()[0]}:")
            print("Please answer the following questions to update the employee's profile:")
            print("Note: You can leave any field blank to keep the current value.")
            addEmployeeProfile()
            all_employees[employee_to_edit] = all_employees[-1]  # Replace the old profile with the new one
            all_employees.pop()  # Remove the duplicate profile added by addEmployeeProfile()

def viewEmployeeProfiles():
    if len(all_employees) == 0:
        print("No employee profiles to view, please add some first.")
    else:
        print("\nEmployee Profiles:")
        for profile in all_employees:
            print(profile)
            print("-" * 40)  # Separator between profiles

def employeeProfileGenerator():
    print(welcome_message)
    command = input("Enter a command (start, exit): ")

    while command != "exit":
        
        if command == "start":
            addEmployeeProfile()
            if len(all_employees) > 0:
                print(f"\nTotal employees generated: {len(all_employees)}")
                command = input("\nEnter a command (add, edit, exit, view): ")
                while command != "exit":
                    if command == "add":
                        addEmployeeProfile()
                        command = input("\nEnter a command (add, edit, exit, view): ")
                    elif command == "edit":
                        editEmployeeProfile()
                        command = input("\nEnter a command (add, edit, exit, view): ")
                    elif command == "view":
                        viewEmployeeProfiles()
                        command = input("\nEnter a command (add, edit, exit, view): ")
                    else:
                        print("Invalid command. Please try again.")
                        command = input("\nEnter a command (add, edit, exit, view): ")
                break
        else:
            print("Invalid command. Please enter 'start' or 'exit'.")
            command = input("Enter a command (start, exit): ")
    
    print("Exiting Employee Profile Generator. Goodbye!")

if __name__ == "__main__":
    employeeProfileGenerator()