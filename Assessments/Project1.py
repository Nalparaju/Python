#STUDENT MANAGEMENT SYSTEM

'''
Create a simple student management system using Python that allows users to add, update, delete, and view student records. 
This project will help you apply fundamental programming concepts, including variables, data types, operators, lists, conditional statements, tuples, sets, and loops.'''

#Consider Students as dictionary
Students = {}

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Mark Attendance")
    print("4. View Student Details")
    print("5. Delete Student Record")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        rollNumber = input("Enter roll number: ")
        Students[rollNumber] = {"Name": name, "Marks" : [], "Attendance": set()}
        print("Student added successfully", Students[rollNumber])
    
    elif choice == 2:
        rollNumber = input("Enter student roll number: ")
        if rollNumber in Students:
            marks = list(input("Enter marks of student with comma separated: ").split(","))
            Students[rollNumber]["Marks"].extend(marks)
            print("Marks updated")
        else:
            print("Cant find student, add a student")
    
    elif choice == 3:
        rollNumber = input("Enter roll number: ")
        if rollNumber in Students:
            attendanceDate = input("Enter Attendance Date (YYYY-MM-DD):")
            Students[rollNumber]["Attendance"].add(attendanceDate)
            print("Updated attendance")
        else:
            print("Cant find student")

    elif choice == 4:
        rollNumber = input("Enter roll number: ")
        if rollNumber in Students:
            student = Students[rollNumber]
            tot = 0
            for mark in Students[rollNumber]["Marks"]:
                tot = tot + int(mark)
            avg = tot/len(Students[rollNumber]["Marks"])
            print("Name: ",student["Name"])
            print("Roll number: ", rollNumber)
            print("Marks: ", student["Marks"])
            print("Avg Marks: ", avg)
            print("Attendance: ", student["Attendance"])
        else:
            print("Cant find student")

    elif choice == 5:
        rollNumber = input("Enter roll number: ")
        if rollNumber in Students:
            Students.pop(rollNumber)
            print("Student deleted")
        else:
            print("Unable to find student")
    
    elif choice == 6:
        print("Thank you!! Good Bye")
        break

    else:
        print("try again")
