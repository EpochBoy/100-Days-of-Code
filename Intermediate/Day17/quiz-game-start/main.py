from data import question_data, open_trivia_db
from question_model import Question
from quiz_brain import Quiz

question_bank = []


def populate_bank():
    # Changed for loop to loop TriviaDB
    for i in open_trivia_db:
        # q = i["text"]
        # Modified for TriviaDB
        q = i["question"]
        # a = i["answer"]
        # Modified for TriviaDB
        a = i["correct_answer"]
        question = Question(q, a)
        question_bank.append(question)


def runner():
    populate_bank()
    quiz = Quiz(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()
        quiz.check_answer()
    else:
        print(f"Your final score was {quiz.score}")
        print("You've completed the quiz!\n\n")


runner()