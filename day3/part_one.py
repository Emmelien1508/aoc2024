import re

# Read file
file = open("inputs/input.txt")
lines = file.readlines()

# Find all do()'s and don't()'s
full_text = ""
for line in lines:
    line = line.replace("\n", "")
    full_text += line

dont_pattern = "don't\\(\\)"
do_pattern = "do\\(\\)"
multiplier_pattern = "mul\\([0-9]+,[0-9]+\\)"

dont_matches = [
    {"dont": (match.start(0), match.end(0))}
    for match in re.finditer(dont_pattern, full_text)
]

do_matches = [
    {"do": (match.start(0), match.end(0))}
    for match in re.finditer(do_pattern, full_text)
]

# Make illegal_indices
# Add dont and do matches to the important indices, but sort by start index
important_indices = do_matches + dont_matches
important_indices = sorted(important_indices, key=lambda d: list(d.values())[0][0])

indices = [True for _ in range(len(full_text))]
for item in important_indices:
    for k, (start, end) in item.items():
        factor = k != "dont"
        indices[start:] = [factor] * len(indices[start:])

multiplier_matches = [
    (match.start(0), match.end(0))
    for match in re.finditer(multiplier_pattern, full_text)
]

number_pattern = "[0-9]+"
scores = []
for match_start_idx, match_end_idx in multiplier_matches:
    if indices[match_start_idx] and indices[match_end_idx]:
        score = 1
        mul = full_text[match_start_idx:match_end_idx]
        result = re.findall(number_pattern, mul)
        for r in result:
            score *= int(r)
        scores.append(score)

print("this is the score")
print(sum(scores))
print()
