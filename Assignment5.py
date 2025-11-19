# TASK 1

student_marks = {"Alice": 85,
                 "Bob": 92,
                 "Charlie": 78,
                 "Diana": 95,
                 "Ethan": 88}

search_name = input("Please enter the student's name to check their marks: ")

if search_name in student_marks:
    marks = student_marks[search_name]
    print(f"{search_name} : {marks}")
else:
    print(f"Student {search_name} was not found.")

# TASK 2

original_list = list(range(1, 11))
print(f"\nOriginal List: {original_list}")

extracted_list = original_list[0:5]
print(f"Extracted List (First Five Elements): {extracted_list}")

reversed_list = extracted_list[::-1]
print(f"Reversed Extracted List: {reversed_list}")