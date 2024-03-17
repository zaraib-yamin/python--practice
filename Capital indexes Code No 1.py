def capital_indexes(string):
    """
    Return a list of indexes of capital letters in the given string.

    Args:
    string (str): The input string.

    Returns:
    list: A list containing the indexes of capital letters in the string.
    """
    return [index for index, char in enumerate(string) if char.isupper()]

# Example usage:
print(capital_indexes("Hello World"))  # Output: [0, 6]