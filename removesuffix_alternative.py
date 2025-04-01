# Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.

# Sample string 
smpl_string = "AeroGel"
suffix = "Gel"

# Create a function that replicates remove suffix 
if smpl_string.endswith(suffix):
    index = len(smpl_string) - len(suffix)
    new_string = smpl_string[:index]

else:
    new_string = smpl_string

# Implement
print(new_string)