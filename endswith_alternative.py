# Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

# Sample string and suffix
sample_string = "hello_world"
suffix = "world"

# Create a function to replicate endswith()
index = len(suffix)
if sample_string[-index:] == suffix:
    print("YES") 
else:
    print("NO")  

