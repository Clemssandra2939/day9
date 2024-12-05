# Dictionary & Nesting

# Dictionary has two sections:key(word) and value(actual definition of the word)

# How to create a dictionary
# {key: Value}  # everything in the curly braces is the content of our dictionary

# E.g
programming_dictionary = {
    "Bug":"An error in a program that prevents the program from running as expected.",
    "Function":"A piece of code that you can easily call over and over again."
}

# What if you want to extract a value just by using the key,retriving items from dictionary
# e.g
# print(proramming_dictionary["Bug"])

# What if you want to add an item to the dictionary
programming_dictionary["Loop"] ="The action of doing something over and over again."
# print(programming_dictionary)

# how to make empty dictionary to start out first when coding 
empty_dictionary = {}

# How to wipe an existing dictionary,this can be helpful when the you want to restart a game or clear the user's progress
proramming_dictionary = {}
print(proramming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bugs"]="A moth in your computer." #to make it or assign it to  a defferent new value instead
# print(programming_dictionary)

# How to loop through a dictionary 
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
