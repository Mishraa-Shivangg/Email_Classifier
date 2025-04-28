import tkinter as tk
from tkinter import messagebox
import joblib

# Load model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Function to check if email is spam
def check_spam():
    email_text = entry.get("1.0", tk.END).strip()
    if not email_text:
        messagebox.showwarning("Warning", "Please enter an email!")
        return

    email_vec = vectorizer.transform([email_text])
    prediction = model.predict(email_vec)[0]

    if prediction == 1:
        result_label.config(text="Spam ❌", fg="red")
    else:
        result_label.config(text="Not Spam ✅", fg="green")

# GUI Setup
root = tk.Tk()
root.title("Spam Email Detector")
root.geometry("500x300")
root.configure(bg="#f0f0f0")

# Widgets
tk.Label(root, text="Enter Email Text:", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)
entry = tk.Text(root, height=5, width=50, font=("Arial", 12))
entry.pack(pady=5)

check_button = tk.Button(root, text="Check Spam", command=check_spam, font=("Arial", 12), bg="blue", fg="white")
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#f0f0f0")
result_label.pack(pady=10)

# Run the app
root.mainloop()
