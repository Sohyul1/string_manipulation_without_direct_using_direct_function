# Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

# Sample string
sample_string = "hello world, hello there"
substring = "hello"

# Initialize count 
count = 0

# Create a function that repliicates count()
for i in range(len(sample_string) - len(substring) + 1):
    if sample_string[i:i + len(substring)] == substring:
        count += 1

# Implement
print(count)