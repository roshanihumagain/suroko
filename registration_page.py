import tkinter as tk
from tkinter import messagebox

class Registration(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # Initialize the registration window
        self.title("Signup - Suroko Cinemas")
        self.geometry("400x500")
        self.configure(bg="#34A94D")

        frame = tk.Frame(self, bg="#34A94D", padx=20, pady=20)
        frame.pack(pady=50)

        label_registration = tk.Label(frame, text="Let's signup", fg="black", bg="#34A94D", font=("Arial", 15))
        label_registration.grid(row=0, column=0, pady=5, sticky="w")

        label_first_name = tk.Label(frame, text="First Name", fg="black", bg="#34A94D", font=("Arial", 12))
        label_first_name.grid(row=1, column=0, pady=5, sticky="w")
        self.entry_first_name = tk.Entry(frame, width=30)
        self.entry_first_name.grid(row=1, column=1, pady=5)

        label_last_name = tk.Label(frame, text="Last Name", fg="black", bg="#34A94D", font=("Arial", 12))
        label_last_name.grid(row=2, column=0, pady=5, sticky="w")
        self.entry_last_name = tk.Entry(frame, width=30)
        self.entry_last_name.grid(row=2, column=1, pady=5)

        label_email = tk.Label(frame, text="Email", fg="black", bg="#34A94D", font=("Arial", 12))
        label_email.grid(row=3, column=0, pady=5, sticky="w")
        self.entry_email = tk.Entry(frame, width=30)
        self.entry_email.grid(row=3, column=1, pady=5)

        label_mobile = tk.Label(frame, text="Mobile Number", fg="black", bg="#34A94D", font=("Arial", 12))
        label_mobile.grid(row=4, column=0, pady=5, sticky="w")
        self.entry_mobile = tk.Entry(frame, width=30)
        self.entry_mobile.grid(row=4, column=1, pady=5)

        label_password = tk.Label(frame, text="Password", fg="black", bg="#34A94D", font=("Arial", 12))
        label_password.grid(row=5, column=0, pady=5, sticky="w")
        self.entry_password = tk.Entry(frame, width=30, show="*")
        self.entry_password.grid(row=5, column=1, pady=5)

        label_confirm_password = tk.Label(frame, text="Confirm Password", fg="black", bg="#34A94D", font=("Arial", 12))
        label_confirm_password.grid(row=6, column=0, pady=5, sticky="w")
        self.entry_confirm_password = tk.Entry(frame, width=30, show="*")
        self.entry_confirm_password.grid(row=6, column=1, pady=5)

        self.var_agree_terms = tk.IntVar()
        checkbox_agree_terms = tk.Checkbutton(frame, text="I agree to the terms and conditions.", variable=self.var_agree_terms, bg="#34A94D", font=("Arial", 10))
        checkbox_agree_terms.grid(row=7, columnspan=2, pady=10)

        button_submit = tk.Button(frame, text="SUBMIT", command=self.register, bg="#0D954B", fg="white", width=10, font=("Arial", 12))
        button_submit.grid(row=8, columnspan=2, pady=10)

        label_close = tk.Label(frame, text="Close", fg="black", bg="#34A94D", font=("Arial", 12))
        label_close.grid(row=9, columnspan=2, pady=10)
        label_close.bind("<Button-1>", lambda e: self.close_window())

        # Handle the window close button
        self.protocol("WM_DELETE_WINDOW", self.close_window)


    def close_window(self):
        self.grab_release()
        self.parent.grab_set()
        self.destroy()

    def register(self):
        try:
            first_name = self.entry_first_name.get().strip()
            last_name = self.entry_last_name.get().strip()
            email = self.entry_email.get().strip()
            mobile = self.entry_mobile.get().strip()
            password = self.entry_password.get().strip()
            confirm_password = self.entry_confirm_password.get().strip()
            agree_terms = str(self.var_agree_terms.get())
            
            if not all([first_name, last_name, email, mobile, password, confirm_password]):
                raise ValueError("All fields must be filled out.")
            
            if "@" not in email:
                raise ValueError("Please enter a valid email address.")

            if password != confirm_password:
                raise ValueError("Passwords do not match.")

            if not int(agree_terms):
                raise ValueError("You must agree to the terms and conditions.")
            
            mobile_num = int(mobile)
            if len(str(mobile)) != 10:
                raise ValueError("Invalid mobile number. It should be a 10-digit number.")

            self.updateInTextFile(first_name, last_name, email, mobile, password)
            messagebox.showinfo("Registration", "Registration Succesfull")
        
            self.close_window()

        except ValueError as ve:
            messagebox.showerror("Error", str(ve))

    def updateInTextFile(self, first_name, last_name,email,mobile,password):
            with open("registration_data.txt", "a") as file:
                file.write(f"First Name: {first_name}, ")
                file.write(f"Last Name: {last_name}, ")
                file.write(f"Email: {email}, ")
                file.write(f"Mobile: {mobile}, ")
                file.write(f"Password: {password}")
                file.write("\n")
