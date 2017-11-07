class Allergies(object):
    allergies_score = {
        'eggs': 1,
        'peanuts': 2,
        'shellfish': 4,
        'strawberries': 8,
        'tomatoes': 16,
        'chocolate': 32,
        'pollen': 64,
        'cats': 128
    }

    score = 0

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
        return self.allergies_score[item] <= self.score

    def rescore(self, mscore):
        if self.score >= mscore:
            self.score = self.score - mscore
            return True
        return False

    @property
    def lst(self):
        self.score = self.score % 256

        sortdesc = sorted(self.allergies_score.items(), key=lambda x: (x[1]), reverse=True)
        s = list(filter(lambda x: self.rescore(x[1]), sortdesc))
        s = list(map(lambda x: x[0], s))

        return s
