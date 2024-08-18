import tkinter as tk
from PIL import Image, ImageTk

# # Initialize the main window
# root = tk.Tk()
# root.title("Suroko Cinemas")
# root.geometry("1024x768")

class HomePageFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.see_more_buttons = []

        # Background image for top banner
        background_frame = tk.Frame(self, bg="", height=200)
        background_frame.pack(fill="x")

        background_image = Image.open(r"cover_image.png")
        background_image = background_image.resize((1024, 200), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(background_frame, image=self.background_photo)
        background_label.pack(fill="both", expand=True)

        # Main content
        content_frame = tk.Frame(self, bg="#4CAF50")
        content_frame.pack(fill="x", expand=False, padx=20, pady=20)

        # Now Showing section
        now_showing_label = tk.Label(content_frame, text="Now Showing", font=("Arial", 20), bg="#4CAF50", fg="white")
        now_showing_label.pack(anchor="w", pady=5)

        movies_frame = tk.Frame(content_frame, bg="#4CAF50")
        movies_frame.pack(fill="x")

        # Add movie posters
        movies = [
            ("Despicable Me 4", r"movie1.png"),
            ("Gaun Aayeko Bato", r"movie2.png"),
            ("Kalki", r"movie3.png"),
            ("Kill", r"movie4.png")
        ]

        # Get the size of the first image
        first_image_path = movies[0][1]
        first_image = Image.open(first_image_path)
        image_width, image_height = first_image.size

        for movie in movies:
            movie_frame = tk.Frame(movies_frame, bg="#4CAF50")
            movie_frame.pack(side="left", padx=10)

            # Resize images to the size of the first image
            image = Image.open(movie[1])
            resized_image = image.resize((image_width, image_height), Image.LANCZOS)
            poster = ImageTk.PhotoImage(resized_image)
            poster_label = tk.Label(movie_frame, image=poster, bg="#4CAF50")
            poster_label.image = poster  # Keep a reference
            poster_label.pack(pady=10)
            
            title_label = tk.Label(movie_frame, text=movie[0], font=("Arial", 14), bg="#4CAF50", fg="white")
            title_label.pack(pady=3)
            
            see_more_button = tk.Button(movie_frame, text="See More", bg="#00796B", fg="white")
            see_more_button.pack(pady=5)
            self.see_more_buttons.append(see_more_button)

    def get_see_more_buttons(self):
        return self.see_more_buttons


# homepage = HomePageFrame(root)
# homepage.pack(fill="x", expand=True)

# # Start the Tkinter main loop
# root.mainloop()

