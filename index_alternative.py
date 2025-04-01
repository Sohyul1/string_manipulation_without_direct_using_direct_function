# Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.

# Sample string
sample_string = "hello world"
substring = "world"

# Create a funtion that replicates index()
for i  in range(len(sample_string)):
    if sample_string[i:i + len(substring)] == substring:
        # Implement
        print(i)
        break
 