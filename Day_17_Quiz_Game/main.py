from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions_list = []
for i in question_data:
    obj = Question(q_text=i["text"], q_ans=i["answer"])
    questions_list.append(obj)

quiz = QuizBrain(questions_list)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!!!")
print(f"Your sinal score is {quiz.score}/{len(quiz.question_list)}")

