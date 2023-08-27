class Die:
    def __init__(self):
        self.chances = {}

class FairDie(Die):
    def __init__(self, sides):
        self.sides = sides
        self.chances = {}
        _chance = 1 / sides
        for i in range(1, sides+1):
            self.chances[i] = _chance

class UnfairDie(Die):
    def __init__(self, chances:{}):
        '''
        chances structured like {1: 0.333, 2: 0.333, 3: 0.3333}, where the key if the sidevalue and the value is its chance. It won't get checked if it sums up to 1
        '''        
        self.chances = chances
        self.sides = len(self.chances)