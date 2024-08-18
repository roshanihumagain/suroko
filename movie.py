import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Initialize the main window
# root = tk.Tk()
# root.title("Movie")
# root.geometry("1024x768")

class Movie(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        style = ttk.Style()
        style.configure("Treeview", rowheight=30) 

        # Create left and right frames and pack them side by side
        left_frame = tk.Frame(self, bg="#4CAF50", width=350, height=500)
        left_frame.pack(side="left", fill="y", expand=True, padx=5, pady=5)
        
        right_frame = tk.Frame(self, bg="#4CAF50", width=350, height=500)
        right_frame.pack(side="left", fill="y", expand=True, padx=5, pady=5)
        right_frame.pack_propagate(False)
        
        image = Image.open("despicable.jpg")
        resized_image = image.resize((350, 250), Image.LANCZOS)
        self.poster = ImageTk.PhotoImage(resized_image)
        poster_label = tk.Label(left_frame, image=self.poster, bg="#4CAF50")
        poster_label.pack(pady=10)
        
        # Info Frame
        info_frame = tk.Frame(left_frame, bg="#4CAF50")
        info_frame.pack(fill="both", expand=True)

        # Treeview for the info table
        tree = ttk.Treeview(info_frame, columns=("Attribute", "Value"), show="headings", height=5)

        # Define the column headings
        tree.heading("Attribute", text="Attribute")
        tree.heading("Value", text="Value")

        # Set the width of the columns
        tree.column("Attribute", anchor="w", width=150)
        tree.column("Value", anchor="w", width=200)

        # Sample data for the treeview
        data = [
            ("Releasing Date:", "Aug 02, 2024"),
            ("Run Time:", "2 Hrs 25 Min"),
            ("Director:", "Neeraj Pandey"),
            ("Genre:", "Action Drama Romance"),
            ("Cast:", "Ajay Devgn, Tabu, Jimmy Shergill")
        ]

        # Insert data into the treeview
        for item in data:
            tree.insert("", "end", values=item)

        # Pack the treeview inside the info frame
        tree.pack(fill="both", expand=True)

        #Right Frame
        today_label = tk.Label(right_frame, text="TODAY", font=("Arial", 35), bg="#4CAF50" ,fg="white")
        today_label.pack(anchor= "center", pady=10)
        
        movie_title = tk.Label(right_frame, text="Despicable Me 4", font=("Arial", 24), bg="#4CAF50" ,fg="white")
        movie_title.pack(anchor= "w", pady=10)
        
        movie_desc_text = "Anti-Villain League (AVL) agent Gru attends a reunion at \n his alma mater, Lycée Pas Bon."
        movie_desc = tk.Label(right_frame, text= movie_desc_text, font=("Arial", 10), bg="#4CAF50" ,fg="white")
        movie_desc.pack(anchor= "w", pady=10)
        
        self.slot = tk.Button(right_frame, text="7 : 00 AM", bg="#00796B", fg="white", relief="flat", height=5, width=10)
        self.slot.pack(anchor="w", padx=10, pady=10)


    def get_slot_button(self):
        return self.slot        
# movie = Movie(root)
# movie.pack(expand=True)

# root.mainloop()
