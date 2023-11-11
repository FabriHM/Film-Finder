import tkinter as tk
from tkinter import messagebox
import csv
from login import LoginApp

class RegisterApp:
    def show_window(self):
        self.root.mainloop()

    def __init__(self, root, login_app):
        self.root = root
        self.login_app = login_app
        self.root.title("Register")

        # Labels
        self.label_id = tk.Label(root, text="ID:")
        self.label_full_name = tk.Label(root, text="Full Name:")
        self.label_birth_date = tk.Label(root, text="Birth Date:")
        self.label_phone = tk.Label(root, text="Phone:")
        self.label_email = tk.Label(root, text="Email:")
        self.label_username = tk.Label(root, text="Username:")
        self.label_password = tk.Label(root, text="Password:")

        # Entry fields
        self.entry_id = tk.Entry(root)
        self.entry_full_name = tk.Entry(root)
        self.entry_birth_date = tk.Entry(root)
        self.entry_phone = tk.Entry(root)
        self.entry_email = tk.Entry(root)
        self.entry_username = tk.Entry(root)
        self.entry_password = tk.Entry(root, show="*")

        # Buttons
        self.button_register = tk.Button(
            root, text="Register", command=self.register)
        self.button_login = tk.Button(
            root, text="Login", command=self.show_login_window)

        # Positioning elements in the interface
        self.label_id.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.label_full_name.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.label_birth_date.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.label_phone.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.label_email.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        self.label_username.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
        self.label_password.grid(
            row=6, column=0, padx=10, pady=5, sticky=tk.W)

        self.entry_id.grid(row=0, column=1, padx=10, pady=5)
        self.entry_full_name.grid(row=1, column=1, padx=10, pady=5)
        self.entry_birth_date.grid(row=2, column=1, padx=10, pady=5)
        self.entry_phone.grid(row=3, column=1, padx=10, pady=5)
        self.entry_email.grid(row=4, column=1, padx=10, pady=5)
        self.entry_username.grid(row=5, column=1, padx=10, pady=5)
        self.entry_password.grid(row=6, column=1, padx=10, pady=5)

        self.button_register.grid(row=7, column=1, pady=10)
        self.button_login.grid(row=8, column=1, pady=10)

    def register(self):
        # Get values from entry fields
        user_id = self.entry_id.get()
        full_name = self.entry_full_name.get()
        birth_date = self.entry_birth_date.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Validate that all fields are filled
        if not user_id or not full_name or not birth_date or not phone or not email or not username or not password:
            messagebox.showerror(
                "Error", "Please fill in all the fields.")
            return

        # Registration logic
        # Save data to the CSV file
        with open("users.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([user_id, full_name, birth_date, phone, email, username, password])

        # Close the current window
        self.root.destroy()

        # Show the login window
        self.login_app.root.deiconify()

    def show_login_window(self):
        self.root.destroy()
        self.login_app.root.deiconify()

# Create the main window
if __name__ == "__main__":
    root = tk.Tk()
    app = RegisterApp(root, LoginApp(root))

    # Start the main application loop
    root.mainloop()
