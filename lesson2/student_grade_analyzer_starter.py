
# =====================================================================
#  Classify a Grade
# =====================================================================
def classify_grade(grade):
    
    if grade >= 90:
        return ("Excellent", "Passed")
    elif grade >= 85:
        return ("Very Good", "Passed")
    elif grade >= 80:
        return ("Good", "Passed")
    elif grade >= 75:
        return ("Satisfactory", "Passed")
    else:
        return ("Needs Improvement", "Failed")


# =====================================================================
# Load and Validate the Records
# =====================================================================
def load_students(filename):
    
    students = []
    
    try:
        
        with open(filename, "r", encoding="utf-8") as file_handle:
            for line in file_handle:
               
                clean_line = line.strip()
                if len(clean_line) == 0:
                    continue
                
                
                parts = clean_line.split(",")
                if len(parts) != 3:
                    continue
                
                try:
                   
                    grade = float(parts[2])
                    if grade >= 0 and grade <= 100:
                        
                        record = {"student_id": parts[0], "name": parts[1], "grade": grade}
                        students.append(record)
                except:
                   
                    continue
                    
    except FileNotFoundError:
        print("Error: The file %s cannot be opened." % filename)
        
    return students


# =====================================================================
#  Analyze the Class
# =====================================================================
def calculate_statistics(students):
   
    if not students:
        return None

   
    total_grade = 0
    passed_count = 0
    failed_count = 0
    
    
    highest_student = students[0]
    lowest_student = students[0]
    count = 0

    
    for student in students:
        count = count + 1
        total_grade = total_grade + student["grade"]
        
        classification, status = classify_grade(student["grade"])
        
        if status == "Passed":
            passed_count = passed_count + 1
        else:
            failed_count = failed_count + 1
            
        if student["grade"] > highest_student["grade"]:
            highest_student = student
            
        if student["grade"] < lowest_student["grade"]:
            lowest_student = student

    
    average = total_grade / count

    
    statistics = {
        "count": count,
        "average": average,
        "passed": passed_count,
        "failed": failed_count,
        "highest": highest_student,
        "lowest": lowest_student
    }
    
    return statistics


# =====================================================================
#  Display All Students
# =====================================================================
def display_students(students):
   
    print("ID         | Name            | Grade  | Classification     | Status")
    print("---------------------------------------------------------------------")
    
    
    for student in students:
        classification, status = classify_grade(student["grade"])
        
       
        short_name = student["name"][:15]
        
        
        print("%s | %s | %.2f  | %s | %s" % (
            student["student_id"], 
            short_name, 
            student["grade"], 
            classification, 
            status
        ))



def display_statistics(statistics):
    
    if not statistics:
        print("No statistics available.")
        return
        
    print("\nCLASS STATISTICS")
    print("Number of students: %d" % statistics["count"])
    print("Class average: %.2f" % statistics["average"])
    print("Passed: %d" % statistics["passed"])
    print("Failed: %d" % statistics["failed"])
    
    highest = statistics["highest"]
    lowest = statistics["lowest"]
    print("Highest: %s - %.2f" % (highest["name"], highest["grade"]))
    print("Lowest: %s - %.2f" % (lowest["name"], lowest["grade"]))


# =====================================================================
#  Search for a Student
# =====================================================================
def search_student(students, keyword):
    
    matches = []
    
    
    clean_keyword = keyword.lower().strip()

    
    for student in students:
        name_lower = student["name"].lower()
        id_lower = student["student_id"].lower()
        
        if clean_keyword in name_lower or clean_keyword in id_lower:
            matches.append(student)

    return matches


# =====================================================================
#  Save the Report
# =====================================================================
def save_report(students, statistics, filename):
    
    if not students or not statistics:
        print("No data to save.")
        return

    try:
        
        with open(filename, "w", encoding="utf-8") as file_handle:
            file_handle.write("STUDENT GRADE REPORT\n")
            file_handle.write("==============================\n\n")
            
            
            for student in students:
                classification, status = classify_grade(student["grade"])
                line = "%s - %s: %.2f (%s / %s)\n" % (
                    student["student_id"], 
                    student["name"], 
                    student["grade"], 
                    classification, 
                    status
                )
                file_handle.write(line)
                
           
            file_handle.write("\nCLASS STATISTICS\n")
            file_handle.write("------------------------------\n")
            file_handle.write("Class average: %.2f\n" % statistics["average"])
            file_handle.write("Passed: %d\n" % statistics["passed"])
            file_handle.write("Failed: %d\n" % statistics["failed"])
            
            highest = statistics["highest"]
            lowest = statistics["lowest"]
            file_handle.write("Highest: %s (%.2f)\n" % (highest["name"], highest["grade"]))
            file_handle.write("Lowest: %s (%.2f)\n" % (lowest["name"], lowest["grade"]))
            
        print("Report successfully saved to %s" % filename)
        
    except OSError:
        # Handle a possible OSError as requested by starter code
        print("Error: Could not write to the file %s" % filename)


# =====================================================================
#  Complete the Menu
# =====================================================================
def main():
    
    students = load_students("grades.txt")

    if not students:
        print("No valid student records were loaded.")
        return

    statistics = calculate_statistics(students)

    
    while True:
        print("\nSTUDENT GRADE ANALYZER")
        print("[1] Display all students")
        print("[2] Display class statistics")
        print("[3] Search for a student")
        print("[4] Save report")
        print("[5] Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_students(students)
        elif choice == "2":
            display_statistics(statistics)
        elif choice == "3":
            keyword = input("Enter student name or ID to search: ")
            matches = search_student(students, keyword)
            if len(matches) > 0:
                print("\nSearch Results:")
                display_students(matches)
            else:
                print("No students found.")
        elif choice == "4":
            save_report(students, statistics, "grade_report.txt")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
            continue


if __name__ == "__main__":
    main()