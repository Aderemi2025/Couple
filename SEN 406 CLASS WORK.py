# Program to count male and female students

male = 0
female = 0

# Number of students
students = int(input("Enter number of students: "))

for i in range(students):
    gender = input("Enter gender (M/F): ").upper()

    if gender == "M":
        male += 1
    elif gender == "F":
        female += 1
    else:
        print("Invalid input")

print("\nClass Summary")
print("Male Students:", male)
print("Female Students:", female)

# Compare numbers
if male < female:
    print("Males are fewer than females.")
elif female < male:
    print("Females are fewer than males.")
else:
    print("Number of males and females are equal.")