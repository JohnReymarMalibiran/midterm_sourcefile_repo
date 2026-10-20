# Raw records with the required valid students and invalid test cases included
raw_records = [
    "Ana,88,92,90",
    "Ben,70,72,74",
    "Cara,95,91,94",
    "Dan,78,80,76",
    "Ella,85,89,87",
    "Fred,90,85",          # Invalid (missing score)
    "Gina",                # Invalid (only name)
    "Henry,90,eighty,85",  # Invalid (text instead of number)
    "Ivy,"                 # Invalid (blank scores)
]

PASSING_GRADE = 75
student_scores = {}

# PART A & F: Parse and organize the records 
for record in raw_records:
    fields = record.split(",")
    
    
    if len(fields) != 4:
        print(f"Skipped invalid record: {record}")
        continue
    
    name = fields[0]
    
    
    try:
        scores = [int(fields[1]), int(fields[2]), int(fields[3])]
        student_scores[name] = scores
    except ValueError:
        print(f"Skipped invalid record: {record}")
        continue

# PART B: Display records alphabetically
print("\nORGANIZED STUDENT RECORDS")
for name in sorted(student_scores.keys()):
    print(f"{name}: {student_scores[name]}")

# PART C: Calculate the student results
ranking = []
passed_count = 0
failed_count = 0
sum_of_averages = 0


for name, scores in student_scores.items():
    if len(scores) == 0:
        continue
        
    total = sum(scores)
    average = total / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)
    
    if average >= PASSING_GRADE:
        remark = "Passed"
        passed_count += 1
    else:
        remark = "Failed"
        failed_count += 1
        
    sum_of_averages += average
   
    ranking_tuple = (average, name, highest_score, lowest_score, remark)
    ranking.append(ranking_tuple)

# PART D: Sort and display the ranking

ranking.sort(reverse=True) 

print("\nSTUDENT GRADE REPORT")
print(f"{'Rank':<6}{'Name':<7}{'Average':<9}{'Highest':<9}{'Lowest':<8}{'Remark'}")

for rank_num, (avg, name, high, low, remark) in enumerate(ranking, start=1):
   
    print(f"{rank_num:<6}{name:<7}{avg:<9.2f}{high:<9}{low:<8}{remark}")

# PART E: Display the class summary
total_students = len(ranking)
class_average = sum_of_averages / total_students


highest_student = ranking[0]
lowest_student = ranking[-1]

print("\nCLASS SUMMARY")
print(f"Number of Students: {total_students}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Class Average: {class_average:.2f}")
print(f"Highest: {highest_student[1]} - {highest_student[0]:.2f}")
print(f"Lowest: {lowest_student[1]} - {lowest_student[0]:.2f}")