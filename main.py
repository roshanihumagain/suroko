import tkinter as tk
from PIL import Image, ImageTk
from home_page import HomePageFrame
from seats import Seats
from ticket_rates import TicketRatesFrame
from login_hall import Login
from about_us import AboutUs
from movie import Movie

# Initialize the main window
root = tk.Tk()
root.title("Suroko Cinemas")
root.geometry("1024x768")

# Top banner with logo, background image, and login
top_frame = tk.Frame(root, bg="#4CAF50", height=100)
top_frame.pack(fill="x")

# Logo on the left
logo_image = Image.open(r"logo2.png")
logo_image = logo_image.resize((100, 100), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(top_frame, image=logo_photo, bg="#4CAF50")
logo_label.pack(side="left", padx=10)

# Navigation bar with buttons aligned to the right
nav_frame = tk.Frame(top_frame, bg="#4CAF50")
nav_frame.pack(side="right")

nav_buttons = []

nav_buttons_texts = ["Home","Ticket Rates", "About Us", "Login"]
for btn_text in nav_buttons_texts:
    btn = tk.Button(nav_frame, text=btn_text, bg="#00796B", fg="white", relief="flat")
    nav_buttons.append(btn)
    btn.pack(side="left", padx=10, pady=20)

content_frames = []

see_more_buttons = []


homepage_frame = HomePageFrame(root)

content_frames.append(homepage_frame)
homepage_frame.pack(fill="both", expand=True)

ticket_rates_frame = TicketRatesFrame(root)
content_frames.append(ticket_rates_frame)

aboutUs_frame = AboutUs(root)
content_frames.append(aboutUs_frame)

movie_frame = Movie(root)
content_frames.append(movie_frame)
slot_button = movie_frame.get_slot_button()

ticket_booking_frame = Seats(root)
content_frames.append(ticket_booking_frame)

def home():
    global see_more_buttons  # Ensure you're using the global variable

    for frame in content_frames:
        frame.pack_forget()
    homepage_frame.pack(fill="both", expand=True)

    see_more_buttons.clear()
    see_more_buttons = homepage_frame.get_see_more_buttons()
    for button in see_more_buttons:
        button.config(command=seeMore)

def ticketRates(): 
    for frame in content_frames:
        frame.pack_forget()
    ticket_rates_frame.pack(fill="both", expand=True)
    
def aboutUs():
    for frame in content_frames:
        frame.pack_forget()
    aboutUs_frame.pack(fill="both", expand=True)
 
def login():
    loginWindow = Login(root)
    loginWindow.grab_set()  # Make this window modal

def seeMore():
    for frame in content_frames:
        frame.pack_forget()
    movie_frame.pack()


def seats():
    for frame in content_frames:
        frame.pack_forget()
    ticket_booking_frame.pack()

nav_buttons[0].config(command=home)
nav_buttons[1].config(command = ticketRates)
nav_buttons[2].config(command = aboutUs)
nav_buttons[3].config(command = login)

slot_button.config(command=seats)

def footer():
    footer_frame = tk.Frame(root, bg="#2E7D32", height=100)
    footer_frame.pack(fill="x", side="bottom")

    footer_labels = [
        ("Contact Us", ["Facebook"]),
        ("About Us", ["Suroko Cinemas"]),
        ("LINKS", ["Now Showing"]),
        ("INFORMATION", ["Terms And Conditions"])
    ]

    for section in footer_labels:
        section_frame = tk.Frame(footer_frame, bg="#2E7D32")
        section_frame.pack(side="left", padx=20, pady=20)
        
        section_label = tk.Label(section_frame, text=section[0], font=("Arial", 14), bg="#2E7D32", fg="white")
        section_label.pack(anchor="w")
        
        for item in section[1]:
            item_label = tk.Label(section_frame, text=item, font=("Arial", 10), bg="#2E7D32", fg="white")
            item_label.pack(anchor="w")

home()
footer()

root.mainloop()
