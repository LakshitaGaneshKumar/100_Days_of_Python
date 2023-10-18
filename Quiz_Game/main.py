from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create question bank of Question objects
question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz = QuizBrain(question_bank)

while (quiz.still_has_questions()):
    quiz.next_question()

quiz.complete_game()
