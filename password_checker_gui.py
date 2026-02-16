import tkinter as tk
from tkinter import messagebox

def check_password():
    password = entry.get()

    has_upper = False
    has_lower = False
    has_num = False
    has_spch = False

    for i in password:
        if i.isupper():
            has_upper = True
        if i.islower():
            has_lower = True
        if i.isdigit():
            has_num = True
        if i in "@#$&*":
            has_spch = True

    feedback = []

    if len(password) < 8:
        feedback.append("• Password must be at least 8 characters")

    if not has_upper:
        feedback.append("• Add an uppercase letter")
    if not has_lower:
        feedback.append("• Add a lowercase letter")
    if not has_num:
        feedback.append("• Add a number")
    if not has_spch:
        feedback.append("• Add a special character (@#$&*)")

    score = has_upper + has_lower + has_num + has_spch

    if len(password) < 8 or score <= 1:
        strength = "WEAK"
    elif score == 4:
        strength = "STRONG"
    else:
        strength = "MEDIUM"

    result_label.config(text=f"Password Strength: {strength}")

    if feedback:
        messagebox.showinfo("Feedback", "\n".join(feedback))


# GUI window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.resizable(False, False)

# Heading
tk.Label(root, text="Password Strength Checker", font=("Arial", 14, "bold")).pack(pady=10)

# Password input
tk.Label(root, text="Enter Password:").pack()
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

# Button
tk.Button(root, text="Check Strength", command=check_password).pack(pady=10)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

root.mainloop()
