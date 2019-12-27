import abc
import random


class Gamer(metaclass=abc.ABCMeta):
    def __init__(self, gamerName, totalTrial):
        self.TotalT = totalTrial
        self.name = gamerName
        self.mood = 'bad'

        self.index = 0
        self.answer_opponent = []
        self.answer_owner = []
        self.scores = []        

    def init_mood(self, mood):
        self.mood = mood
        pass

    def get_current_index(self):
        # return len(scores)
        return index

    def record_answer(self, owner_answer, opponent_answer):
        self.answer_owner.append(owner_answer)
        self.answer_opponent.append(opponent_answer)

    def record_score(self, score):
        self.scores.append(score)

    def get_score(self):
        summary = sum(self.scores)
        print('{}: sum: {} (len: {})'.format(self.name, summary, len(self.scores)))
        self.index += 1
        return summary

    @abc.abstractclassmethod
    def Answer(self):
        return NotImplemented


class PositiveGamer(Gamer):
    def Answer(self):
        self.mood = 'good'
        return self.mood


class NegativeGamer(Gamer):
    def Answer(self):
        self.mood = 'bad'
        return self.mood


class RandomGamer(Gamer):
    def __init__(self, gamerName, totalTrial, goodRatio):
      Gamer.__init__(self, gamerName, totalTrial)
      self.good_ratio = goodRatio      

    def Answer(self):
        # index = self.get_current_index()
        rand = random.randint(1, 100)
        if rand <= self.good_ratio:
            self.mood = 'good'
        else:
            self.mood = 'bad'
        return self.mood


def calculate(a1, a2):
    if a1 == 'bad':
        if a2 == 'bad':  # (bad, bad)
            return [0, 0]
        else:  # (bad, good)
            return [100, 0]
    else:
        if a2 == 'good':  # (good, good)
            return [50, 50]
        else:  # (bood, bad)
            return [0, 100]


T = 20

# gamer1 = PositiveGamer('PosGamer', T)
# gamer2 = NegativeGamer('NegGamer', T)
# gamer1 = NegativeGamer('NegGamer', T)
gamer1 = RandomGamer('RandomGamer Tom', T, 50)
gamer2 = RandomGamer('RandomGamer John', T, 20)

for index in range(0, T):
    a1 = gamer1.Answer()
    a2 = gamer2.Answer()
    scores = calculate(a1, a2)
    print('({}, {}): ({}, {}): ({}, {})'.format(gamer1.name, gamer2.name, a1, a2, scores[0], scores[1]))
    gamer1.record_answer(a1, a2)
    gamer1.record_score(scores[0])
    gamer2.record_answer(a2, a1)
    gamer2.record_score(scores[1])

total1 = gamer1.get_score()
total2 = gamer2.get_score()

print('total score: {} : {} --> {} : {}'.format(gamer1.name, gamer2.name, total1, total2))
