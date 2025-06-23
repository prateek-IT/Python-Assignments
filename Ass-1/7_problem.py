#  Write a Python program to check if a string is an
#  anagram of another string.
#      string1 = "listen", string2 = "silent"
#      Output: True
str1 = "prateek"
str2 = "teekpar"

sorted(str1)
sorted(str2)

if sorted(str1) == sorted(str2):
    print("it is an anagrams")