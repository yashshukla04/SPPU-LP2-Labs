import tkinter as tk
from tkinter import scrolledtext

# --- Expert System Logic ---
def get_recommendation(stock,
                       trend,
                       risk,
                       volatility):

    if trend == "up" and risk == "low":

        return "BUY 📈 (Strong growth, low risk)\nConfidence: 85%"

    elif trend == "up" and risk == "medium":

        return "HOLD / BUY cautiously ⚠️\nConfidence: 65%"

    elif trend == "down" and risk == "high":

        return "SELL 📉 (High risk, downtrend)\nConfidence: 90%"

    elif volatility == "high":

        return "HOLD ⏸️ (Market unstable)\nConfidence: 60%"

    elif trend == "up":

        return "BUY 🚀 (Positive momentum)\nConfidence: 75%"

    else:

        return "HOLD ⏸️ (Wait for better opportunity)\nConfidence: 50%"


# --- Button Function ---
def analyze_stock():

    stock = entry_stock.get()

    trend = entry_trend.get().lower()

    risk = entry_risk.get().lower()

    volatility = entry_volatility.get().lower()

    result = get_recommendation(
        stock,
        trend,
        risk,
        volatility
    )

    chat_box.config(state=tk.NORMAL)

    chat_box.insert(
        tk.END,
        f"\n📊 Stock: {stock}\n",
        "user"
    )

    chat_box.insert(
        tk.END,
        f"Trend: {trend}, Risk: {risk}, Volatility: {volatility}\n",
        "user"
    )

    chat_box.insert(
        tk.END,
        "👉 Recommendation:\n",
        "bot"
    )

    chat_box.insert(
        tk.END,
        result + "\n" + "-" * 50 + "\n",
        "bot"
    )

    chat_box.config(state=tk.DISABLED)

    chat_box.yview(tk.END)


# --- UI Window ---
root = tk.Tk()

root.title("Groww-like Stock Advisor Bot")

root.geometry("500x600")

root.config(bg="#1e272e")


# --- Title ---
title = tk.Label(
    root,
    text="📊 Stock Market Advisor Bot",
    font=("Arial", 16, "bold"),
    bg="#1e272e",
    fg="white"
)

title.pack(pady=10)


# --- Input Fields ---
frame = tk.Frame(root,
                 bg="#1e272e")

frame.pack()

tk.Label(
    frame,
    text="Stock Name:",
    bg="#1e272e",
    fg="white"
).grid(row=0, column=0)

entry_stock = tk.Entry(frame)

entry_stock.grid(row=0, column=1)

tk.Label(
    frame,
    text="Trend (up/down):",
    bg="#1e272e",
    fg="white"
).grid(row=1, column=0)

entry_trend = tk.Entry(frame)

entry_trend.grid(row=1, column=1)

tk.Label(
    frame,
    text="Risk (low/medium/high):",
    bg="#1e272e",
    fg="white"
).grid(row=2, column=0)

entry_risk = tk.Entry(frame)

entry_risk.grid(row=2, column=1)

tk.Label(
    frame,
    text="Volatility (low/high):",
    bg="#1e272e",
    fg="white"
).grid(row=3, column=0)

entry_volatility = tk.Entry(frame)

entry_volatility.grid(row=3, column=1)


# --- Button ---
btn = tk.Button(
    root,
    text="Analyze Stock 📊",
    command=analyze_stock,
    bg="green",
    fg="white"
)

btn.pack(pady=10)


# --- Chat Output Box ---
chat_box = scrolledtext.ScrolledText(
    root,
    width=60,
    height=20,
    state=tk.DISABLED
)

chat_box.pack(pady=10)

chat_box.tag_config(
    "user",
    foreground="blue"
)

chat_box.tag_config(
    "bot",
    foreground="green"
)


# --- Run App ---
root.mainloop()