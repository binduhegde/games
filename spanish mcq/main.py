from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

NO_OF_QUESTIONS = 20

question_bank = []
for question in range(NO_OF_QUESTIONS):
    new_question = Question()
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
