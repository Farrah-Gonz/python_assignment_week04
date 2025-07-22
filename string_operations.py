def reverse_string(s):
    return s[::-1]
def capitalize_string(s):
    return s.capitalize()
def lowercase_string(s):
    return s.lower()
def uppercase_string(s):
    return s.upper()

import string_operations as so

sample_string = "hello World"

print("Original:", sample_string)
print("Reversed:", so.reverse_string(sample_string))
print("Capitalized:", so.capitalize_string(sample_string))
print("Lowercase:", so.lowercase_string(sample_string))
print("Uppercase:", so.uppercase_string(sample_string))
