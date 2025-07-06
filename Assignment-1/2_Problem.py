# Write a program that accepts a string as input from
#  the user and calculates the number of digits and
#  letters.
#      Input: Hello123 
#      Output: Alphabets: 5 & Number : 3 

alpha = 0
number = 0
for i in list("Brudite"):
    if i.isalpha():
       alpha += 1
    elif i.isnumeric():
       number += 1
print(f"total alphabets: {alpha} & total numbers:{number}")
