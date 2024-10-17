from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_Bank = []
for x in question_data:
    question_text = x["text"]
    answers = x["answer"]
    new_question = Question(question_text,answers)
    question_Bank.append(new_question)
quiz = QuizBrain(question_Bank)

while quiz.still_question():
    quiz.next_question()

print("you have completed the quiz")
print(f"your final score is {quiz.score}/{quiz.question_number}")
