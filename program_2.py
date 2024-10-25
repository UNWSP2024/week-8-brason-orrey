def separate_words(sentence):
    # Initialize an empty result string
    result = sentence[0]  # Start with the first character (index=0)

    # Loop through the rest of the sentence after first character
    for char in sentence[1:]:
        # If the character is uppercase, add a space before it and convert it to lowercase
        if char.isupper():
            result += ' ' + char.lower()
        else:
            result += char

    # Capitalize the first character and return the result
    return result.capitalize()

# Get user input
input_sentence = input("Enter a camel-cased sentence: ")

# Display the modified sentence
print("Converted sentence:", separate_words(input_sentence))
