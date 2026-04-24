class Player:
    def __init__(self, name, score, accuracy=0, streak=0, coding=False, math=False):
        self.name = name
        self.score = score
        self.accuracy = accuracy
        self.streak = streak
        self.coding = coding == "True"
        self.math = math == "True"

    def __str__(self):
        return f"{self.name}({int(self.score)})"


class Leaderboard:
    def __init__(self, players):
        self.players = players

    def rank(self):
        return sorted(self.players, key=lambda x: (-x.score, x.name))

    def __len__(self):
        return len(self.players)

    def __str__(self):
        medals = ["1", "2", "3"]
        sorted_players = self.rank()
        result = []

        for i in range(min(3, len(sorted_players))):
            s = sorted_players[i]
            result.append(f"{medals[i]} {s.name} {int(s.score)} pts")

        return "\n".join(result)


n = int(input())
players = []

for i in range(n):
    name = input()
    score = float(input())
    accuracy = float(input())
    streak = int(input())
    coding = input()
    math = input()

    players.append(Player(name, score, accuracy, streak, coding, math))


lb = Leaderboard(players)


badges = {}

for student in players:
    badges[student.name] = set()

    if student.accuracy == 100:
        badges[student.name].add("Perfect Round")

    if student.streak > 3:
        badges[student.name].add("Streak Master")

    if student.coding:
        badges[student.name].add("Coder")

    if student.math:
        badges[student.name].add("Mathlete")


scores = [p.score for p in players]

highest = max(scores)
lowest = min(scores)
average = sum(scores) / len(scores)

best_student = max(players, key=lambda x: x.score).name


print(lb)
print(len(lb))

for name in badges:
    print(name, ":", badges[name])

print("Highest Score:", int(highest))
print("Lowest Score:", int(lowest))
print("Average Score:", round(average, 2))
print("Best Student:", best_student)