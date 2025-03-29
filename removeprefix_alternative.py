# Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

# Sample string
smpl_string = "AeroGel"
prefix = "Aero"

#  Create a function to replicate removeprefix()
if smpl_string.startswith(prefix):
    index = smpl_string.index(prefix) + len(prefix)
    new_string = smpl_string[index:]

# Implement
print(new_string)