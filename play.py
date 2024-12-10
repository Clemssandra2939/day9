# Instructions
# You are going to write a program that add to a travel_log,
# You can see a travel_log which is a List that contain 2 dictionaries.

# Write a function that will work the following line of code on line 21 to add the  entry for Russia to the travel_log.

# add_new_country {"Russia",2,["Moscow","Saint Peterburg"]}

# You 've visited Russia 2 times.
# You 've  been to Moscow and Saint Peterburg 

# Do Not modify the travel_log directly,You need to create  a functiom that modify it 

# Hint
# Look at the function call above to see what the nae of function should be.
# the input for the function are positional arguments.the order is very iportant.

# 


# Function that allows multiple input
# def greet_with(name,location):
#     print(f"Hello {name}")
#     print(f"wat is it like in {location}")

# greet_with("Sandra", "Enugu")

# when the postion of the data is switched like
# def greet_with(name,location):
#     print(f"Hello {name}")
#     print(f"wat is it like in {location}")

# greet_with("Enugu", "Sandra")

# this wat it is goinh to be like
# ##Hello Enugu
# Wwat is it like in Sandra

# placing it in the wrong parameters,this is called postional argument

# Keyword arguemnt

# Keyword argument is a way of resolving those kind of errors of poistional argument
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"wat is it like in {location}")

greet_with(location = "Enugu", name = "Sandra")