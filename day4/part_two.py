# Read file
file = open("inputs/input.txt")
lines = file.readlines()

# Initialize the matrix
matrix = []

for line in lines:
    line = line.replace("\n", "")
    row = [letter for letter in line]
    matrix.append(row)


xmas_count = 0

# We have to find the word MAS in an X shape:
# Find them relative to each other
# M . S - (x,y)     .           (x+2,y)
# . A . - .         (x+1,y+1)   .
# M . S - (x,y+2)   .           (x+2,y+2)
# -----
# M . M
# . A .
# S . S
# -----
# S . M
# . A .
# S . M
# -----
# S . S
# . A .
# M . M

patterns = [
    ("M", "S", "M", "S"),  # first X-MAS
    ("M", "M", "S", "S"),  # second X-MAS
    ("S", "M", "S", "M"),  # third X-MAS
    ("S", "S", "M", "M"),  # fourth X-MAS
]


def print_matrix_match(matrix):
    print(f"{matrix[i][j]} . {matrix[i+2][j]}")
    print(f". {matrix[i+1][j+1]} .")
    print(f"{matrix[i][j+2]} . {matrix[i+2][j+2]}")


max_row = len(matrix)
max_col = len(matrix[0])

for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        # check if matrix[i][j] is any of the options
        if i + 2 >= max_row or j + 2 >= max_col:
            continue

        if matrix[i + 1][j + 1] != "A":
            continue

        for pattern in patterns:
            if (
                matrix[i][j] == pattern[0]  # This is either M or S
                and matrix[i + 2][j] == pattern[1]  # This is either M or S
                and matrix[i][j + 2] == pattern[2]  # This is either M or S
                and matrix[i + 2][j + 2] == pattern[3]  # This is either M or S
            ):
                xmas_count += 1


print()
print("so many xmas'es are there:")
print(xmas_count)
print()
