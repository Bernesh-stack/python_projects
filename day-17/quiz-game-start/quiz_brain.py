class QuizBrain:
    def __init__(self ,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_question(self):
        if (self.question_number == len(self.question_list)):
            return False
        else:
            return True

    def next_question(self):
        r = self.question_list[self.question_number]
        self.question_number +=1
        user_ans = input(f"Q.{self.question_number}:{r.text}: true or false")
        self.check_anwer(user_ans,r.answer)

    def check_anwer(self,user_ans,correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("you got it ")
            self.score +=1
            print(f"your current score is {self.score}/{self.question_number}")
        else:
            print("sorry wrong")
            print(f"the correct ans is {correct_ans}")
