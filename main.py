# Dictionary representing the Morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# Get user input for the word to convert
user_input = input("Please enter the word you would like to convert into Morse code: ")

# Iterate through each character in the input and convert to Morse code
for char in user_input:
    # Check if the character exists in the Morse code dictionary
    if char.upper() in MORSE_CODE_DICT:
        # Print the Morse code representation for the character
        print(MORSE_CODE_DICT[char.upper()], end="")
    else:
        # If character is not in the dictionary, print a message
        print(f"Character '{char}' cannot be converted to Morse code.", end="")

