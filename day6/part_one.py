from enum import Enum


class Direction(Enum):
    # Shows in (x,y) tuple how much to add
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)


class GridPoint:
    def __init__(self, x, y, obstacle=False):
        self.location = (x, y)
        self.obstacle = obstacle

    def __str__(self):
        return f"GP ({self.location[0]},{self.location[1]})"


class Map:
    def __init__(self):
        self.visited_positions = []
        self.direction = Direction.NORTH
        self.starting_position = None
        self.reached_end = False
        self.direction_rotation = [
            Direction.NORTH,
            Direction.EAST,
            Direction.SOUTH,
            Direction.WEST,
        ]

        self.matrix = []

        self.read_file()
        if self.matrix:
            self.solve()

    def read_file(self):
        file = open("inputs/input.txt")
        lines = file.readlines()
        full_text = "".join(line for line in lines)

        # Transpose the matrix so that x & y are doable
        lines = full_text.split("\n")

        rows = len(lines)
        cols = len(lines[0])

        transposed = []
        for col in range(cols):
            new_row = [lines[row][col] for row in range(rows)]
            transposed.append(new_row)

        for i, row in enumerate(transposed):
            self.matrix.insert(i, [])
            for j, col in enumerate(row):
                self.matrix[i].append(GridPoint(i, j, col == "#"))

                if col == "^":
                    self.starting_position = (i, j)

        max_rows = len(self.matrix) - 1
        max_cols = len(self.matrix[0]) - 1
        self.max_position = (max_rows, max_cols)
        self.min_position = (0, 0)

    def solve(self):
        self.current_position = self.starting_position

        # While you haven't reached the end:
        while not self.has_reached_end():
            # Fake add to your current position based on the direction
            new_x = self.current_position[0] + self.direction.value[0]
            new_y = self.current_position[1] + self.direction.value[1]

            # Check if that new location is an obstacle
            if self.matrix[new_x][new_y].obstacle:
                # Rotate directions
                idx = self.direction_rotation.index(self.direction)
                if idx < len(self.direction_rotation) - 1:
                    self.direction = self.direction_rotation[idx + 1]
                else:
                    self.direction = self.direction_rotation[0]
            else:
                # Real add to current position
                self.current_position = (new_x, new_y)
                if self.current_position not in self.visited_positions:
                    self.visited_positions.append(self.current_position)

        print("Ending at:")
        print(self.current_position)
        print("with so many distinctive steps:")
        print(len(self.visited_positions))
        print()

    def has_reached_end(self):
        # Checks if you reached the end
        return any(
            [
                self.current_position[0] >= self.max_position[0],
                self.current_position[1] >= self.max_position[1],
                self.current_position[0] <= self.min_position[0],
                self.current_position[1] <= self.min_position[1],
            ]
        )


m = Map()
