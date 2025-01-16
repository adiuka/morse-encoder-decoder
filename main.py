import function as f

program_on = True

while program_on:

    mode_selection = input("Hello and welcome to the Morse Encoder and Decoder. The program takes strings as input, and depending on the mode, \n"
                        "turns them into morse coded strings or vice versa. Please choose a mode (encode or decode, and exit): \n")

    if mode_selection == 'encode':
        message = input("Please enter the message you would like to be coded in morse: \n")
        print(f.encode_message(message=message))

    elif mode_selection == 'decode':
        message = input("Please enter the message in morse you would like to be translated: \n"
                        "(NOTE: Morse letters contain . and -, each letter is seperated by / and each word by a ' ') \n"
                        "(e.g. )")
        try: 
            print(message)
