marks = []
total = 0

print("Enter marks of 5 subjects")

for i in range(5):
    mark = int(input(f"Subject {i+1}: "))
    marks.append(mark)
    total += mark

average = total / 5

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "D"

print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)