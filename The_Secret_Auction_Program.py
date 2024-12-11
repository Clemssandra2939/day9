from replit import clear
# Hint: You can clear() to clear the otput in the console.abs

from art import logo
print(logo)

print("Welcome to the Secret Auction Program")
name = input("What is your name?/n")
price = input("what's yor bid? $ /n")

info_auction = {
    "Chima": 120,
}

answer = input("Are there any other bidders?Type 'yes' or 'no'./n")
if  answer == "yes":
    clear()

    