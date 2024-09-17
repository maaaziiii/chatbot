import random
import requests  # To send requests to the language model API

# Assuming there's a setup for authentication and endpoint
API_KEY = 'AIzaSyD4EDOxODrl69UoVpycnCiCK3JOSOxrWl8'
API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyD4EDOxODrl69UoVpycnCiCK3JOSOxrWl8'
class NegotiationBot:
    def __init__(self):
        self.product_price = random.randint(50, 100)  # Random starting price
        self.discount_threshold = 10  # Maximum discount to propose
        self.lower_price_limit = self.product_price - self.discount_threshold

    def start_negotiation(self):
        return f"Welcome! The initial price for the product is ${self.product_price}." \
               f"What do you think? (Type 'accept', 'reject', or propose a 'counteroffer')"

    def handle_user_input(self, user_input):
        response = ""

        if user_input.lower() == "accept":
            response = "Great! The deal is closed at ${}.".format(self.product_price)

        elif user_input.lower() == "reject":
            response = "I'm sorry to hear that. Would you like to propose a counteroffer? (Enter a new price)"

        elif user_input.isdigit():
            user_price = int(user_input)
            response = self.process_counteroffer(user_price)

        else:
            response = "I didn't quite catch that. Please type 'accept', 'reject', or propose a 'counteroffer' by entering a price."

        return response

    def process_counteroffer(self, user_price):
        if user_price >= self.product_price:
            return "That's a bit high for us. How about we meet at ${} instead?".format(self.product_price - 5)

        elif self.lower_price_limit <= user_price < self.product_price:
            # Accept user price if it's within discount range
            self.product_price = user_price
            return "Deal! I'll sell it for ${}.".format(self.product_price)

        else:
            return "Your counteroffer of ${} is too low. The best I can do is ${}.".format(user_price, self.lower_price_limit)
def main():
    bot = NegotiationBot()
    print(bot.start_negotiation())

    while True:
        user_input = input("You: ")
        response = bot.handle_user_input(user_input)

        print("Bot:", response)
        
        # End the conversation if the deal is closed
        if "deal is closed" in response or "I'll sell it for" in response:
            break

if __name__ == "__main__":
    main()

def main():
    bot = NegotiationBot()
    print(bot.start_negotiation())

    while True:
        user_input = input("You: ")
        response = bot.handle_user_input(user_input)

        print("Bot:", response)
        
        # End the conversation if the deal is closed
        if "deal is closed" in response or "I'll sell it for" in response:
            break

if __name__ == "__main__":
    main()

