# Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

# Sample string
sample_string1 = "HELLO"
sample_string2 = "hello hi"
# Create a function to replicate isupper()
def uppercase_checker(s):
    for char in s:
        if char.isalpha() and char != char.upper():        
        # Implement
            print("NO")
            return
    print("YES")

uppercase_checker(sample_string1)
uppercase_checker(sample_string2)