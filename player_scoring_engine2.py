questions_raw = [
("Q1","What is 8×7?", "56", "math", 10),
("Q2","Capital of France?", "Paris", "geo", 8),
("Q3","Python list to set syntax?","set(list)", "coding", 12),
("Q4","What is 144's square root?","12", "math", 10),
("Q5","Fastest animal?", "cheetah", "nature", 8),
("Q6","Output of 2**10?", "1024", "coding", 12),
]
rounds = [
("alice", [("Q1","56"),("Q2","London"),("Q3","set(list)"),("Q4","12")]),
("bob", [("Q1","56"),("Q2","Paris"), ("Q3","list(set)"),("Q5","cheetah")]),
("charlie", [("Q2","Paris"),("Q4","12"),("Q5","cheetah"), ("Q6","1024")]),
]

class Player:  #Player Class
    def __init__(self, name, score, correct_count, wrong_count, answer_history):  #Constructor
        self.name: str = name
        self.score: int = score
        self.correct_count: int = correct_count
        self.wrong_count: int = wrong_count
        self.answer_history: list = answer_history
        self.streak_earned: bool = False

    def track_streak(self):
        """Checking the streak and multiplying score"""
        streak: int = 0
        for ite_rater in self.answer_history:
            if ite_rater == 1:
                streak += 1
            if streak == 3:
                self.score *= 1.5
                self.streak_earned = True
            if ite_rater == 0:
                streak = 0

    def accuracy(self):
        """Calculating accuracy taking correct and incorrect answers"""
        return self.correct_count / (self.correct_count + self.wrong_count) *100
    def __str__(self):
        """Formatted output for each player"""
        return f"Player {self.name} has {int(self.score)} points with {self.accuracy()}% accuracy and has streak {self.streak_earned}"

    def __it__(self,other):
        """Iterator for comparing different players"""
        x: bool = (self.score, self.name) >= (other.score, other.name)
        return x


class ScoringEngine:
    """Scoring engine for player scoring"""
    def grade_round(self, player, answer_list):
        """Result for each of the questions given to the players"""
        i_iterator: int = 0
        report: list = []
        for ques in answer_list:
            if player[1][i_iterator][0] == ques[0]:
                if player[1][i_iterator][1] == ques[2]:
                    report.append(1)
                else:
                    report.append(0)
                i_iterator += 1
            else:
                report.append(-1)
            if i_iterator == 4:
                break
        while len(report) != 6:
            report.append(-1)
        return report

results: list = []
members: list = []

for rn in rounds:
    sc = ScoringEngine() #each player report
    results.append(sc.grade_round(rn, questions_raw))
iterator2 = 0

for r in results:
    correct: int = 0
    wrong: int = 0
    not_attempted: int = 0
    total_score: int = 0
    iterator: int = 0
    for q in r:
        if q == 1:
            correct += 1
            total_score += questions_raw[iterator][4]
        elif q == 0:
            wrong += 1
        else:
            not_attempted += 1
        iterator += 1
    members.append(Player(rounds[iterator2][0], total_score, correct, wrong, r))  #creating player objects
    members[-1].track_streak()
    members[-1].accuracy()
    iterator2 += 1

for m in members:
    print(m.__str__())  #formatted printing of result

for i in range(len(members)):
    for j in range(len(members)):
        if Player.__it__(members[i],members[j]):
            members[i], members[j] = members[j], members[i]  #arranging of the players

leaderboard: list = []
for m in members:
    leaderboard.append(m.name)
print(leaderboard) #leaderboard based on scores achieved