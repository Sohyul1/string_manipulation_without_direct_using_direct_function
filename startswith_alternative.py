# Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

# Sample string and starting character
sample_string = "hello_world"
startswith = "hello"

# Create a funtionthat replicates startswith()
index = len(startswith)
if sample_string[:index] == startswith:
    print("Yes")
else:
    print("NO")

