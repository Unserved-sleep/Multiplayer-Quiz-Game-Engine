from abc import ABC, abstractmethod
import random

# Base abstract class for all questions
class Question(ABC):
    def __init__(self, id, text, category, base_points):
        self.id = id                  # unique question id
        self.text = text              # question text
        self.category = category      # category (math, geo, etc.)
        self.base_points = base_points  # marks for question

    @abstractmethod
    def check(self, answer):
        pass  # must be implemented in child classes

    def __str__(self):
        # string representation of question
        return f"{self.id}: {self.text} [{self.category}, {self.base_points} pts]"

    def __eq__(self, other):
        # compare questions by id
        return isinstance(other, Question) and self.id == other.id


# For exact match questions (text-based)
class ExactQuestion(Question):
    def __init__(self, id, text, answer, category, base_points):
        super().__init__(id, text, category, base_points)
        self.answer = answer  # correct answer

    def check(self, answer):
        # case-insensitive comparison
        return self.answer.lower() == answer.lower()


# For numerical questions with tolerance
class NumericalQuestion(Question):
    def __init__(self, id, text, answer, category, base_points):
        super().__init__(id, text, category, base_points)
        self.answer = float(answer)  # store as number

    def check(self, answer):
        try:
            # allow small error ±0.01
            return abs(self.answer - float(answer)) <= 0.01
        except ValueError:
            return False  # invalid input


# Stores all questions
class QuestionBank:
    def __init__(self):
        self.questions = {}  # dictionary {id: question}

    def add(self, question):
        self.questions[question.id] = question  # add question

    def get(self, id):
        return self.questions.get(id)  # get question by id

    def get_by_category(self, cat):
        # return all questions of a category
        return [q for q in self.questions.values() if q.category == cat]

    def random_quiz(self, n):
        # return n random questions
        return random.sample(list(self.questions.values()), n)


# Convert raw data into objects and store in bank
def parse_and_add(bank, questions_raw):
    for qid, text, ans, cat, pts in questions_raw:
        try:
            float(ans)  # check if numeric
            q = NumericalQuestion(qid, text, ans, cat, pts)
        except ValueError:
            q = ExactQuestion(qid, text, ans, cat, pts)
        bank.add(q)


# Main test block
if __name__ == "__main__":

    questions_raw = [
        ("Q1","What is 8×7?", "56", "math", 10),
        ("Q2","Capital of France?", "Paris", "geo", 8),
        ("Q3","Python list to set syntax?","set(list)", "coding", 12),
        ("Q4","What is 144's square root?","12", "math", 10),
        ("Q5","Fastest animal?", "cheetah", "nature", 8),
        ("Q6","Output of 2**10?", "1024", "coding", 12),
    ]

    bank = QuestionBank()
    parse_and_add(bank, questions_raw)

    # testing numerical question
    q1 = bank.get("Q1")
    print(q1.check("56"))       # True
    print(q1.check("55.99"))    # True

    # testing exact question
    q2 = bank.get("Q2")
    print(q2.check("paris"))    # True

    # testing category filter
    coding_qs = bank.get_by_category("coding")
    print([str(q) for q in coding_qs])

    # print one question
    print(str(q1))