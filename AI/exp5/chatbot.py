import re

class ChatBot:

    def __init__(self):

        self.name = "ShopBot"
        self.running = True

    def greet(self):

        print(f"{self.name}: Hello! Welcome to our store 😊")

        print(f"{self.name}: I can help you with orders, refunds, delivery, and products.")

        print(f"{self.name}: Type 'exit' anytime to quit.\n")

    def get_intent(self, user_input):

        user_input = user_input.lower()

        intents = {

            "greeting":
            ["hello", "hi", "hey"],

            "order_status":
            ["order", "track", "status"],

            "refund":
            ["refund", "return", "cancel"],

            "delivery":
            ["delivery", "shipping", "arrive"],

            "product":
            ["product", "item", "buy"],

            "thanks":
            ["thanks", "thank you"]
        }

        for intent, keywords in intents.items():

            for word in keywords:

                if word in user_input:
                    return intent

        return "unknown"

    def handle_intent(self,
                      intent,
                      user_input):

        if intent == "greeting":

            print(f"{self.name}: Hi there! How can I assist you today?")

        elif intent == "order_status":

            order_id = self.extract_order_id(user_input)

            if order_id:

                print(f"{self.name}: Checking status for order #{order_id}...")

                print(f"{self.name}: Your order is out for delivery 🚚")

            else:

                print(f"{self.name}: Please provide your order ID.")

        elif intent == "refund":

            print(f"{self.name}: Refunds are processed within 5-7 business days.")

            print(f"{self.name}: Would you like to initiate a refund?")

        elif intent == "delivery":

            print(f"{self.name}: Standard delivery takes 3-5 working days.")

            print(f"{self.name}: Express delivery takes 1-2 days.")

        elif intent == "product":

            print(f"{self.name}: We have electronics, clothing, and accessories.")

            print(f"{self.name}: What are you looking for?")

        elif intent == "thanks":

            print(f"{self.name}: You're welcome! 😊")

        else:

            print(f"{self.name}: Sorry, I didn't understand that.")

            print(f"{self.name}: Can you please rephrase?")

    def extract_order_id(self, text):

        match = re.search(r"\d+", text)

        return match.group() if match else None

    def run(self):

        self.greet()

        while self.running:

            user_input = input("You: ")

            if user_input.lower() in [
                "exit",
                "bye",
                "quit"
            ]:

                print(f"{self.name}: Thank you for visiting! Have a great day 😊")

                self.running = False
                break

            intent = self.get_intent(user_input)

            self.handle_intent(
                intent,
                user_input
            )


# Run chatbot
if __name__ == "__main__":

    bot = ChatBot()

    bot.run()