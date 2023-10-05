from magic_calculation_102 import add, sub

def magic_calculation(a, b):
    add_result = add(a, b)
    
    if add_result < 0:
        return add_result

    sub_result = sub(a, b)

    for i in range(4, 6):
        add_result = add(add_result, i)

    return add_result

if __name__ == "__main__":
    a = 10  # Example values for testing
    b = 5   # Modify as needed
    result = magic_calculation(a, b)

    if result is not None:
        print(f"Result: {result}")
