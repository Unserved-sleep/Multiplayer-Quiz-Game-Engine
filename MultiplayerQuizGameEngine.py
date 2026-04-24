
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
