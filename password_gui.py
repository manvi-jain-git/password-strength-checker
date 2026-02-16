import tkinter as tk
from password_logic import check_password_strength


def live_check(event=None):
    password = entry.get()

    strength, feedback = check_password_strength(password)

    # Strength text + color
    strength_label.config(text=f"Strength: {strength}")

    if strength == "WEAK":
        strength_label.config(fg="red")
    elif strength == "MEDIUM":
        strength_label.config(fg="orange")
    else:
        strength_label.config(fg="green")

    # Reset rule colors
    length_label.config(fg="red")
    upper_label.config(fg="red")
    digit_label.config(fg="red")
    special_label.config(fg="red")

    # Turn rules green if satisfied
    if len(password) >= 8:
        length_label.config(fg="green")
    if any(c.isupper() for c in password):
        upper_label.config(fg="green")
    if any(c.isdigit() for c in password):
        digit_label.config(fg="green")
    if any(c in "!@#$%^&*()" for c in password):
        special_label.config(fg="green")


# Window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("420x320")
root.resizable(False, False)

# Heading
tk.Label(root, text="Password Strength Checker",
         font=("Arial", 14, "bold")).pack(pady=10)

# Input label
tk.Label(root, text="Enter Password:").pack()

# Password field
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

# Live checking
entry.bind("<KeyRelease>", live_check)

# Strength result
strength_label = tk.Label(root, text="Strength: ",
                           font=("Arial", 12, "bold"))
strength_label.pack(pady=10)

# Rules section
tk.Label(root, text="Password must contain:",
         font=("Arial", 11, "bold")).pack(pady=5)

length_label = tk.Label(root, text="• At least 8 characters", fg="red")
length_label.pack(anchor="w", padx=40)

upper_label = tk.Label(root, text="• One uppercase letter", fg="red")
upper_label.pack(anchor="w", padx=40)

digit_label = tk.Label(root, text="• One number", fg="red")
digit_label.pack(anchor="w", padx=40)

special_label = tk.Label(root, text="• One special character (!@#$%^&*)", fg="red")
special_label.pack(anchor="w", padx=40)

root.mainloop()
