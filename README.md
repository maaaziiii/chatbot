This Python code defines a simple Negotiation Bot that simulates a negotiation process for a product with a random starting price.

Features
Generates a random starting price between $50 and $100.
Allows users to accept, reject, or propose a counteroffer.
Negotiates within a predefined discount range.
Provides informative responses based on user input.
Usage
Save the code as a Python file (e.g., negotiation_bot.py).
Run the script from your terminal: python negotiation_bot.py

The provided code takes the Google's Gemini 1.5 model and connects it in a negotiation bot. An API key and URL are used to make the connection with the model. The negotiation bot is simulating negotiating on a product price with a user via text messages like 'accept'/'reject' or a new counteroffer. The bot is generating it's own response (although using requests library to talk to the language model) but most importantly, sending user’s inputs to the model by adding them to an understandable API url and receiving dynamic responses. If you would instead send these requests to model and receive them + adjust your negotiation dynamically based on this Model’s part that is returned as output - this way making your process of negotiation interactive & adaptable.

Example Interaction:

Welcome! The initial price for the product is $72. What do you think? (Type 'accept', 'reject', or propose a 'counteroffer')
You: counteroffer 65
Bot: That's a bit high for us. How about we meet at $67 instead?
You: accept
Bot: Great! The deal is closed at $67.
