import sys
import math
import argparse
from colorama import init, Fore, Style

init(autoreset=True)

class Calculator:
    def __init__(self):
        self.history = []

    def log(self, entry):
        self.history.append(entry)
        with open('calc_history.log', 'a') as f:
            f.write(entry + '\n')

    def show_history(self):
        print(Fore.YELLOW + "\n--- Operation History ---")
        for entry in self.history:
            print(entry)
        print(Fore.YELLOW + "------------------------\n")

class SimpleCalculator(Calculator):
    def add(self, a, b):
        result = a + b
        self.log(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.log(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.log(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        try:
            result = a / b
            self.log(f"{a} / {b} = {result}")
            return result
        except ZeroDivisionError:
            self.log(f"{a} / {b} = Error (division by zero)")
            raise ValueError("Division by zero is not allowed.")

class ScientificCalculator(SimpleCalculator):
    def sin(self, x):
        result = math.sin(x)
        self.log(f"sin({x}) = {result}")
        return result

    def cos(self, x):
        result = math.cos(x)
        self.log(f"cos({x}) = {result}")
        return result

    def tan(self, x):
        result = math.tan(x)
        self.log(f"tan({x}) = {result}")
        return result

    def asin(self, x):
        result = math.asin(x)
        self.log(f"asin({x}) = {result}")
        return result

    def acos(self, x):
        result = math.acos(x)
        self.log(f"acos({x}) = {result}")
        return result

    def atan(self, x):
        result = math.atan(x)
        self.log(f"atan({x}) = {result}")
        return result

    def radians(self, x):
        result = math.radians(x)
        self.log(f"radians({x}) = {result}")
        return result

    def degrees(self, x):
        result = math.degrees(x)
        self.log(f"degrees({x}) = {result}")
        return result

    def log(self, x, base=math.e):
        result = math.log(x, base)
        self.log(f"log base {base} ({x}) = {result}")
        return result

    def log10(self, x):
        result = math.log10(x)
        self.log(f"log10({x}) = {result}")
        return result

    def pow(self, x, y):
        result = math.pow(x, y)
        self.log(f"{x} ^ {y} = {result}")
        return result

    def exp(self, x):
        result = math.exp(x)
        self.log(f"exp({x}) = {result}")
        return result

    def sqrt(self, x):
        result = math.sqrt(x)
        self.log(f"sqrt({x}) = {result}")
        return result

    def factorial(self, x):
        result = math.factorial(x)
        self.log(f"factorial({x}) = {result}")
        return result

    def pi(self):
        self.log(f"pi = {math.pi}")
        return math.pi

    def e(self):
        self.log(f"e = {math.e}")
        return math.e

def parse_args():
    parser = argparse.ArgumentParser(description="Advanced Calculator CLI App")
    parser.add_argument('--mode', choices=['simple', 'scientific'], help='Calculator mode')
    return parser.parse_args()

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")

def main():
    args = parse_args()
    mode = args.mode or 'simple'
    calc = ScientificCalculator() if mode == 'scientific' else SimpleCalculator()
    print(Fore.CYAN + f"\nWelcome to the Advanced Calculator! Mode: {mode.capitalize()}")
    while True:
        print(Fore.GREEN + "\nSelect operation:")
        if isinstance(calc, ScientificCalculator):
            print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Sin\n6. Cos\n7. Tan\n8. Radians\n9. Degrees\n10. Log\n11. Log10\n12. Power\n13. Exp\n14. Sqrt\n15. Factorial\n16. Pi\n17. e\n18. Asin\n19. Acos\n20. Atan\n21. Show History\n22. Switch Mode\n0. Exit")
        else:
            print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Show History\n6. Switch Mode\n0. Exit")
        choice = input(Fore.YELLOW + "\nEnter choice: ").strip()
        try:
            if choice == '0':
                confirm = input(Fore.YELLOW + "Are you sure you want to exit? (y/n): ").lower()
                if confirm == 'y':
                    print(Fore.CYAN + "Goodbye!")
                    break
                continue
            if isinstance(calc, ScientificCalculator):
                if choice == '1':
                    a, b = get_float('a: '), get_float('b: ')
                    print(Fore.BLUE + f"Result: {calc.add(a, b)}")
                elif choice == '2':
                    a, b = get_float('a: '), get_float('b: ')
                    print(Fore.BLUE + f"Result: {calc.subtract(a, b)}")
                elif choice == '3':
                    a, b = get_float('a: '), get_float('b: ')
                    print(Fore.BLUE + f"Result: {calc.multiply(a, b)}")
                elif choice == '4':
                    a, b = get_float('a: '), get_float('b: ')
                    try:
                        print(Fore.BLUE + f"Result: {calc.divide(a, b)}")
                    except ValueError as e:
                        print(Fore.RED + str(e))
                elif choice == '5':
                    x = get_float('x (radians): ')
                    print(Fore.BLUE + f"Result: {calc.sin(x)}")
                elif choice == '6':
                    x = get_float('x (radians): ')
                    print(Fore.BLUE + f"Result: {calc.cos(x)}")
                elif choice == '7':
                    x = get_float('x (radians): ')
                    print(Fore.BLUE + f"Result: {calc.tan(x)}")
                elif choice == '8':
                    x = get_float('x (degrees): ')
                    print(Fore.BLUE + f"Result: {calc.radians(x)}")
                elif choice == '9':
                    x = get_float('x (radians): ')
                    print(Fore.BLUE + f"Result: {calc.degrees(x)}")
                elif choice == '10':
                    x = get_float('x: ')
                    base = get_float('base (default e): ') if input('Custom base? (y/n): ').lower() == 'y' else math.e
                    print(Fore.BLUE + f"Result: {calc.log(x, base)}")
                elif choice == '11':
                    x = get_float('x: ')
                    print(Fore.BLUE + f"Result: {calc.log10(x)}")
                elif choice == '12':
                    x, y = get_float('x: '), get_float('y: ')
                    print(Fore.BLUE + f"Result: {calc.pow(x, y)}")
                elif choice == '13':
                    x = get_float('x: ')
                    print(Fore.BLUE + f"Result: {calc.exp(x)}")
                elif choice == '14':
                    x = get_float('x: ')
                    print(Fore.BLUE + f"Result: {calc.sqrt(x)}")
                elif choice == '15':
                    x = int(get_float('x (integer): '))
                    print(Fore.BLUE + f"Result: {calc.factorial(x)}")
                elif choice == '16':
                    print(Fore.BLUE + f"Result: {calc.pi()}")
                elif choice == '17':
                    print(Fore.BLUE + f"Result: {calc.e()}")
                elif choice == '18':
                    x = get_float('x: ')
                    print(Fore.BLUE + f"Result: {calc.asin(x)}")
                elif choice == '19':
                    x = get_float('x: ')
                    print(Fore.BLUE + f"Result: {calc.acos(x)}")
                elif choice == '20':
                    x = get_float('x: ')
                    print(Fore.BLUE + f"Result: {calc.atan(x)}")
                elif choice == '21':
                    calc.show_history()
                elif choice == '22':
                    mode = 'simple' if mode == 'scientific' else 'scientific'
                    calc = ScientificCalculator() if mode == 'scientific' else SimpleCalculator()
                    print(Fore.CYAN + f"Switched to {mode.capitalize()} mode.")
                else:
                    print(Fore.RED + "Invalid choice.")
            else:
                if choice == '1':
                    a, b = get_float('a: '), get_float('b: ')
                    print(Fore.BLUE + f"Result: {calc.add(a, b)}")
                elif choice == '2':
                    a, b = get_float('a: '), get_float('b: ')
                    print(Fore.BLUE + f"Result: {calc.subtract(a, b)}")
                elif choice == '3':
                    a, b = get_float('a: '), get_float('b: ')
                    print(Fore.BLUE + f"Result: {calc.multiply(a, b)}")
                elif choice == '4':
                    a, b = get_float('a: '), get_float('b: ')
                    try:
                        print(Fore.BLUE + f"Result: {calc.divide(a, b)}")
                    except ValueError as e:
                        print(Fore.RED + str(e))
                elif choice == '5':
                    calc.show_history()
                elif choice == '6':
                    mode = 'scientific' if mode == 'simple' else 'simple'
                    calc = ScientificCalculator() if mode == 'scientific' else SimpleCalculator()
                    print(Fore.CYAN + f"Switched to {mode.capitalize()} mode.")
                else:
                    print(Fore.RED + "Invalid choice.")
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

if __name__ == '__main__':
    main()
