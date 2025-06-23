#  Write a Python program to reverse a number using
#  a while loop.
#      Sample Input: num = 12345
#      Sample Output: revnum = 54321
num = 4321
reversed = 0
while num > 0:
    digit = num % 10
    reversed = reversed * 10 + digit
    num //= 10
print(reversed) 
