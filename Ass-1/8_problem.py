#  Write a Python program to calculate the LCM (Least
#  Common Multiple) of two numbers.
#      number1 = 12, number2 = 18
#      LCM of 12 and 18 are: 36
a = 12 
b = 18
lcm = 0
max = a if a > b else b
while True:
    if max % a == 0 and max % b == 0:
        lcm = max
        break
    else:
        max += 1
print(lcm)