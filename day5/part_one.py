def parse_input():
    file = open("inputs/input.txt")
    lines = file.readlines()

    rules = set()
    updates = []

    for line in lines:
        if line == "":
            continue

        line = line.replace("\n", "")

        if "|" in line:
            before, after = line.split("|")
            rules.add((before, after))
        elif "," in line:
            update = line.split(",")
            updates.append(update)

    return rules, updates


def is_valid_update(update, rules):
    # Compare current element with all next elements to see if valid
    for i in range(len(update) - 1):
        for j in range(i + 1, len(update)):
            if (update[i], update[j]) in rules:
                continue

            if (update[j], update[i]) in rules:
                # Order is swapped, so not valid if this is the case
                return False

    return True


def solve(rules, updates):
    invalid_updates = []
    total = 0

    for update in updates:
        if is_valid_update(update, rules):
            invalid_updates.append(update)

            # Get middle index
            middle_index = int((len(update) - 1) / 2)
            total += int(update[middle_index])

    print()
    print("this is the total!")
    print(total)
    print()


rules, updates = parse_input()
solve(rules, updates)
