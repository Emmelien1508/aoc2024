import numpy as np
import re


def get_rows(matrix):
    return ["".join([col for col in row]) for row in matrix]


def get_cols(matrix):
    t_matrix = np.transpose(matrix)
    return ["".join([col for col in row]) for row in t_matrix]


def get_diagonals(matrix):
    # Min k = -10 and max k = 10
    min_k = -1 * len(matrix)
    max_k = len(matrix)
    diagonals = []
    # This only does it from BL to TR
    for k in range(min_k + 1, max_k):
        d = np.diag(matrix, k)
        # If d is < 4, skip it cuz its not interesting
        if len(d) >= 4:
            diagonals.append("".join(d))

    # We should also do from TL to BR
    # Reverse each row
    t_matrix = matrix[:, ::-1]
    for k in range(min_k + 1, max_k):
        d = np.diag(t_matrix, k)
        if len(d) >= 4:
            diagonals.append("".join(d))
    return diagonals


# Read file
file = open("inputs/input.txt")
lines = file.readlines()

# Initialize the matrix
matrix = []

# Find XMAS horizontal, vertical, diagonal, written backwards, or even overlapping other words.
for line in lines:
    line = line.replace("\n", "")
    row = [letter for letter in line]
    matrix.append(row)

matrix = np.array(matrix)

xmas_count = 0

# Find XMAS with regex
word = "XMAS"
reverse_word = word[::-1]
pattern = f"(?=({word}|{reverse_word}))"

for d in get_diagonals(matrix):
    matches = re.findall(pattern, d)
    if matches:
        xmas_count += len(matches)

for c in get_cols(matrix):
    matches = re.findall(pattern, c)
    if matches:
        xmas_count += len(matches)

for r in get_rows(matrix):
    matches = re.findall(pattern, r)
    if matches:
        xmas_count += len(matches)

print()
print("so many xmas'es are there:")
print(xmas_count)
print()
