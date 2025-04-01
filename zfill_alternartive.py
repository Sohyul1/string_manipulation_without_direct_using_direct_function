# Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

# Sample string
sample_number = 123
total_characters = 5

# Zeros to add 
zeros_to_add = total_characters - len(str(sample_number))

# Create a function that replicates zfill()
if zeros_to_add > 0:
    new_num = "0" * zeros_to_add + str(sample_number)
else:
    new_num = sample_number

# Implement 
print(new_num)