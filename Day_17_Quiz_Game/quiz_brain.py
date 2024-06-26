class QuizBrain:
    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    def check_answer(self, real_answer, user_answer):
        if real_answer.lower()==user_answer.lower():
            print("You got it right!!")
            self.score+=1
        else:
            print("Oops!! Wrong answer")
        print("The correct answer is " + real_answer)
        print(f"Your current score is: {self.score}/{self.question_number}\n\n")
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(current_question.answer, user_answer)
