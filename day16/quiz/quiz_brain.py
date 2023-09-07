class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        self.total_marks = len(question_list)

    def still_has_question(self):
        if self.question_number <= len(self.question_list):
            return True
        else:
            return False

    def current_question(self):
        current_question = self.question_list[self.question_number]
        print(f"Q # {self.question_number+1} :{current_question.text}")
        return current_question

    def next_question(self):
        self.question_number += 1

    def is_correct(self, current_question):
        answer = input("True or False : ")
        if current_question.answer.lower() == answer.lower():
            self.score += 1
            print("Right answer")
        else:
            print("Wrong aswer")
        print(f"Score is : {self.score}/{self.total_marks}\n")
