import random

# Python Quiz Questions List
questions = [
    {"question": "What does print(2**3) output?", "options": ["8", "6", "9", "7"], "answer": 8},
    {"question": "What is an example of a mutable type?", "options": ["String", "List", "Tuple", "None"], "answer": "List"},
    {"question": "How do you begin a comment in Python?", "options": ["#", "//", "/*", "'"], "answer": "#"},
    {"question": "Is 'nonlocal' a keyword in Python?", "options": ["Yes", "No", "Maybe", "Not Sure"], "answer": "Yes"},
    {"question": "What will print(3/2) output?", "options": ["1.5", "1", "2", "None of these"], "answer": "1.5"}
]

# Function to run the quiz
def run_quiz():
    score = 0  # Initialize score

    random.shuffle(questions)  # Shuffle questions to create a dynamic quiz session

    # Loop through the first 5 questions
    for i, q in enumerate(questions[:5]):
        print(f"Q{i+1}: {q['question']}")

        # Display options
        for idx, option in enumerate(q['options']):
            print(f"{idx+1}. {option}")

        # Take user's input and validate it
        while True:
            answer = input("Enter the correct option (1-4): ")
            if answer.isdigit() and 1 <= int(answer) <= len(q['options']):
                break  # A valid answer, exit the loop
            else:
                print("Invalid input! Enter a number from 1 to", len(q['options']))

        # Check the user's answer
        if q['options'][int(answer)-1] == str(q['answer']) or q['options'][int(answer)-1] == q['answer']:
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is: {q['answer']}\n")

    print(f"Quiz finished! Your total score is: {score}/{len(questions[:5])}")

# Run the quiz
run_quiz()