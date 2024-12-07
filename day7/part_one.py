import itertools


class Calibrator:
    def __init__(self):
        self.true_equations = {}
        self.equations = {}

        self.read_file()
        self.evaluate_equations()

    def read_file(self):
        file = open("inputs/input.txt")
        lines = file.readlines()

        for line in lines:
            line = line.replace("\n", "")
            value, numbers = line.split(": ")
            numbers = numbers.split(" ")
            self.equations[value] = numbers

    def evaluate_equations(self):
        for value, numbers in self.equations.items():
            # We can put a + or * between the numbers
            combinations = self.generate_operation_combinations(numbers)
            for combination in combinations:
                combined_list = ["(" for _ in range(len(numbers) - 2)]
                for index in range(len(combination)):
                    if index == 0:
                        operation = [numbers[index], combination[index]]
                    else:
                        operation = [numbers[index], ")", combination[index]]
                    combined_list.extend(operation)
                combined_list.append(numbers[-1])
                equation = "".join(combined_list)

                if eval(equation) == int(value):
                    self.true_equations[value] = numbers
        print()
        print("TRUE EQUATIONS:")
        print(self.true_equations)
        print("This is the sum of true equation values:")
        true_values = [int(k) for k in self.true_equations.keys()]
        print(sum(true_values))
        print()

    def generate_operation_combinations(self, numbers):
        operators = ["*", "+"]
        n = len(numbers) - 1
        combinations = list(itertools.product(operators, repeat=n))

        return combinations


c = Calibrator()
