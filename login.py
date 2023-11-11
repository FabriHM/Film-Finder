import tkinter as tk
from tkinter import messagebox
import csv
from interfaceUI import MainWindow

class LoginApp:
    def show_register_window(self):
        self.root.withdraw()
        from register import RegisterApp  # Import locally to avoid circular import
        register_app = RegisterApp(tk.Toplevel(self.root), self)
        register_app.show_window()

    def __init__(self, root):
        self.root = root
        self.root.title("Login")

        # Labels
        self.label_user = tk.Label(root, text="User:")
        self.label_password = tk.Label(root, text="Password:")

        # Entry fields
        self.entry_user = tk.Entry(root)
        self.entry_password = tk.Entry(root, show="*")

        # Buttons
        self.button_login = tk.Button(
            root, text="Login", command=self.login)
        self.button_register = tk.Button(
            root, text="Register", command=self.show_register_window)

        # Positioning elements in the interface
        self.label_user.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.label_password.grid(
            row=1, column=0, padx=10, pady=5, sticky=tk.W)

        self.entry_user.grid(row=0, column=1, padx=10, pady=5)
        self.entry_password.grid(row=1, column=1, padx=10, pady=5)

        self.button_login.grid(row=2, column=1, pady=10)
        self.button_register.grid(row=3, column=1, pady=10)

    def login(self):
        # Get values from entry fields
        user = self.entry_user.get()
        password = self.entry_password.get()

        # Validate that both user and password are entered
        if not user or not password:
            messagebox.showerror(
                "Error", "Please enter both user and password.")
            return

        # Login logic
        # Read data stored in the CSV file
        with open("users.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[5] == user and row[6] == password:
                    messagebox.showinfo("Success", "Successful login.")
                    main_window = MainWindow()
                    main_window.mainloop()
                    return

        # Show error message if credentials are not valid
        messagebox.showerror("Error", "Invalid credentials.")

# Create the main window
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)

    # Start the main application loop
    root.mainloop()
