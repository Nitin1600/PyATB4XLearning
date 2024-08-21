# result = max(5, 3, 2)
# print(result)

"""
(Q)Grade Calculator:
>Write a programe that calculates and displays the letter grade for a given numerical score:
#A:(90-100).
#B:(80-89).
#C:(70-79).
#D:(60-69).
#F:(0-59).

"""

score = float(input("Enter your score:\n"))

if score >= 90 and score <= 100:
    print("Your grade is A")
elif score >= 80 and score <= 89:
    print("Your gade is B")
elif score >= 70 and score <= 79:
    print("Your grade is C")
elif score >= 60 and score <= 69:
    print("Yor grade is D")
elif score > 100:
     print("This score is not valid!")
else:
     grade = "F"
     print("Your grade is", grade)
# elif score >= 0 and score <= 59:
#     print("Your grade is F")
