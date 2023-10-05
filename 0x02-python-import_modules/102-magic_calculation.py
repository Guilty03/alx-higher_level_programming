#!/usr/bin/python3

def magic_calculation(a, b):
    """Perform calculations based on the values of a and b."""
    from magic_calculation_102 import add, sub

    try:
        if a < b:
            result = add(a, b)
            for i in range(4, 6):
                result = add(result, i)
        else:
            result = sub(a, b)
    except Exception as e:
        print(f"An error occurred: {e}")
        result = None

    return result

if __name__ == "__main__":
    a = 10  # Example values for testing
    b = 5   # Modify as needed
    result = magic_calculation(a, b)

    if result is not None:
        print(f"Result: {result}")
