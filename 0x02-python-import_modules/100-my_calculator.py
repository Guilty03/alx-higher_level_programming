#!/usr/bin/python3

if __name__ == "__main__":
    """Handle basic arithmetic operations."""

    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    ops = {"+": add, "-": sub, "*": mul, "/": div}

    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    result = ops[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
