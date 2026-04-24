
class Question:
    def __init__(self, id, text, category, base_points):
        self.id = id
        self.text = text
        self.category = category
        self.base_points = base_points
        
    def check(self, answer):
        raise NotImplementedError("Subclasses must implement this method")
    
class ExactQuestion(Question):
    def __init__(self, id, text, answer, category, base_points):
        super().__init__(id, text, category, base_points)
        self.answer = answer
        
    def check(self, answer):
        return self.answer.lower() == answer.lower()
    
    class NumericalQuestion(Question):
        def __init__(self, id, text, answer, category, base_points):
            super().__init__(id, text, category, base_points)
            self.answer = float(answer)
        
        def check(self, answer):
            try:
                return abs(self.answer - float(answer)) <= 0.01
            except ValueError:
                return False

class QuestionBank:
    def __init__(self):
        self.questions = {}
        
    def add(self, question):
        self.questions[question.id] = question
        
    def get(self, id):
        return self.questions.get(id)
    
    def get_by_category(self, category):
        return [q for q in self.questions.values() if q.category == category]
    
    def random_quiz(self, n):
        import random
        return random.sample(list(self.questions.values()), n)
    
    def __str__(self):
        return '\n'.join(str(q) for q in self.questions.values())
    
    def __eq__(self, other):
        if isinstance(other, QuestionBank):
            return set(self.questions.keys()) == set(other.questions.keys())
        return False
