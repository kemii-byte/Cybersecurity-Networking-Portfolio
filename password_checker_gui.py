import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"[0-9]", password):
        score += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        return "Weak ❌", "red"
    elif score <= 4:
        return "Moderate ⚠️", "orange"
    else:
        return "Strong ✅", "green"


def evaluate_password():
    password = entry.get()

    if password == "":
        messagebox.showwarning("Input Error", "Please enter a password")
        return

    strength, color = check_password_strength(password)
    result_label.config(text=f"Strength: {strength}", fg=color)


# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")

title_label = tk.Label(root, text="Password Checker 🔐", font=("Arial", 16))
title_label.pack(pady=10)

entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=10)

check_button = tk.Button(root, text="Check Strength", command=evaluate_password)
check_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()