#Iteration 4

# Dictionary to store the user's username and password
user_details = {}

# Registration process
while True:
    username = input("Enter your Username: ")
    password = input("Enter your Password: ")

    if username.strip() == "" or password.strip() == "":
        print("Username or password cannot be blank. Please try again.")
    elif username in user_details:
        print("Username already exists. Please choose a different username.")
    else:
        user_details[username] = password
        print("Registration successful")
        break

# Login process
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in user_details and user_details[username] == password:
        print("Login successful!")
        break
    else:
        print("Invalid username or password. Please try again.")

# Quiz
while True:
    # Defining the questions, options, and the correct answers
    questions = ("What year was the very first model of the iPhone released?: ",
                 "What does DC stand for?: ",
                 "How many Lord of the Rings films are there?: ",
                 "Who played Wolverine?: ",
                 "What country won the very first FIFA World Cup in 1930?: ")

    options = (("A. 2007", "B. 2006", "C. 2008", "D. 2005"),
               ("A. Detective Comics", "B. Death Comics", "C. Darkseid Comics", "D. Dino Comics"),
               ("A. 4", "B. 5", "C. 3", "D. 2"),
               ("A. Tom Hardy", "B. Hugh Jackman", "C. Chris Evans", "D. Ryan Reynolds"),
               ("A. Brazil", "B. England", "C. Uruguay", "D. France"))

    # Define the correct answers for each question
    answers = ("A", "A", "C", "B", "C")

    
    # Empty list to store the user's guesses
    guesses = []

    # Initialise the the score and question number
    score = 0
    question_num = 0

    # Loop through each question
    for question in questions:
        print("----------------------")
        print(question)

        # Display answer options for the current question
        for option in options[question_num]:
            print(option)

        # Keep asking for the user's input until a valid answer (A, B, C, D, or S) is provided    
        while True:
            guess = input("Enter (A, B, C, D) to answer or 'S' to skip: ").upper()
            if guess not in ['A', 'B', 'C', 'D', 'S']:
                print("Invalid input. Please enter A, B, C, D, or S.")
                continue

            # If the user chooses to skip the question, move on to the next question
            if guess == 'S':
                print("Question skipped.")
                guesses.append(guess)
                break

            # Adds the user's guess to the list of guesses
            guesses.append(guess)

            # Check if the guess if correct
            if guess == answers[question_num]:
                score += 1
                print("CORRECT!")
            else:
                print("INCORRECT!")
                print(f"{answers[question_num]} is the correct answer")
            break

        question_num += 1
        


    print("----------------------")
    print("        RESULTS       ")
    print("----------------------")

    # Displays the correct answers
    print("answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()

    # Displays the user's guesses
    print("guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    # Displays the user's score
    score = int(score / len(questions) * 100)
    print(f"Your score is: {score}%")

    # Ask if the user wants to play again
    while True:
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            break
        elif play_again.lower() == "no":
            print("Thank you for playing this Quiz! Bye.")
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
