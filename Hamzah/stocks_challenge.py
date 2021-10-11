print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

Amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
# TODO: Write code to ask the client his savings and save it to another variable.
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
name = input("What is your name?")
print(name)
savings = int(input("What is your savings?"))
print(int(savings))
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print(stock)

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stored in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

# '''
# Your code should look like this:

# if stock == "amzn":
#     ...
# elif ...
# else ...
# '''

if stock == "amzn":
    if savings < 3000:
       print("You don't have enough savings to purchase Amazon stock.")
    if savings >= 3000:
        print(f"You can purchase ({savings / Amazon}) with the amount in your savings!")
    print(f"{name} has ${savings} in savings and he can buy {savings / Amazon} shares of Amazon at the current price of $3000.")

elif stock == "appl":
    if savings < 100:
       print("You don't have enough savings to purchase Apple stock.")
    if savings >= 100:
        print(f"You can purchase ({savings / apple}) with the amount in your savings!")
    print(f"{name} has ${savings} in savings and he can buy {savings / apple} shares of Apple at the current price of $100.")

elif stock == "fb":
    if savings < 250:
       print("You don't have enough savings to purchase FaceBook stock.")
    if savings >= 250:
        print(f"You can purchase ({savings / fb}) with the amount in your savings!")
    print(f"{name} has ${savings} in savings and he can buy {savings / fb} shares of FaceBook at the current price of $250.")

elif stock == "goog":
    if savings < 1400:
       print("You don't have enough savings to purchase Google stock.")
    if savings >= 1400:
        print(f"You can purchase ({savings / google}) with the amount in your savings!")
    print(f"{name} has ${savings} in savings and he can buy {savings / google} shares of Google at the current price of $1400.")

elif stock == "msft":
    if savings < 200:
       print("You don't have enough savings to purchase Microsoft stock.")
    if savings >= 200:
        print(f"You can purchase ({savings / msft}) with the amount in your savings!")
    print(f"{name} has ${savings} in savings and he can buy {savings / msft} shares of Microsoft at the current price of $200.")

else:
    print("I don't understand.")



print("Challenge 3.2.3: Output for the user the result")
# TODO: Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

print(f"{name} has ${savings} in savings and he can buy {savings / Amazon} shares of Amazon at the current price of $3000.")

print(f"{name} has ${savings} in savings and he can buy {savings / apple} shares of Apple at the current price of $100.")

print(f"{name} has ${savings} in savings and he can buy {savings / fb} shares of FaceBook at the current price of $250.")

print(f"{name} has ${savings} in savings and he can buy {savings / google} shares of Google at the current price of $1400.")

print(f"{name} has ${savings} in savings and he can buy {savings / msft} shares of Microsoft at the current price of $200.")


