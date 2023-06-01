#Iteration 3

while True:
    # Define the list of questions
    questions = ("What year was the very first model of the iPhone released?: ",
                 "What does DC stand for?: ",
                 "How many Lord of the Rings films are there?: ",
                 "Who played Wolverine?: ",
                 "What country won the very first FIFA World Cup in 1930?: ")
    
    # Define the answer options for each question
    options = (("A. 2007", "B. 2006", "C. 2008", "D. 2005"),
               ("A. Detective Comics", "B. Death Comics", "C. Darkseid Comics", "D. Dino Comics"),
               ("A. 4", "B. 5", "C. 3", "D. 2"),
               ("A. Tom Hardy", "B. Hugh Jackman", "C. Chris Evans", "D. Ryan Reynolds"),
               ("A. Brazil", "B. England", "C. Uruguay", "D. France"))

    # Define the correct answers for each question
    answers = ("A", "A", "C", "B", "C")

    # Empty list to store the user's guesses
    guesses = []

    # Initialise the score and question number
    score = 0
    question_num = 0
    
    # Loop through each question
    for question in questions:
        print("----------------------")
        print(question)

        # Display the answer options for the current question
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

            # Add the user's guess to the list of guesses
            guesses.append(guess)

            # Check if the guess is correct and update the score accordingly
            if guess == answers[question_num]:
                score += 1
                print("CORRECT!")
            else:
                print("INCORRECT!")
                print(f"{answers[question_num]} is the correct answer")
            break

        # Move to the next question
        question_num += 1

      

    print("----------------------")
    print("        RESULTS       ")
    print("----------------------")

    # Display the correct answers
    print("answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()

    # Display the user's guesses
    print("guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    # Calculate and display the user's score
    score = int(score / len(questions) * 100)
    print(f"Your score is: {score}%")

    # Asks the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thank you for playing this Quiz! Bye.")
        break
