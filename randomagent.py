import random

class RandomAgent:
    def __init__(self, name):
        self.name = name

    def chooseAction(self, positions, current_board, symbol):
        return positions[random.choice(list(range(0,len(positions))))]

    # append a hash state
    def addState(self, state):
        pass

    # at the end of game, backpropagate and update states value
    def feedReward(self, reward):
        pass

    def reset(self):
        pass