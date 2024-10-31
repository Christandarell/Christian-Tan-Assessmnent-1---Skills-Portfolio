# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 00:44:31 2024

@author: darel
"""

from tkinter import *  # Tkinter for GUI
from tkinter import messagebox, ttk  # Message box and combo box

# student data with Filipino and Japanese names
students = [
    {'name': 'Juan dela Cruz', 'number': 9384, 'coursework': 19, 'exam': 33},
    {'name': 'Yuki Tanaka', 'number': 1234, 'coursework': 75, 'exam': 82},
    {'name': 'Maria Clara', 'number': 4321, 'coursework': 62, 'exam': 70},
    {'name': 'Hana Saito', 'number': 5678, 'coursework': 88, 'exam': 91},
    {'name': 'Pedro Gonzales', 'number': 9876, 'coursework': 55, 'exam': 60},
    {'name': 'Sakura Yamamoto', 'number': 1357, 'coursework': 70, 'exam': 80},
    {'name': 'Jose Rizal', 'number': 2468, 'coursework': 45, 'exam': 52},
    {'name': 'Aiko Suzuki', 'number': 1122, 'coursework': 83, 'exam': 77},
    {'name': 'Andres Bonifacio', 'number': 3344, 'coursework': 90, 'exam': 94},
    {'name': 'Emiko Watanabe', 'number': 5566, 'coursework': 50, 'exam': 48},
    {'name': 'Liam Garcia', 'number': 1350, 'coursework': 65, 'exam': 70},  # Added extra student
    {'name': 'Emma Rodriguez', 'number': 2460, 'coursework': 85, 'exam': 90},
]

# calculate percentage and grade
def calculate_results(student):
    total = student['coursework'] + student['exam']
    percentage = (total / 160) * 100
    if percentage >= 70:
        grade = 'A'
    elif percentage >= 60:
        grade = 'B'
    elif percentage >= 50:
        grade = 'C'
    elif percentage >= 40:
        grade = 'D'
    else:
        grade = 'F'
    return percentage, grade

# view all student records
def view_all_records():
    records = ""
    for student in students:
        percentage, grade = calculate_results(student)
        records += (f"Name: {student['name']}\n"
                    f"Number: {student['number']}\n"
                    f"Coursework Total: {student['coursework']}\n"
                    f"Exam Mark: {student['exam']}\n"
                    f"Overall Percentage: {percentage:.2f}%\n"
                    f"Grade: {grade}\n\n")
    messagebox.showinfo("All Student Records", records)

# display individual student record
def view_student_record():
    selected_student = student_combo.get()
    if not selected_student:
        messagebox.showwarning("Selection Error", "Please select a student!")
        return
    student = next(s for s in students if s['name'] == selected_student)
    percentage, grade = calculate_results(student)
    output = (f"Name: {student['name']}\n"
              f"Number: {student['number']}\n"
              f"Coursework Total: {student['coursework']}\n"
              f"Exam Mark: {student['exam']}\n"
              f"Overall Percentage: {percentage:.2f}%\n"
              f"Grade: {grade}")
    student_details_label.config(text=output)

# Show highest score
def show_highest_score():
    highest_student = max(students, key=lambda s: s['coursework'] + s['exam'])
    view_student(highest_student)

# Show lowest score
def show_lowest_score():
    lowest_student = min(students, key=lambda s: s['coursework'] + s['exam'])
    view_student(lowest_student)

# View student details
def view_student(student):
    percentage, grade = calculate_results(student)
    output = (f"Name: {student['name']}\n"
              f"Number: {student['number']}\n"
              f"Coursework Total: {student['coursework']}\n"
              f"Exam Mark: {student['exam']}\n"
              f"Overall Percentage: {percentage:.2f}%\n"
              f"Grade: {grade}")
    messagebox.showinfo("Student Record", output)

# Create main application window
root = Tk()
root.title("Student Manager")
root.geometry("500x400")
root.configure(bg="#f0f8ff")

# Title Label
title_label = Label(root, text="Student Manager", font=("Arial", 16), bg="#f0f8ff")
title_label.pack(pady=10)

# Frame for buttons
btn_frame = Frame(root, bg="#f0f8ff")
btn_frame.pack(pady=10)

# Buttons for actions
view_all_btn = Button(btn_frame, text="View All Student Records", command=view_all_records, width=20, bg="#add8e6", fg="black")
view_all_btn.grid(row=0, column=0, padx=10, pady=5)

highest_score_btn = Button(btn_frame, text="Show Highest Score", command=show_highest_score, width=20, bg="#add8e6", fg="black")
highest_score_btn.grid(row=0, column=1, padx=10, pady=5)

lowest_score_btn = Button(btn_frame, text="Show Lowest Score", command=show_lowest_score, width=20, bg="#add8e6", fg="black")
lowest_score_btn.grid(row=0, column=2, padx=10, pady=5)

# Dropdown menu for individual student
student_label = Label(root, text="View Individual Student Record:", font=("Arial", 12), bg="#f0f8ff")
student_label.pack(pady=10)

student_combo = ttk.Combobox(root, values=[s['name'] for s in students], state="readonly", width=20)
student_combo.pack()

view_record_btn = Button(root, text="View Record", command=view_student_record, bg="#add8e6", fg="black")
view_record_btn.pack(pady=5)

# Label to display student details
student_details_label = Label(root, text="", font=("Arial", 10), justify="left", bg="#f0f8ff")
student_details_label.pack(pady=10)

# Run the tkinter event loop
root.mainloop()  # Start the GUI
