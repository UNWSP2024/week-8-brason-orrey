def get_user_name(full_name):
    # Split the name into parts
    name_parts = full_name.split()
    
    # Get the initials by taking the first letter of each part
    initials = [name[0].upper() + '.' for name in name_parts]
    
    # Join the initials with spaces
    return ' '.join(initials)

# Get user input
full_name = input("Enter a person's full name (first, middle, and last): ")

# Display the initials
print("Initials are:", get_user_name(full_name))
