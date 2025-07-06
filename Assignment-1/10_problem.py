# Write a Python program to reverse the order of
#  words in a given sentence.
#   Input_sentence = “Hello, World! Welcome to Python
#  programming.”
#      Output after reverse = “programming. Python to Welcome
#  World! Hello,”
string = "prateek singh"
word = string.split()
reversed_string = " ".join(reversed(word))
print(reversed_string)