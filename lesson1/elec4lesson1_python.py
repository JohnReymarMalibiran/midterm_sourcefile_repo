import sys
# Define scores as individual variables
score1 = 85
score2 = 72
score3 = 91
score4 = 64
score5 = 78

print("Student Scores:")
print(score1)
print(score2)
print(score3)
print(score4)
print(score5)
print()

passed_count = 0
failed_count = 0

# Evaluate Student 1
if score1 >= 90:
    print("Student 1: " + str(score1) + " - Excellent - Passed")
    passed_count = passed_count + 1
elif score1 >= 80:
    print("Student 1: " + str(score1) + " - Very Good - Passed")
    passed_count = passed_count + 1
elif score1 >= 75:
    print("Student 1: " + str(score1) + " - Good - Passed")
    passed_count = passed_count + 1
else:
    print("Student 1: " + str(score1) + " - Failed")
    failed_count = failed_count + 1

# Evaluate Student 2
if score2 >= 90:
    print("Student 2: " + str(score2) + " - Excellent - Passed")
    passed_count = passed_count + 1
elif score2 >= 80:
    print("Student 2: " + str(score2) + " - Very Good - Passed")
    passed_count = passed_count + 1
elif score2 >= 75:
    print("Student 2: " + str(score2) + " - Good - Passed")
    passed_count = passed_count + 1
else:
    print("Student 2: " + str(score2) + " - Failed")
    failed_count = failed_count + 1

# Evaluate Student 3
if score3 >= 90:
    print("Student 3: " + str(score3) + " - Excellent - Passed")
    passed_count = passed_count + 1
elif score3 >= 80:
    print("Student 3: " + str(score3) + " - Very Good - Passed")
    passed_count = passed_count + 1
elif score3 >= 75:
    print("Student 3: " + str(score3) + " - Good - Passed")
    passed_count = passed_count + 1
else:
    print("Student 3: " + str(score3) + " - Failed")
    failed_count = failed_count + 1

# Evaluate Student 4
if score4 >= 90:
    print("Student 4: " + str(score4) + " - Excellent - Passed")
    passed_count = passed_count + 1
elif score4 >= 80:
    print("Student 4: " + str(score4) + " - Very Good - Passed")
    passed_count = passed_count + 1
elif score4 >= 75:
    print("Student 4: " + str(score4) + " - Good - Passed")
    passed_count = passed_count + 1
else:
    print("Student 4: " + str(score4) + " - Failed")
    failed_count = failed_count + 1

# Evaluate Student 5
if score5 >= 90:
    print("Student 5: " + str(score5) + " - Excellent - Passed")
    passed_count = passed_count + 1
elif score5 >= 80:
    print("Student 5: " + str(score5) + " - Very Good - Passed")
    passed_count = passed_count + 1
elif score5 >= 75:
    print("Student 5: " + str(score5) + " - Good - Passed")
    passed_count = passed_count + 1
else:
    print("Student 5: " + str(score5) + " - Failed")
    failed_count = failed_count + 1

# Calculate Total and Average
total_score = score1 + score2 + score3 + score4 + score5
average_score = total_score / 5

# Determine Highest Score using sequential if statements
highest_score = score1
if score2 > highest_score:
    highest_score = score2
if score3 > highest_score:
    highest_score = score3
if score4 > highest_score:
    highest_score = score4
if score5 > highest_score:
    highest_score = score5

# Determine Lowest Score using sequential if statements
lowest_score = score1
if score2 < lowest_score:
    lowest_score = score2
if score3 < lowest_score:
    lowest_score = score3
if score4 < lowest_score:
    lowest_score = score4
if score5 < lowest_score:
    lowest_score = score5

# Print Final Statistics
print()
print("Total Score:", total_score)
print("Average Score:", int(average_score))
print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)
print("Passed:", passed_count)
print("Failed:", failed_count)