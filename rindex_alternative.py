# Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.

# Sample string
sample_string = "hello world and hello to you"
substring = "hello"

# Create a funtion that replicates index()
for i  in range(len(sample_string) - len(substring), -1, -1):
    if sample_string[i:i + len(substring)] == substring:
        # Implement
        print(i)
        break

