# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 00:47:49 2024

@author: darel
"""

from tkinter import *  # Importing Tkinter for GUI
import random  # To select jokes randomly

# New list of jokes
jokes = [
    ("What do you call cheese that isn't yours?", "Nacho cheese!"),
    ("Why did the computer go to the doctor?", "It had a virus!"),
    ("Why did the golfer bring two pairs of pants?", "In case he got a hole in one!"),
    ("Why don't skeletons fight each other?", "They don't have the guts!"),
    ("What did the grape do when it got stepped on?", "Nothing, it just let out a little wine!"),
    ("Why did the teddy bear say no to dessert?", "Because it was stuffed!"),
    ("What did one plate say to another plate?", "Dinner's on me!"),
    ("Why was the broom late?", "It swept in!"),
    ("Why can't you give Elsa a balloon?", "Because she will let it go!"),
    ("What do you call a bear with no teeth?", "A gummy bear!"),
]

class JokeApp:
    def __init__(self, master):
        self.master = master
        master.title("Joke Teller")  # Setting up the window title
        master.configure(bg="yellow")  # Set the background color to yellow

        # Create a frame for green background
        green_frame = Frame(master, bg="green")
        green_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Create a frame for blue background
        blue_frame = Frame(green_frame, bg="blue")
        blue_frame.pack(pady=20, padx=20)

        self.joke_label = Label(blue_frame, text="", wraplength=300, bg="blue", fg="white")  # For the joke setup
        self.joke_label.pack(pady=20)

        self.punchline_label = Label(blue_frame, text="", wraplength=300, bg="blue", fg="white")  # For the punchline
        self.punchline_label.pack(pady=20)

        self.setup_button = Button(blue_frame, text="Tell me a joke", command=self.display_joke)  # Button for a new joke
        self.setup_button.pack(pady=10)

        self.punchline_button = Button(blue_frame, text="Show punchline", command=self.show_punchline)  # Button to reveal the punchline
        self.punchline_button.pack(pady=10)

        self.quit_button = Button(blue_frame, text="Quit", command=master.quit)  # Button to exit the app
        self.quit_button.pack(pady=10)

        self.current_joke = None  # To store the current joke

    def display_joke(self):
        self.current_joke = random.choice(jokes)  # Get a random joke
        self.joke_label.config(text=self.current_joke[0])  # Show the setup
        self.punchline_label.config(text="")  # Clear the punchline

    def show_punchline(self):
        if self.current_joke:  # If there's a joke
            self.punchline_label.config(text=self.current_joke[1])  # Show the punchline

# Running the app
if __name__ == "__main__":
    root = Tk()  # Create the main window
    app = JokeApp(root)  # Instantiate the joke app
    root.mainloop()  # Start the GUI loop