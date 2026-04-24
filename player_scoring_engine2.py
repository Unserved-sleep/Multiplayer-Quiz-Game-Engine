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

class Player:
    def __init__(self, name, score, correct_count, wrong_count, answer_history):
        self.name = name
        self.score = score
        self.correct_count = correct_count
        self.wrong_count = wrong_count
        self.answer_history = answer_history
        self.streak_earned = False

    def track_streak(self):
        streak = 0
        for i in self.answer_history:
            if i == 1:
                streak += 1
            if streak == 3:
                self.score *= 1.5
                self.streak_earned = True
            if i == 0:
                streak = 0

    def accuracy(self):
        return self.correct_count / (self.correct_count + self.wrong_count) *100
    def __str__(self):
        return f"Player {self.name} has {int(self.score)} points with {self.accuracy()}% accuracy and has streak {self.streak_earned}"

    def __it__(self,other):
        x = (self.score, self.name) >= (other.score, other.name)
        return x


class ScoringEngine:
    def grade_round(self, player, answer_list):
        i = 0
        report = []
        for ques in answer_list:
            if player[1][i][0] == ques[0]:
                if player[1][i][1] == ques[2]:
                    report.append(1)
                else:
                    report.append(0)
                i += 1
            else:
                report.append(-1)
            if i == 4:
                break
        while len(report) != 6:
            report.append(-1)
        return report

results = []
members = []

for rn in rounds:
    sc = ScoringEngine()
    results.append(sc.grade_round(rn, questions_raw))
iterator2 = 0

for r in results:
    correct = 0
    wrong = 0
    not_attempted = 0
    total_score = 0
    iterator = 0
    for q in r:
        if q == 1:
            correct += 1
            total_score += questions_raw[iterator][4]
        elif q == 0:
            wrong += 1
        else:
            not_attempted += 1
        iterator += 1
    members.append(Player(rounds[iterator2][0], total_score, correct, wrong, r))
    members[-1].track_streak()
    members[-1].accuracy()
    iterator2 += 1

for m in members:
    print(m.__str__())

for i in range(len(members)):
    for j in range(len(members)):
        if Player.__it__(members[i],members[j]):
            members[i], members[j] = members[j], members[i]

leaderboard = []
for m in members:
    leaderboard.append(m.name)
print(leaderboard)