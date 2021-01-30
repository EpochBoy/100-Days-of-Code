class Quiz:
    def __init__(self, question_bank):
        self.question_nr = 0
        self.score = 0
        self.question_list = question_bank

    def next_question(self):
        self.answer = input(
            f"Q.{self.question_nr+1}: {self.question_list[self.question_nr].question}: (True/False)?: "
        )
        self.question_nr += 1

    def still_has_questions(self):
        # Shorthand from angela:
        return self.question_nr < len(self.question_list)
        # if self.question_nr < len(self.question_list) - 1:
        #     return True
        # else:
        #     return False

    def check_answer(self):
        if (
            self.answer.lower()
            == self.question_list[self.question_nr - 1].answer.lower()
        ):
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong")
        print(
            f"The correct answer was: {self.question_list[self.question_nr - 1].answer}"
        )
        print(f"Your current score is {self.score}/{self.question_nr}\n\n")
