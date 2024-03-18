def mid(s):
    length = len(s)
    if length % 2 == 0:
        return ''
    else:
        return s[length // 2]

# Example usage:
string1 = "hello"
string2 = "python"
string3 = "abcd"
print(mid(string1))  # Output: l
print(mid(string2))  # Output: h
print(mid(string3))  # Output: ''
