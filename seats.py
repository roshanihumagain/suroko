import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Initialize the main window
# root = tk.Tk()
# root.title("Movie")
# root.geometry("1024x768")

class Seats(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # List to keep track of selected seats
        self.selected_seats = []
        self.rate = 350    

        # Create left and right frames and pack them side by side
        left_frame = tk.Frame(self, bg="#4CAF50", width=600, height=500)
        left_frame.pack(side="left", fill="y", expand=True, padx=5, pady=5)
        
        right_frame = tk.Frame(self, bg="#4CAF50", width=300, height=500)
        right_frame.pack(side="left", fill="y", expand=True, padx=5, pady=5)
        right_frame.pack_propagate(False)
        
        # Add buttons to the left_frame
        rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        for i, row in enumerate(rows):
            for j, col in enumerate(columns):
                button_text = f"{row}{col}"
                seat_button = tk.Button(
                    left_frame, 
                    text=button_text, 
                    width=4, 
                    height=2, 
                    bg="lightgray"
                )
                seat_button.grid(row=i, column=j, padx=5, pady=5)
                seat_button.config(command=lambda btn=seat_button: self.toggle_seat(btn))

        # Right Frame - Labels
        self.number_label = tk.Label(right_frame, text="No. of Seats: 0", font=("Arial", 20), bg="#4CAF50" ,fg="white")
        self.number_label.pack(anchor="center", pady=10)

        self.price_label = tk.Label(right_frame, text="Total Price: 0", font=("Arial", 20), bg="#4CAF50" ,fg="white")
        self.price_label.pack(anchor="center", pady=10)

        self.seats_label = tk.Label(right_frame, text="Selected Seats: None", font=("Arial", 14), bg="#4CAF50" ,fg="white", wraplength=250)
        self.seats_label.pack(anchor="center", pady=10)
    
    def toggle_seat(self, button):
        seat_id = button.cget("text")

        if seat_id in self.selected_seats:
            # Deselect seat
            button.config(bg="lightgray")
            self.selected_seats.remove(seat_id)
        else:
            # Select seat
            button.config(bg="yellow")
            self.selected_seats.append(seat_id)

        # Update the display after toggling the seat
        self.update_display()

    def update_display(self):
        # Update the number of selected seats
        self.number_label.config(text=f"No. of Seats: {len(self.selected_seats)}")
        
        # Update the total price
        total_price = len(self.selected_seats) * self.rate
        self.price_label.config(text=f"Total Price: {total_price}")
        
        # Update the selected seats label
        if self.selected_seats:
            selected_seats_text = ", ".join(self.selected_seats)
        else:
            selected_seats_text = "None"
        self.seats_label.config(text=f"Selected Seats: {selected_seats_text}")


# Create the Seats instance and pack it
# movie = Seats(root)
# movie.pack(expand=True)

# root.mainloop()
