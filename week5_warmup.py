# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character.
magic = "abracadabra"
print(magic[5])
# b. Retrieve the second to last character.
print(magic[-2])
# c. Find the first occurrence of the letter 'c'.
print(magic.find('c'))
# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
alphabet = "abcdefhijklmnopqrstuvwxyz"
# a. Extract the letters 'hij'.
print(alphabet.find("h"))
print(alphabet[6:9])
# b. Extract every second letter starting from 'a' to 'm'.
print(alphabet[0:11:2])
# c. Reverse the entire string using slicing.
print(alphabet[::-1])

# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
quote =  "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy "
print(quote.find("J"))
print(quote[83:-1])

# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
info = "Python is fun. Fun is good. Good is subjective."
info_list = info.split()
# a. Extract the word 'subjective' without knowing its exact position.
print(info_list[-1])
# b. Extract every third word.
every_third_word = info_list[::3]
everyThirdWordJoin = " ".join(every_third_word)
print(everyThirdWordJoin)
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
new_info_list = info_list[::-1]
joinNewInfoList = " ".join(new_info_list)
print(joinNewInfoList)
# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
starwarsquote = "MAY THE FORCE BE WITH YOU."
print(starwarsquote.lower())
# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
motto = ["Make", "haste", "slowly."]
# a. Convert the list into a single string.
joined_motto = " ".join(motto)
print(joined_motto)
# b. Now, split the string at every occurrence of the letter 'a'.
split_string1 = joined_motto.split("a")
print(" ".join(split_string1))
# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
inspirational_quote = "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
print(inspirational_quote.replace("busy" , "distracted"))
# b. Replace "plans" with "mistakes".
print(inspirational_quote.replace("plans" , "mistakes"))

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
repeated_word = "Iteration " * 7
print(repeated_word)

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"]
quote2 = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
word = "moonlight"
if word in quote2:
    print("Word found")
else:
    print("word not found")

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word/phrase.
calc = "Supercalifragilisticexpialidocious"
print(len(calc))