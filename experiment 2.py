
print("STUDENT GRADE CALCULATOR")

total = 0

for i in range(1, 6):
    marks = int(input("Enter marks for subject " + str(i) + ": "))

    if marks < 0 or marks > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        continue

    total += marks

average = total / 5

print("\nTotal Marks:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A+")
elif average >= 80:
    print("Grade: A")
elif average >= 70:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 50:
    print("Grade: D")
else:
    print("Grade: F")

print("\nCountdown:")
count = 5

while count > 0:
    print(count)
    count -= 1

print("Program completed!")

