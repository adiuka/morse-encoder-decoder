import dict as d

string = 'Hello World!'


# TODO!: I need the script to break down each word into a list:

word_list = string.split(" ")

# TODO!: I need the script to then break down each letter of every word into letters and convert them into mores equivalent:

morse_word_letters = []
morse_word_list = []

# Here I try to loop through every word in the split string:
for n in range(0, len(word_list)):
    # And another loop for looping through every character in the word:
    for l in word_list[n]:
        # I then append the encoded letter into a new list:
        morse_word_letters.append(d.encode[l.upper()])
    # Then I join it into a word, together with a dash / that simbolises a new letter. 
    morse_word_list.append("/".join(morse_word_letters))
    # I then drop the word list to get ready for the new word in the loop:
    morse_word_letters = []

morse_string = " ".join(morse_word_list)
print(morse_string)
# First and foremost I split the encoded morse sentance into a list:
encoded_word_list = morse_string.split(" ")

decoded_word = []
decoded_list = []

for n in range(0, len(encoded_word_list)):
    clean_morse_word = encoded_word_list[n].split("/")
    for l in clean_morse_word:
          decoded_word.append(d.decode[l])
    decoded_list.append("".join(decoded_word))
    decoded_word = []
    

print(" ".join(decoded_list).title())