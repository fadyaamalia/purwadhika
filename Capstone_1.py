# Fadya Amalia Zahra
# JCDSOL-014

def menu():
    while True:
        print("\n---Student Performance Data---")
        print("1. Student Data Report")
        print("2. Add Student Data")
        print("3. Update Student Data")
        print("4. Delete Student Data")
        print("5. Exit Program")
        
        pilihan = input("Select the main menu: ")
        
        if pilihan == '1':
            read_data()
        elif pilihan == '2':
            create_data()
        elif pilihan == '3':
            update_data()
        elif pilihan == '4':
            delete_data()
        elif pilihan == '5':
            while True:
                exit_program = input("Are you sure you want to exit the program? (yes/no): ").lower()
                if exit_program == 'yes':
                    print("Exiting the program.")
                    return 
                elif exit_program == 'no':
                    break  
                else:
                    print("The option you entered is not valid.")
        else:
            print("The option you entered is not valid.")


def read_data():
    while True:
        print("\n-------Report Data Menu-------")
        print("1. Report Data Students")
        print("2. Report Data by Filter")
        print("3. Back to Main Menu")
        
        submenu_choice = input("Select the sub-menu: ")
        
        if submenu_choice == '1':
            report_all_students()
        elif submenu_choice == '2':
            report_data_by_filter()
        elif submenu_choice == '3':
            break
        else:
            print("The option you entered is not valid.")

def report_all_students():
    print("\nReport Data Students")
    if students: 
        print("ID\tName\tClass\tPE\tMath\tScience")  
        print("-" * 50)
        for student in students:
            print(f"{student['student_id']}\t{student['name']}\t{student['class']}\t{student['PE']}\t{student['Math']}\t{student['Science']}")
    else:
        print("No student data available.")

def report_data_by_filter():
    print("\nReport Data by Filter")
    
    while True:
        class_filter = input("Enter class to filter: ").upper()
        filtered_students = [student for student in students if student['class'] == class_filter]
        
        if filtered_students:
            print("Filtered Data by Class:")
            print("ID\tName\tClass\tPE\tMath\tScience")
            print("-" * 50)
            for student in filtered_students:
                print(f"{student['student_id']}\t{student['name']}\t{student['class']}\t{student['PE']}\t{student['Math']}\t{student['Science']}")
            break
        else:
            print(f"No student data available for class {class_filter}.")


def create_data():
    while True:
        print("\n-----------Add Menu-----------")
        print("1. Add Student Data")
        print("2. Back to Main Menu")
        
        submenu_choice = input("Select the sub-menu: ")
        
        if submenu_choice == '1':
            while True:
                student_id = input("Enter student ID: ")
                if student_id.isdigit():
                    student_id = int(student_id)
                    break
                else:
                    print("The option you entered is not valid. Please input an integer for student ID.")
            
            while True:
                name = input("Enter student name: ").title()
                if name.isalpha():
                    break
                else:
                    print("The option you entered is not valid. Please enter alphabetic characters only for name.")
            
            class_name = input("Enter student class: ").upper() 
            while True:
                try:
                    PE = float(input("Enter student PE score: "))
                    Math = float(input("Enter student Math score: "))
                    Science = float(input("Enter student Science score: "))
                    break
                except ValueError:
                    print("The option you entered is not valid. Please enter a number for scores.")
            
            students.append({"student_id": student_id, "name": name, "class": class_name, "PE": PE, "Math": Math, "Science": Science})
            print("Student data added successfully.")
        elif submenu_choice == '2':
            break
        else:
            print("The option you entered is not valid.")


def update_data():
    while True:
        print("\n----------Update Menu----------")
        print("1. Update Student Data")
        print("2. Back to Main Menu")
        
        submenu_choice = input("Select the sub-menu: ")
        
        if submenu_choice == '1':
            while True:
                student_id = input("Enter student ID to update: ")
                if student_id.isdigit():
                    student_id = int(student_id)
                    break
                else:
                    print("The option you entered is not valid. Please enter an integer for student ID.")

            for student in students:
                if student['student_id'] == student_id:
                    while True:
                        name = input("Enter new name: ").title()
                        if name.isalpha():
                            break
                        else:
                            print("The option you entered is not valid. Please enter alphabetic characters only for name.")

                    class_name = input("Enter new class: ").upper() 

                    while True:
                        try:
                            PE = float(input("Enter new PE score: "))
                            Math = float(input("Enter new Math score: "))
                            Science = float(input("Enter new Science score: "))
                            break
                        except ValueError:
                            print("The option you entered is not valid. Please enter a number for scores.")

                    student['name'] = name
                    student['class'] = class_name
                    student['PE'] = PE
                    student['Math'] = Math
                    student['Science'] = Science

                    print("Student data updated successfully.")
                    break
            else:
                print("ID not found.")
        elif submenu_choice == '2':
            break
        else:
            print("The option you entered is not valid.")


def delete_data():
    while True:
        print("\n----------Delete Menu----------")
        print("1. Delete Student Data")
        print("2. Back to Main Menu")
        
        submenu_choice = input("Select the sub-menu: ")
        
        if submenu_choice == '1':
            while True:
                student_id = input("Enter student ID to delete: ")
                if student_id.isdigit():
                    student_id = int(student_id)
                    if any(student['student_id'] == student_id for student in students):
                        break  
                    else:
                        print("ID not found. Please try again.")
                else:
                    print("The option you entered is not valid. Please enter an integer for student ID.")

            for student in students:
                if student['student_id'] == student_id:
                    students.remove(student)
                    print("Student data deleted successfully.")
                    break
        elif submenu_choice == '2':
            break
        else:
            print("The option you entered is not valid.")

students = [
    {"student_id": 1, "name": "Tabuti", "class": "5A", "PE": 90.0, "Math": 50.0, "Science": 40.0},
    {"student_id": 2, "name": "Yaya", "class": "5A", "PE": 80.0, "Math": 60.0, "Science": 70.0},
    {"student_id": 3, "name": "Ahmad", "class": "5A", "PE": 85.0, "Math": 75.0, "Science": 65.0},
    {"student_id": 4, "name": "Chikiyo", "class": "5B", "PE": 70.0, "Math": 65.0, "Science": 55.0},
    {"student_id": 5, "name": "Anisa", "class": "5B", "PE": 95.0, "Math": 85.0, "Science": 90.0}
]

menu()
