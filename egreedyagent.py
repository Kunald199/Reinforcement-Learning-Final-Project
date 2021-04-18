import numpy as np
import random


class EpsilonGreedyAgent:
    def __init__(self, name, exp_rate):
        self.name = name
        self.name=name
        self.eps = 0.4 # probability of choosing random action instead of greedy
        self.states_value = {}
        self.exp_rate=exp_rate

    def chooseAction(self, positions, current_board, symbol):
        r = np.random.rand()
        best_state = None
        if r < self.eps:
            return positions[random.choice(list(range(0, len(positions))))]
        else:
            value_max = -999
            for p in positions:
                next_board = current_board.copy()
                next_board[p] = symbol
                next_boardHash = str(next_board.reshape(3 * 3))
                value = 0 if self.states_value.get(next_boardHash) is None else self.states_value.get(next_boardHash)
                if value >= value_max:
                    value_max = value
                    action = p
        return action

        def addState(self, state):
            pass

        # at the end of game, backpropagate and update states value
        def feedReward(self, reward):
            pass

        def reset(self):
            self.state_history = []
