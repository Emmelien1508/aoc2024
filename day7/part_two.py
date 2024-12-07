import itertools


class Calibrator:
    def __init__(self):
        self.true_equations = {}
        self.equations = {}

        self.read_file()
        self.evaluate_equations()

    def read_file(self):
        file = open("inputs/test.txt")
        lines = file.readlines()

        for line in lines:
            line = line.replace("\n", "")
            value, numbers = line.split(": ")
            numbers = numbers.split(" ")
            self.equations[value] = numbers

    def evaluate_equations(self):
        for value, numbers in self.equations.items():
            # We can put a + or * between the numbers
            if value == "7290":
                equations = self.write_equation(numbers)
                for equation in equations:
                    eq = self.evaluate_expression(equation)
                    print(eq)
                    print("----")
                    print()
                # print("Value:", value)
                # print("These are the numbers:", numbers)
                # for e in equations:
                #     print(f"Eval eq: {e} = {eval(e)}")
                #     print(eval(e) == int(value))
                #     if eval(e) == int(value):
                #         self.true_equations[value] = numbers
                print("***")
                print()
                # if eval(equation) == int(value):
                #     self.true_equations[value] = numbers

        # print()
        # print("TRUE EQUATIONS:")
        # print(self.true_equations)
        # # true_values = [int(k) for k in self.true_equations.keys()]
        # print()

    def evaluate_expression(self, expr):
        result = 0
        temporary_result = ""
        equation = ""

        print("We start with:")
        print(expr)
        # The temporary result is a buildup of previous operations
        for item in expr:
            if item.isdigit():
                temporary_result += item
                equation += item

            elif item == "||":
                # if there is no result yet, just add the temporary result
                if result == 0:
                    result += int(temporary_result)
                else:
                    # Concatenate the temp + current result
                    result = int(str(result) + temporary_result)

                # After handling concatenation, make temporary result empty again
                temporary_result = ""
                equation += " || "

            elif item in ["*", "+"]:
                if temporary_result:
                    # Is this even possible?
                    if result == 0:
                        result = int(temporary_result)
                    else:
                        if item == "+":
                            result += int(temporary_result)
                        elif item == "*":
                            result *= int(temporary_result)

                    # After handling + or *, make temporary result empty again
                    temporary_result = ""
                equation += f" {item} "

            print(f"Current step: {equation} (Result: {result})")

        # Handle the last number if there is one
        if temporary_result:
            if result == 0:
                result = int(temporary_result)
            else:
                result = int(str(result) + temporary_result)

        return result

    def write_equation(self, numbers):
        equations = []

        combinations = self.generate_operation_combinations(numbers)
        for combination in combinations:
            c = len(combination)
            combined_list = []
            for index in range(c):
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
