def only_ints(param1, param2):
    """
    Check if both parameters are integers.

    Args:
        param1 (any): The first parameter.
        param2 (any): The second parameter.

    Returns:
        bool: True if both parameters are integers, False otherwise.
    """
    return type(param1) == int and type(param2) == int

# Example usage:
print(only_ints(5, 10))   # Output: True
print(only_ints(3, "hello"))  # Output: False
print(only_ints("world", 7))  # Output: False
print(only_ints(2.5, 6))   # Output: False
