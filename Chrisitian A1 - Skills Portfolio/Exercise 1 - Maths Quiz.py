# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 00:23:33 2024

@author: darel
"""

from tkinter import *
import random

class ArithmeticQuiz:
    def __init__(self, root):
        self.root = root  # Reference to the main window
        self.root.title("Arithmetic Quiz")  # Window title
        self.root.configure(bg="lightblue")  # Background color
        self.total_score = 0  # Total score starts at zero
        self.current_question = 0  # Track the current question number
        self.difficulty_level = None  # User's chosen difficulty level
        self.setup_menu()  # Show the difficulty selection menu

    def setup_menu(self):
        self.clear_screen()  # Clear any previous widgets
        title_label = Label(self.root, text="CHOOSE DIFFICULTY LEVEL", bg="lightblue", font=("Arial", 14))
        title_label.pack(pady=10)  # Difficulty menu title

        # Buttons for difficulty levels
        Button(self.root, text="1. Easy", font=("Arial", 12), command=lambda: self.start_quiz(1)).pack(pady=5)
        Button(self.root, text="2. Moderate", font=("Arial", 12), command=lambda: self.start_quiz(2)).pack(pady=5)
        Button(self.root, text="3. Advanced", font=("Arial", 12), command=lambda: self.start_quiz(3)).pack(pady=5)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()  # Remove all widgets from the current screen

    def start_quiz(self, level):
        self.difficulty_level = level  # Set difficulty
        self.total_score = 0  # Reset score
        self.current_question = 0  # Reset question count
        self.display_next_question()  # Start showing questions

    def generate_random_number(self):
        if self.difficulty_level == 1:
            return random.randint(1, 9)  # Easy level numbers
        elif self.difficulty_level == 2:
            return random.randint(10, 99)  # Moderate level numbers
        else:
            return random.randint(1000, 9999)  # Advanced level numbers

    def choose_operation(self):
        return random.choice(["+", "-"])  # Randomly choose addition or subtraction

    def show_question(self):
        self.num1 = self.generate_random_number()  # First number
        self.num2 = self.generate_random_number()  # Second number
        self.operation = self.choose_operation()  # Operation to perform
        self.correct_answer = eval(f"{self.num1} {self.operation} {self.num2}")  # Calculate answer

        # Display the question
        question_label = Label(self.root, text=f"Question {self.current_question + 1}: {self.num1} {self.operation} {self.num2} =", font=("Arial", 14), bg="lightblue")
        question_label.pack(pady=10)

        self.answer_entry = Entry(self.root, font=("Arial", 12))  # Entry for the user's answer
        self.answer_entry.pack(pady=5)
        submit_button = Button(self.root, text="Submit", font=("Arial", 12), command=self.check_user_answer)
        submit_button.pack(pady=5)  # Button to submit the answer

    def check_user_answer(self):
        user_answer = self.answer_entry.get()  # Get user input
        if user_answer.isdigit() and int(user_answer) == self.correct_answer:
            self.total_score += 10 if self.attempt == 1 else 5  # Update score
            self.display_next_question()  # Move to next question
        elif self.attempt == 1:
            self.attempt += 1  # Allow one more attempt
            self.answer_entry.delete(0, END)  # Clear input
        else:
            self.display_next_question()  # Move on after second attempt

    def display_next_question(self):
        self.clear_screen()  # Clear for next question
        self.attempt = 1  # Reset attempt counter
        if self.current_question < 10:
            self.show_question()  # Show next question
            self.current_question += 1  # Increment question count
        else:
            self.show_final_score()  # Show final score if done

    def show_final_score(self):
        # Determine grade based on score
        grade = "A+" if self.total_score >= 90 else "A" if self.total_score >= 80 else "B" if self.total_score >= 70 else "C" if self.total_score >= 60 else "D"
        result_label = Label(self.root, text=f"Your final score is {self.total_score}/100\nGrade: {grade}", font=("Arial", 14), bg="lightblue")
        result_label.pack(pady=10)  # Display score and grade

        play_again_button = Button(self.root, text="Play Again", font=("Arial", 12), command=self.setup_menu)
        play_again_button.pack(pady=5)  # Button to restart quiz

root = Tk()
app = ArithmeticQuiz(root)  # Create an instance of the quiz
root.mainloop()  # Start the main event loop
