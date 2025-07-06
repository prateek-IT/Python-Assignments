# Write a Python program to count the frequency of
#  each element in a list.
#      Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
#      Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}
input_list = [4, 3, 2, 2, 1,]
frequ_count = {}
for element in input_list:
    if element in frequ_count:
        frequ_count[element] += 1
    else:
        frequ_count[element] = 1
print(frequ_count)