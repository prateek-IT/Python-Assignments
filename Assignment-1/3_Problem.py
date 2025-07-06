# Write a Python program to input marks for five
#  subjects Physics, Chemistry, Biology, Mathematics,
#  and Computer. Calculate the percentage and grade
#  according to the following:
#  Percentage >= 90% : Grade A
#  Percentage >= 80% : Grade B
#  Percentage >= 70% : Grade C
#  Percentage >= 60% : Grade D
#  Percentage >= 40% : Grade E
#  Percentage < 40% : Grade F


physics = 75
chemistry = 65
biology = 65
mathematics = 85
computer = 95

total_marks = physics + chemistry + biology + mathematics + computer
percentage = (total_marks / 500) * 100

if percentage >= 90 and percentage < 100:
    print("grade A")
elif percentage >= 80 and percentage < 90:
    print("greade B")
elif percentage >= 70 and percentage < 80:
    print("grade C")
elif percentage >= 60 and percentage < 70:
    print("grade D")
elif percentage >= 40 and percentage < 60:
    print("grade E")
elif percentage < 40:
    print("grade F")
    