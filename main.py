from questions.python_questions import python_questions


GAME_TITLE = "TEAM PYTHON QUIZ"


def show_welcome():
    print()
    print("=" * 40)
    print(GAME_TITLE)
    print("=" * 40)
    print()


def ask_question(question):
    print(question["question"])

    for index, answer in enumerate(question["answers"], start=1):
        print(f"{index}. {answer}")

    choice = input("Your answer: ").strip()

    if not choice.isdigit():
        print("Invalid answer.")
        return False

    choice_index = int(choice) - 1

    if choice_index < 0 or choice_index >= len(question["answers"]):
        print("Invalid answer.")
        return False

    selected_answer = question["answers"][choice_index]

    if selected_answer == question["correct"]:
        print("Correct!")
        return True

    print(f'Wrong. Correct answer: {question["correct"]}')
    return False


def run_quiz(questions):
    score = 0

    for question in questions:
        print()

        if ask_question(question):
            score += 1

    print()
    print(f"Final score: {score}/{len(questions)}")


def main():
    show_welcome()
    run_quiz(python_questions)


if __name__ == "__main__":
    main()