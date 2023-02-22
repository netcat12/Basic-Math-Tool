import math

class MathTool:
    GREEN = '\033[92m'
    BOLD = '\033[1m'
    END = '\033[0m'

    def __init__(self):
        print(f"{self.GREEN}{self.BOLD}===============================")
        print("=      Welcome to MathTool    =")
        print("=           Made by Asif      =")
        print("==============================={self.END}")

    def get_user_choice(self):
        print("What would you like to do?")
        print("1. Find the square root of a number")
        print("2. Solve an algebraic expression using formula")
        print("3. Calculate a logarithm")

        choice = int(input("Enter your choice (1/2/3): "))
        return choice

    def get_number(self, prompt):
        return float(input(prompt))

    def get_formula(self):
        formula = input("Enter the formula: ")
        return formula

    def square_root(self):
        num = self.get_number("Enter a number: ")
        result = math.sqrt(num)
        print(f"The square root of {num} is {result}")

    def solve_algebra(self):
        formula = self.get_formula()
        vars = formula.split(' ')
        for i, var in enumerate(vars):
            if var.isalpha():
                val = self.get_number(f"Enter the value of {var}: ")
                vars[i] = str(val)
        formula = ' '.join(vars)
        result = eval(formula)
        print(f"The result of the formula {formula} is {result}")

    def calculate_logarithm(self):
        base = self.get_number("Enter the base: ")
        num = self.get_number("Enter the number: ")
        result = math.log(num, base)
        print(f"The logarithm of {num} to the base {base} is {result}")

    def run(self):
        while True:
            choice = self.get_user_choice()

            if choice == 1:
                self.square_root()
            elif choice == 2:
                self.solve_algebra()
            elif choice == 3:
                self.calculate_logarithm()
            else:
                print("Invalid choice. Please choose a valid option.")

            # Prompt the user to continue or quit
            answer = input("Do you want to continue (Y/N)? ")
            if answer.lower() != 'y':
                print(f"{self.GREEN}Goodbye!{self.END}")
                break

if __name__ == "__main__":
    math_tool = MathTool()
    math_tool.run()
