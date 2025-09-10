'''Task 8: Write a function student_details(**kwargs) 
that accepts name, age, course and prints them.
✅ Test Case:

print(student_details(name="Sunil", age=25, course="Data Analytics"))
# Output: {'name': 'Sunil', 'age': 25, 'course': 'Data Analytics'}'''

def student_details(**kwargs) :
    return kwargs
print(student_details(name="Sunil", age=25, course="Data Analytics"))

        