import argparse
from calculator_functions import multiply, subtract, divide, add

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Math Operations')
    parser.add_argument('numbers', type=str, help='Comma-separated list of numbers')
    parser.add_argument('-o', '--operation', choices=['multiply', 'subtract', 'divide', 'add'], help='Operation to perform')
    args = parser.parse_args()

    numbers = [int(num) for num in args.numbers.split(',')]

    if args.operation == 'multiply':
        result = multiply(numbers)
    elif args.operation == 'subtract':
        if len(numbers) != 2:
            print("Subtraction requires exactly two numbers.")
            exit(1)
        result = subtract(numbers)
    elif args.operation == 'divide':
        if len(numbers) != 2:
            print("Division requires exactly two numbers.")
            exit(1)
        result = divide(numbers)
    else:
        result = add(numbers)

    print(f"Result: {result}")
