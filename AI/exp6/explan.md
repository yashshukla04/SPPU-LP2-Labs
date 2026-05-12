Code Explanation
1. Import Tkinter
import tkinter as tk

Used to create GUI window.

2. Import ScrolledText
from tkinter import scrolledtext

Used for scrollable output box.

3. get_recommendation()
def get_recommendation(...)

Main expert system logic.

Uses IF-ELSE rules for recommendations.

4. BUY Rule
if trend == "up" and risk == "low"

Suggests BUY for positive growth and low risk.

5. SELL Rule
elif trend == "down" and risk == "high"

Suggests SELL for risky downtrend stocks.

6. analyze_stock()
def analyze_stock():

Reads user input and displays recommendation.

7. Tkinter Window
root = tk.Tk()

Creates main GUI window.

8. Input Fields
tk.Entry(frame)

Accepts stock details from user.

9. Button
tk.Button(...)

Triggers stock analysis.

10. Chat Box
ScrolledText(...)

Displays recommendation output.

Sample Output

According to uploaded screenshots:

Example 1
Stock: Tata Motors

Trend: down
Risk: high
Volatility: high

Recommendation:
SELL (High risk, downtrend)

Confidence: 90%
Example 2
Stock: Infosys Systems

Trend: up
Risk: medium
Volatility: high

Recommendation:
HOLD / BUY cautiously

Confidence: 65%
Complexity Analysis
Time Complexity:
O(1)

because fixed rule checks are performed.

Viva Questions
What is Expert System?

AI system that mimics human expert decisions.

What is Knowledge Base?

Collection of facts and rules.

What is Inference Engine?

Processes rules to make decisions.

What is Tkinter?

Python GUI library.

Applications of Expert Systems?
Medical diagnosis
Finance
Banking
Customer support
Conclusion

Thus, we successfully implemented a GUI-based Stock Market Advisor Expert System using Python and Tkinter with rule-based decision making.