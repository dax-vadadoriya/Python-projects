questions = [
    {
        "question": "What is the output of 2 + 3?",
        "options": ["4", "5", "6", "7"],
        "answer": "2"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "3"
    },
    {
        "question": "Which data type stores multiple items in an ordered collection?",
        "options": ["List", "Integer", "Boolean", "Float"],
        "answer": "1"
    },
    {
        "question": "Which symbol is used for multiplication in Python?",
        "options": ["x", "*", "%", "#"],
        "answer": "2"
    },
    {
        "question": "What does len() do?",
        "options": [
            "Deletes an item",
            "Adds an item",
            "Returns the number of items",
            "Sorts a list"
        ],
        "answer": "3"
    }
]


def run_quiz():
    score = 0

    print("===== PYTHON QUIZ =====")

    for index, question in enumerate(questions, start=1):
        print(f"\nQuestion {index}:")
        print(question["question"])

        for option_index, option in enumerate(question["options"], start=1):
            print(f"{option_index}. {option}")

        while True:
            user_answer = input("Your answer (1-4): ")

            if user_answer in ["1", "2", "3", "4"]:
                break

            print("Invalid choice. Enter 1, 2, 3, or 4.")

        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            correct_option = int(question["answer"]) - 1
            correct_answer = question["options"][correct_option]

            print("Wrong!")
            print(f"Correct answer: {correct_answer}")

    total_questions = len(questions)
    percentage = (score / total_questions) * 100

    print("\n===== RESULT =====")
    print(f"Score: {score}/{total_questions}")
    print(f"Percentage: {percentage:.1f}%")

    if percentage == 100:
        print("Excellent!")
    elif percentage >= 60:
        print("Good job!")
    else:
        print("Keep practicing!")


run_quiz()
