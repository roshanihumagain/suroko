import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Initialize the main window
# root = tk.Tk()
# root.title("Suroko Cinemas")
# root.geometry("1024x768")

class TicketRatesFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Configure the style for Treeview to change the row height
        style = ttk.Style()
        style.configure("Treeview", rowheight=30)  # Change the row height to 30 pixels

        # Background image for top banner
        background_frame = tk.Frame(self, bg="#4CAF50", height=200)
        background_frame.pack(fill="x")

        background_image = Image.open(r"suruko_theatre.png")
        background_image = background_image.resize((1024, 300), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(background_frame, image=self.background_photo)
        background_label.pack(fill="both", expand=True)

        # Price Table
        content_frame = tk.Frame(self, bg="#4CAF50")
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Treeview for the price table
        columns = ("Ticket Categories", "GOLD(Cube 1 & 2)", "PLATINUM(Cube 3)", "PREMIUM(Cube 3)")
        tree = ttk.Treeview(content_frame, columns=columns, show="headings", height=5)

        for col in columns:
            tree.heading(col, text=col, anchor="w")
            tree.column(col, width=200, anchor="w")

            if col == "Ticket Categories":
                tree.column(col, width=350, anchor="w")

        # Table data
        data = [
            ("Morning Shows (Everyday, 6 AM - 9 AM)", "NRs. 220.00", "NRs. 300.00", "NRs. 325.00"),
            ("Weekday Shows (Monday & Thursday)", "NRs. 350.00", "NRs. 450.00", "NRs. 500.00"),
            ("Weekend Shows(Friday To Sunday)", "NRs. 440.00", "NRs. 550.00", "NRs. 600.00"),
            ("Public Holiday Shows", "NRs. 440.00", "NRs. 550.00", "NRs. 600.00"),
            ("New Movie Release on weekdays", "NRs. 440.00", "NRs. 550.00", "NRs. 600.00"),
            ("Two Days Fun Days(Tuesday and Wednesday)", "NRs. 220.00", "NRs. 300.00", "NRs. 325.00")
        ]

        # Insert data into table
        for item in data:
            tree.insert("", "end", values=item)

        # Pack the treeview after the background image is fully packed
        tree.pack(fill="both", expand=True)
        
# # Create an instance of the TicketRatesFrame and pack it
# ticketRatesFrame = TicketRatesFrame(root)
# ticketRatesFrame.pack(fill="x", expand=True)

# # Start the Tkinter main loop
# root.mainloop()
