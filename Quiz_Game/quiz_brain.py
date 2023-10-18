class QuizBrain:

    def __init__ (self, question_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        curr_question = self.questions_list[self.question_number]
        user_guess = input(f"Q.{self.question_number + 1} {curr_question.text} (True or False)?: ")
        self.check_answer(user_guess, curr_question.answer)
        self.question_number += 1
        

    def check_answer(self, user_guess, answer):
        if user_guess.lower() == answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {answer}")
        print(f"Your current score is: {self.score}/{self.question_number + 1}")
        print()

    def complete_game(self):
        print("You've completed the quiz!")
        print(f"Your final score was: {self.score}/{self.question_number}")