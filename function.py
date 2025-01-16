import dict as d

# The function for encoding a message:
def encode_message(message):
    word_list = message.split(" ")
    morse_word_letters = []
    morse_word_list = []

    for n in range(0, len(word_list)):
        for l in word_list[n]:
            morse_word_letters.append(d.encode[l.upper()])
        morse_word_list.append("/".join(morse_word_letters))
        morse_word_letters = []

    return " ".join(morse_word_list)


# The function for decoding a message
def decode_message(morse_message):
    encoded_word_list = morse_message.split(" ")
    decoded_word = []
    decoded_list = []

    for n in range(0, len(encoded_word_list)):
        clean_morse_word = encoded_word_list[n].split("/")
        for l in clean_morse_word:
            decoded_word.append(d.decode[l])
        decoded_list.append("".join(decoded_word))
        decoded_word = []

    return " ".join(decoded_list).title()