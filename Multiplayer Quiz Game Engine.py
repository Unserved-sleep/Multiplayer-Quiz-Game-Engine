"""
Quiz engine that has the following features:
- question banks
- live scoring
- leaderboard with streaks
- badges


@Authors:
    -Sidharth S K
    -Aditya Kumar
    -Ashutosh Sharma
    -Sanskar Dewangan
@Date: 24-042026

To-Do:
- Question banks & Catagory System
- Player & Scoring Engine
- Leaderboard, badges & stats
"""

from abc import ABC, abstractmethod
import random


class Question(ABC):
    """Abstract base class for quiz questions.
    Stores metadata like ID, text, answer, category, and base points.
    Supports both numeric and exact-match question types.
    """
    def __init__(self, qid: str, question: str, solution: str, category: str, base_point: int) -> None:        
        self.qid = qid
        self.question = question
        self.solution = solution
        self.category = category
        self.base_point = base_point


    @abstractmethod
    def check(self, answer: str) -> bool:
        pass
    

    def __str__(self) -> str:
        return f"{self.qid}: {self.question} [ Category:{self.category}, Points: {self.base_point}]"
    
    
    def __repr__(self) -> str:
        """For debugging purposes only. Shows constructor arguments."""
        return f"Question({self.qid!r}, {self.question!r}, {self.solution!r}, {self.category!r}, {self.base_point!r})"
    
    def __eq__(self, other) -> bool:
        return isinstance(other, Question) and self.qid == other.qid
    
    def __hash__(self):
        return hash(self.qid)
    

class ExactQuestion(Question):
    """Subclass that handles non-arithemetic questions. The check function checks if the answer is the same as the solution."""
    def check(self, answer: str) -> bool:
        return answer.strip().lower() == self.solution.strip().lower()
    

class NumericQuestion(Question):
    """Subclass that handles arithemetic questions. The check function checks if the answer is same as solution with a tolerance of (+,-)0.01 of the solution."""
    def check(self, answer: str) -> bool:
        try:
            given = float(answer.strip())
            correct = float(self.solution.strip())
            return abs(given - correct) <= 0.01
        except ValueError:
            return False


class QuestionBank:
    """A class that stores questions and can be used to generate random quizzes. The purpose of this class is to store unique questions and generate quiz with randomly selected questions."""
    def __init__(self) -> None:
        self.questions: dict[str, Question] = {}

    def add(self, question: Question) -> None:
        if question.qid not in self.questions:
            self.questions[question.qid] = question

    def get(self, qid: str) -> Question:
        return self.questions[qid]

    def get_by_category(self, category: str) -> list[Question]:
        return [q for q in self.questions.values() if q.category == category]

    def random_quiz(self, num_questions: int) -> list[Question]:
        if num_questions > len(self.questions):
            raise ValueError("Not enough questions in the bank")
        return random.sample(list(self.questions.values()), num_questions)

    def __len__(self) -> int:
        return len(self.questions)


def parse_question_raw(question_raw: list[tuple]) -> QuestionBank:
    """
    Parse a list of question tuples into a question bank. Checks the category of the question, if math then NumericQuestion, else ExactQuestion.
    """
    bank = QuestionBank()
    for qid, question, solution, category, base_point in question_raw:
        if category == "math":
            q = NumericQuestion(qid, question, solution, category, base_point)
        else:
            q = ExactQuestion(qid, question, solution, category, base_point)
        bank.add(q)
    return bank