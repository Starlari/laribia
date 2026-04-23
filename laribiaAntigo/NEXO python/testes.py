import tkinter as tk
from tkinter import messagebox

def login_check():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password123":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Create the main window
root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")

# Create and place labels and entry fields
username_label = tk.Label(root, text="Username:")
username_label.pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

password_label = tk.Label(root, text="Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*") # Hides password input
password_entry.pack(pady=5)

# Create and place the login button
login_button = tk.Button(root, text="Login", command=login_check)
login_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()