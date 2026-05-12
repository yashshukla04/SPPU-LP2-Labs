Code Explanation
1. Import re Module
import re

Used for regular expression matching.

2. ChatBot Class
class ChatBot:

Creates chatbot object.

3. Constructor
def __init__(self):

Initializes:

chatbot name,
running status.
4. greet()
def greet(self):

Displays welcome message.

5. get_intent()
def get_intent(self, user_input):

Detects user intent using keywords.

6. intents Dictionary

Stores:

intent names,
related keywords.

Example:

"refund": ["refund", "return"]
7. handle_intent()
def handle_intent(self, intent, user_input):

Displays response based on detected intent.

8. extract_order_id()
re.search(r"\d+", text)

Extracts numeric order ID.

9. run()

Main chatbot loop.

Takes user input continuously until exit.

Sample Output

According to output screenshot on page 3:

ShopBot: Hello! Welcome to our store

You: delivery

ShopBot: Standard delivery takes 3-5 working days.

You: refund

ShopBot: Refunds are processed within 5-7 business days.
Complexity Analysis
Time Complexity:
O(n)

where n = number of keywords.

Viva Questions
What is chatbot?

AI software that communicates with users.

What is intent recognition?

Identifying user purpose from input.

Why regex is used?

To extract patterns like order IDs.

Applications of chatbot?
Customer support
Banking
E-commerce
Virtual assistants
Advantages of chatbot?
Fast response
24×7 service
Reduced human effort
Conclusion

Thus, we successfully implemented a Smart Customer Support Chatbot using Python with intent recognition and automated responses.