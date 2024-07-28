import tkinter as tk
import re

def check_password_strength():
    password = password_entry.get()
    length = len(password) >= 8
    uppercase= bool(re.search(r'[A-Z]', password))
    lowercase= bool(re.search(r'[a-z]', password))
    number= bool(re.search(r'\d', password))
    special= bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    feedback = []
    if length:
        feedback.append("✓ Length is sufficient")
    else:
        feedback.append("✗ Length should be at least 8 characters")
    if uppercase:
        feedback.append("✓ Contains uppercase letter(s)")
    else:
        feedback.append("✗ Should contain at least one uppercase letter")
    if lowercase:
        feedback.append("✓ Contains lowercase letter(s)")
    else:
        feedback.append("✗ Should contain at least one lowercase letter")
    if number:
        feedback.append("✓ Contains number(s)")
    else:
        feedback.append("✗ Should contain at least one number")
    if special:
        feedback.append("✓ Contains special character(s)")
    else:
        feedback.append("✗ Should contain at least one special character")
    
    feedback_text = "\n".join(feedback)
    feedback_label.config(text=feedback_text, font=("Helvetica", 12))
    if all([length, uppercase, lowercase, number, special]):
        strength_label.config(text="Password Strength: Strong", fg="green", font=("Helvetica", 14, "bold"))
    elif length and any([uppercase, lowercase, number, special]):
        strength_label.config(text="Password Strength: Moderate", fg="orange", font=("Helvetica", 14, "bold"))
    else:
        strength_label.config(text="Password Strength: Weak", fg="red", font=("Helvetica", 14, "bold"))

#GUI
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.configure(bg="#f0f0f0")
title_label = tk.Label(root, text="Password Strength Checker", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

password_label = tk.Label(root, text="Enter Password:", font=("Helvetica", 12), bg="#f0f0f0")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*", font=("Helvetica", 12), width=30)
password_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Password Strength", command=check_password_strength, bg="#4CAF50", fg="white", font=("Helvetica", 12))
check_button.pack(pady=10)
feedback_label = tk.Label(root, text="", bg="#f0f0f0", justify="left", font=("Helvetica", 12))
feedback_label.pack(pady=5)

strength_label = tk.Label(root, text="", bg="#f0f0f0", font=("Helvetica", 14, "bold"))
strength_label.pack(pady=10)

root.mainloop()
