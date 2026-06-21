import sys #boolen example
sys.stdout.reconfigure(encoding='utf-8')

# এরপর আপনার বাকি কোড লিখুন
is_sunny = True

if is_sunny:
    print("ছাতা নিয়ে বাইরে যান।")
else:
    print("ছাতা লাগবে না।")

#oprerattors example and boolean example.
#Both condition must be True to get a true result
is_student = True
has_good_grades = True
if is_student and has_good_grades:
    print("You are the eligible for the scholarsh!")
else:
    print("You are not eligible for the scholarship.:")


#Only one condition must be True to get a true result
    student_has_card = True
    student_has_cash = False
    if student_has_card or student_has_cash:
        print("You can buy lunch.")

    else:
        print("You cannot buy lunch.")

#Only one condition must be True to get a true result
student_has_card = True
student_has_cash = False
if student_has_card or student_has_cash:
    print("You can buy lunch.")

else:
    print("You cannot buy lunch.")

# Tt turns True to False and False to True
is_raining = False
if not is_raining:
    print("You can go outside without an umbrella.")
else:
    print("You should take an umbrella with you.")
    

# Membership operators example
my_skills = ["python", "SQl", "data analysis"]

# checking if 'python' is in the list
if "python" in my_skills:
    print("You have python skills.")
else:
    print("You do not have python skills.")


# conditional statements ( if, elif, else) example
score = 75
if score >= 80:
    print("You got an A+")
elif score >=70:
    print(" You got an A")
elif score >= 60:
    print("You got a B")
elif score >= 50:
    print("You got a c")
elif score >= 40:
    print("You got a D")
else:
    print("You got an F")

# Take 3 task in chatgpt and write code for it
#Ticket pricing(Using if-else and comparison oprerators)
age = 18
if age >= 18:
    print("Adult ticket price is $10.")
else:
    print("child ticket price is $5.")

#Take 2
#Login system(using and operatior)
username = "admin"
password = "11234"
if username == "admin" and password == "11234":
    print("login successful.")
else:
    print("Invalid Credentiasls.")

#task 3
#Grading Assistant(using if-elif-else)
score = 45
if score >= 80:
    print("Excellent")
elif score >=50 and score <=79: #elef 50<=score<=79:
    print("Good")
else:
    print("Needs Improvement")


# practice averything befor practicing loops

# variables and data types example
# Variables storing different data types
name = "Alice" #string(str)
age = 30 #integer (int)
height = 1.75 #floating point (float)
is_student = True #boolean (bool)
print("Name:", name)
print("Age:d", age)
print("Height:", height)
print(" Is student:" , is_student)
