import tkinter as tk
from PIL import Image, ImageTk

# # Initialize the main window
# root = tk.Tk()
# root.title("About Us")
# root.geometry("1024x768")

class AboutUs(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Background image for top banner
        background_frame = tk.Frame(self, bg="", height=200)
        background_frame.pack(fill="x")

        background_image = Image.open(r"aboutus.png")
        background_image = background_image.resize((980, 270), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(background_frame, image=self.background_photo)
        background_label.pack(fill="both", expand=True)

        # Main content
        content_frame = tk.Frame(self, bg="#4CAF50", height=270)
        content_frame.pack(fill="x", expand=False, padx=20, pady=20)

        paragraph = (
            "The halls are equipped with cutting-edge technologies like Dolby 3-Ware Digital \n"
            "sound systems and digital 2K projection view. Considered to be among the most \n sophisticated "
            "and advanced equipment, these will bring forth the best picture and \n sound quality for the "
            "audience to enjoy. The super comfy seats and modern decor \n add a luxurious touch to this "
            "high-tech movie theater. No movie experience is \n complete without refreshments, and at SUROKO "
            "Cinemas, this need is \n also taken care of with its snack corner. Rest assured that watching \n"
            "movies at SUROKO Cinemas will be an audio-visual treat for the audience, \n which you can enjoy "
            "in a relaxed ambiance."
        )
        
        about_us_label = tk.Label(content_frame, text=paragraph, font=("Arial", 12), bg="#4CAF50", fg="white")
        about_us_label.grid(row=0, column=0,)

        # content poster
        image = Image.open("serving.png")
        resized_image = image.resize((400, 300), Image.LANCZOS)
        self.poster = ImageTk.PhotoImage(resized_image)
        poster_label = tk.Label(content_frame, image=self.poster, bg="#4CAF50")
        poster_label.grid(row=0, column=1, padx=5, pady=5)


# aboutUs = AboutUs(root)
# aboutUs.pack(fill="x", expand=True)

# root.mainloop()

