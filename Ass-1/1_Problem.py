# .Write a program in Python to perform the following
#  operation:
#  If a number is divisible by 3 it should print “SKILLBREW”
#  as a string
#  If a number is divisible by 5 it should print “BRUDITE” as a
#  string
#  If a number is divisible by both 3 and 5 it should print
#  “BRUDITE - NIRVANA” as a string.
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("BRUDITE - NIRVANA")
elif num % 3 == 0:
    print("SKILLBREW")
elif num % 5 == 0:
    print("BRUDITE")
elif num % 3 == 0 and num % 5 == 0:
    print("BRUDITE - NIRVANA")