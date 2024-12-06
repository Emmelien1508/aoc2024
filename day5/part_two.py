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


def order_invalid_update(update, rules):
    # Order invalid update based on the rules

    # Create graph representation
    graph = {page: [] for page in update}

    # Populate the graph based on rules
    for before, after in rules:
        if before in graph and after in graph:
            graph[before].append(after)

    sorted_update = []
    visited_nodes = []

    def dfs(node):
        if node in visited_nodes:
            return

        visited_nodes.append(node)
        for neighbor in graph[node]:
            dfs(neighbor)

        sorted_update.insert(0, node)

    for page in update:
        if page not in visited_nodes:
            dfs(page)

    return sorted_update


def solve(rules, updates):
    invalid_updates = []
    total = 0

    for update in updates:
        if not is_valid_update(update, rules):
            invalid_updates.append(update)
            correct_update = order_invalid_update(update, rules)

            # Get middle index
            middle_index = int((len(correct_update) - 1) / 2)
            total += int(correct_update[middle_index])

    print()
    print("this is the total!")
    print(total)
    print()


rules, updates = parse_input()
solve(rules, updates)
