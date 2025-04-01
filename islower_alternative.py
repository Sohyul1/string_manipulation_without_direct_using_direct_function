# Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

# Sample String
sample_string1 = "HELLO"
sample_string2 = "hello hi"

# Create a function that replicates islower()
def lowercase_checker(s):
    for char in s:
        if char.isalpha() and char != char.lower(): 
        # Implement
            print("No")
            return
    print("Yes")

lowercase_checker(sample_string1)
lowercase_checker(sample_string2)
