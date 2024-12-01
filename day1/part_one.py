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

# Sort columns
left_column.sort()
right_column.sort()

# Calculate distance between them
total_distance = 0
for n1, n2 in zip(left_column, right_column):
    total_distance += abs(n1 - n2)

print("*" * 25)
print("This is the total distance:")
print(total_distance)
print("*" * 25)
