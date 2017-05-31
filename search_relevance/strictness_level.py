class StrictnessLevel:

    minimum_score = None

    def passes(self,score):
        if score >= self.minimum_score:
            return True
        return False


class MostStrict(StrictnessLevel):

    def __init__(self):
        self.minimum_score = 0.95

class VeryStrict(StrictnessLevel):

    def __init__(self):
        self.minimum_score = 0.8

class Strict(StrictnessLevel):

    def __init__(self):
        self.minimum_score = 0.5

class VeryLoose(StrictnessLevel):

    def __init__(self):
        self.minimum_score = 0.0