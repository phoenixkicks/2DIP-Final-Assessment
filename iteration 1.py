# Iteration 1


# Using tuple to define the questions
questions = ("What year was the very first model of the iPhone released?: ",
             "What does DC stand for?: ",
             "How many Lord of the Rings films are there?: ",
             "Who played Wolverine?: ",
             "What country won the very first FIFA World Cup in 1930?: ")

# Using a tuple of tuples to define the answer options
options = (("A. 2007", "B. 2006", "C. 2008", "D. 2005"),
           ("A. Detective Comics", "B. Death Comics", "C. Darkseid Comics", "D. Dino Comics"),
           ("A. 4", "B. 5", "C. 3", "D. 2"),
           ("A. Tom Hardy", "B. Hugh Jackman", "C. Chris Evans", "D. Ryan Reynolds"),
           ("A. Brazil", "B. England", "C. Uruguay", "D. France"))

# Using a tuple to define the correct answers to the questions
answers = ("A", "A", "C", "B", "C")

# Empty list which will store the user's guesses
guesses = []

# Initialise the question number
question_num = 0


# Loop through each question
for question in questions:
    print("----------------------")
    print(question)

    # Loop thorugh each answer option for the current question
    for option in options[question_num]:
        print(option)

    # Keeps asking the user's input until the input a valid answer that is (A, B, C, or D) 
    while True:
        guess = input("Enter (A, B, C, D): ").upper()
        if guess not in ['A', 'B', 'C', 'D']:
            print("Invalid input. Please enter A, B, C, or D.")
            continue

        # Adds the user's guess to the list of guesses
        guesses.append(guess)

        # Checks if the guess is correct
        if guess == answers[question_num]:
           
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{answers[question_num]} is the correct answer")

        # Breaks out of the loop and moves on to the next question
        break
    
    # Increments the question number for the next question
    question_num += 1



