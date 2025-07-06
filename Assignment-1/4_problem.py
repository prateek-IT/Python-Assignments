# Write a Python program to find the sum of all odd
# numbers between two given numbers. 
#      Start = 1, stop = 10
#      Sum of odd numbers: 25

start = 1
stop = 10
sum_of_odds = 0 
for i in range(start, stop + 1):
    if i % 2 != 0:
        sum_of_odds = sum_of_odds + i
print(f"Sum of odd numbers: {sum_of_odds}")