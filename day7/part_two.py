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
            equations = self.write_equation(numbers)
            for equation in equations:
                result = self.evaluate_equation(equation)
                if result == int(value):
                    self.true_equations[value] = numbers

        print()
        print("TRUE EQUATIONS:")
        print(self.true_equations)
        true_values = [int(k) for k in self.true_equations.keys()]
        print("True values:")
        print(sum(true_values))
        print()

    def evaluate_equation(self, equation):
        result = 0
        temporary_result = ""
        operation = "+"

        for item in equation:
            if item.isdigit():
                temporary_result += item
            elif item in ["||", "+", "*"]:
                if temporary_result:
                    if operation == "||":
                        result = int(str(result) + temporary_result)
                    elif operation == "+":
                        result += int(temporary_result)
                    elif operation == "*":
                        result *= int(temporary_result)
                    temporary_result = ""
                operation = item

        # Handle the last number
        if temporary_result:
            if operation == "||":
                result = int(str(result) + temporary_result)
            elif operation == "+":
                result += int(temporary_result)
            elif operation == "*":
                result *= int(temporary_result)

        return result

    def write_equation(self, numbers):
        equations = []

        combinations = self.generate_operation_combinations(numbers)
        for combination in combinations:
            # Put the operation between the numbers
            combined_list = []
            for index in range(len(combination)):
                operation = [numbers[index], combination[index]]
                combined_list.extend(operation)
            combined_list.append(numbers[-1])

            equations.append(combined_list)

        return equations

    def generate_operation_combinations(self, numbers):
        operators = ["*", "+", "||"]
        n = len(numbers) - 1
        combinations = list(itertools.product(operators, repeat=n))

        return combinations


c = Calibrator()
