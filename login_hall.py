import tkinter as tk
from tkinter import messagebox
from registration_page import Registration

class Login(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # Initialize the login window
        self.title("Login")
        self.geometry("500x400")
        self.configure(bg='#4CAF50')

        # Function to handle login button click
        def login():
            username = entry_username.get()
            password = entry_password.get()
            if "@" not in username:
                messagebox.showwarning("Invalid Email", "Please enter a valid email address.")
            else:
                messagebox.showinfo("Login", f"Username: {username}\nPassword: {password}")
                self.grab_release()
                self.destroy()

        # Function to handle Google login button click
        def login_with_google():
            messagebox.showinfo("Login", "Google login clicked")

        def signup():
            registration_window = Registration(self)
            registration_window.grab_set()

        # Function to handle entry click for username
        def on_entry_click(event):
            if entry_username.get() == 'Email/Username':
                entry_username.delete(0, "end")  # delete all the text in the entry
                entry_username.config(fg='black', font=('Arial', 14, 'normal'))

        def on_password_entry_click(event):
            if entry_password.get() == 'Password':
                entry_password.delete(0, "end")  # delete all the text in the entry
                entry_password.config(fg='black', font=('Arial', 14, 'normal'))

        # Function to handle focus out for username
        def on_focus_out(event):
            if entry_username.get() == '':
                entry_username.insert(0, 'Email/Username')
                entry_username.config(fg='grey', font=('Arial', 14, 'normal'))

        def on_password_focus_out(event):
            if entry_password.get() == '':
                entry_password.insert(0, 'Password')
                entry_password.config(fg='grey', font=('Arial', 14, 'normal'))

        # Main Frame
        frame = tk.Frame(self, bg='#4CAF50')
        frame.pack(expand=True)

        # Logo
        logo = tk.PhotoImage(file="suroko_logo.png")  # Placeholder for the logo image path
        logo_label = tk.Label(frame, image=logo, bg='#4CAF50')
        logo_label.grid(row=0, column=0, columnspan=3, pady=(10, 20))
        logo_label.image = logo  # Keep a reference to prevent garbage collection

        # Google Login Button
        google_button = tk.Button(frame, text="Login with Google", command=login_with_google, bg='#4285F4', fg='white', font=('Arial', 12), height=1, width=20)
        google_button.grid(row=1, column=0, columnspan=3, pady=5)

        signup_button = tk.Button(frame, text="Signup", command=signup, bg='#4285F4', fg='white', font=('Arial', 12), height=1, width=20)
        signup_button.grid(row=2, column=0, columnspan=3, pady=5)

        # OR Separator
        separator_frame = tk.Frame(frame, bg='#4CAF50')
        separator_frame.grid(row=3, column=0, columnspan=3, pady=5)
        separator_line_left = tk.Label(separator_frame, text=" " * 20, bg='#4CAF50')
        separator_line_left.pack(side=tk.LEFT)
        or_label = tk.Label(separator_frame, text="or", bg='#4CAF50', font=('Arial', 12))
        or_label.pack(side=tk.LEFT)
        separator_line_right = tk.Label(separator_frame, text=" " * 20, bg='#4CAF50')
        separator_line_right.pack(side=tk.LEFT)

        # Username Entry
        entry_username = tk.Entry(frame, font=('Arial', 14, 'bold'), width=30, fg='grey')
        entry_username.insert(0, 'Email/Username')
        entry_username.grid(row=4, column=0, columnspan=3, pady=5)
        entry_username.bind('<FocusIn>', on_entry_click)
        entry_username.bind('<FocusOut>', on_focus_out)

        # Password Entry
        entry_password = tk.Entry(frame, font=('Arial', 14), show='*', width=30)
        entry_password.insert(0, 'Password')
        entry_password.grid(row=5, column=0, columnspan=3, pady=5)
        entry_password.bind('<FocusIn>', on_password_entry_click)
        entry_password.bind('<FocusOut>', on_password_focus_out)

        # Forgot Password
        forgot_password_label = tk.Label(frame, text="Forgot password?", fg='#000000', bg='#4CAF50', font=('Arial', 10))
        forgot_password_label.grid(row=6, column=0, columnspan=3, pady=5)

        # Login Button
        login_button = tk.Button(frame, text="Login", command=login, bg='#4C8BF5', fg='white', font=('Arial', 12), height=1, width=10)
        login_button.grid(row=7, column=0, columnspan=3, pady=10)


