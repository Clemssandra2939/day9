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


# Day 8-caesar cipher 4
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z''a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(start_text,shift_amount,cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1  
    for char in start_text:
        if char in alphabet:
          position = alphabet.index(char)
          new_position = position + shift_amount
          end_text += alphabet[new_position]
        else:
          end_text += char
    
        #  TODO-3-What happens if the user enters a number/sybol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g start_text = "meet me at 3"
        # end_text ="**** ** ** 3"

       
    print(f"Here's the {cipher_direction}d result:{end_text}")

    # TODO -1 - : Import and print the logo from art.py when the program starts.
from art import logo
print(logo)
    # TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
    # e.g Type 'yes' if you wat to go again.otherwise type 'no'. 
    # if they 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
    # Hint:Try creating a new function that calls itself if they type 'yes'.
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt,type 'decode' to decrypt :\n")
    text = input("Type your message:\n").lower()
    shift =int(input("Type the shift number :\n"))

    # TODO -2: What if the user enters a shift that greater than the number of letters in the alphabet?
    # Try running the program and entering a shift number of 45
    # Hint: Think about how you ca use the modulus(%)
    shift = shift % 25 #25 is the rang of the alphabet 0-25 so that my code won't break
    # print(shift) #th nw shift after modulus %
    caesar(start_text=text,shift_amount=shift,cipher_direction=direction)

    result =input("Type 'yes' if you wat to go again.otherwise type 'no'.\n")
    if result == "no":
       should_continue = False
       print("Goodbye!")




# Tip calculator program
print("Welcome to the tip calculator")
total_bill=(input("what is the total_bill? $"))
print(total_bill)
percentage_tip=(input("what is the percentage_tip would u like to give? 10,12 or 15 "))
print(percentage_tip)
num_people=(input("how many people to split the bills?"))
print(num_people)
percentage_number=(int(percentage_tip)/100)
print(percentage_number)
Everyones_bill =int(total_bill) * float(percentage_number)
result=int(Everyones_bill)+ int(total_bill)
print(result)
result/=int(num_people)
print(result)
print(f"Each person should pay:{result}$")
# if the bill was 150.00,split btw 7 people,with 12% tip.
# Each person should pay(150.00/5)*0.12
# Round up to two decimal places