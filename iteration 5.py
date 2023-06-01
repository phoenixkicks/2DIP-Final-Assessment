import tkinter as tk
from tkinter import messagebox


# Define the questions
questions = (
    "What year was the very first model of the iPhone released?: ",
    "What does DC stand for?: ",
    "How many Lord of the Rings films are there?: ",
    "Who played Wolverine?: ",
    "What country won the very first FIFA World Cup in 1930?: "
)

# Define the answer options for each question
options = (
    ("A. 2007", "B. 2006", "C. 2008", "D. 2005"),
    ("A. Detective Comics", "B. Death Comics", "C. Darkseid Comics", "D. Dino Comics"),
    ("A. 4", "B. 5", "C. 3", "D. 2"),
    ("A. Tom Hardy", "B. Hugh Jackman", "C. Chris Evans", "D. Ryan Reynolds"),
    ("A. Brazil", "B. England", "C. Uruguay", "D. France")
)

# Define the correct answers for each question
answers = ("A", "A", "C", "B", "C")

# Keeps list of the user's guesses and current question number
guesses = []
question_num = 0

# Function to submit the user's answer
def submit_answer():
    global question_num
    guess = guess_var.get().upper()

    # Validate the guess as a valid option
    if guess not in ['A', 'B', 'C', 'D']:
        messagebox.showerror("Invalid Answer", "Please enter a valid answer (A, B, C, or D).")
        return

    
    guesses.append(guess)

    # Checks if the guess is correct and provide comment
    if guess == answers[question_num]:
        result_label.config(text="CORRECT!", fg="green")
    else:
        result_label.config(text="INCORRECT! The correct answer is " + answers[question_num], fg="red")

    # Move to the next question or finish the quiz
    question_num += 1
    if question_num < len(questions):
        question_label.config(text=questions[question_num])
        option_menu['menu'].delete(0, 'end')
        for option in options[question_num]:
            option_menu['menu'].add_command(label=option, command=tk._setit(option_var, option))
        guess_var.set('')
    else:
        finish_quiz()

# Function to finish the quiz
def finish_quiz():
    # Display a message box with the quiz results
    messagebox.showinfo(
        "Quiz Completed",
        "Quiz completed!\n\nAnswers: "
        + " ".join(answers)
        + "\nGuesses: "
        + " ".join(guesses)
    )
    
    # Ask the user if they want to play again
    play_again = messagebox.askquestion("Play Again", "Do you want to play again?")
    if play_again == "yes":
        restart_quiz()
    else:
        # Display a goodbye message and close the window
        messagebox.showinfo("Quiz Ended", "Thank you for playing this Quiz! Bye.")
        window.destroy()

# Function to restart the quiz
def restart_quiz():
    global guesses, question_num
    guesses = []
    question_num = 0
    question_label.config(text=questions[question_num])
    option_menu['menu'].delete(0, 'end')
    for option in options[question_num]:
        option_menu['menu'].add_command(label=option, command=tk._setit(option_var, option))
    guess_var.set('')
    result_label.config(text="")

# Create the main window
window = tk.Tk()
window.title("Quiz")

# Quiz question frame
question_frame = tk.Frame(window)
question_frame.pack(pady=10)

question_label = tk.Label(question_frame, text=questions[question_num], wraplength=350)
question_label.pack(fill="both")

option_var = tk.StringVar()
option_var.set(options[question_num][0])  # Set the default option

# Create a dropdown box for answer options
option_menu = tk.OptionMenu(question_frame, option_var, *options[question_num])
option_menu.pack(pady=10)

# User's guess frame
guess_frame = tk.Frame(window)
guess_frame.pack(pady=10)

guess_var = tk.StringVar()
guess_entry = tk.Entry(guess_frame, textvariable=guess_var)
guess_entry.pack()

submit_button = tk.Button(guess_frame, text="Submit", command=submit_answer)
submit_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
