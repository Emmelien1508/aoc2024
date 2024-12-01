# Read file
file = open("inputs/input.txt")
lines = file.readlines()

# Initalize columns
left_column = []
right_column = []

for line in lines:
    line = line.replace("\n", "")
    data_array = line.split(" ")

    first_element = int(data_array[0])
    last_element = int(data_array[-1])

    left_column.append(first_element)
    right_column.append(last_element)

# Calculate similarity score
similarity_score = 0
for number in left_column:
    duplicates = sum(item == number for item in right_column)
    similarity_score += number * duplicates

print("*" * 25)
print("This is the similarity score:")
print(similarity_score)
print("*" * 25)
