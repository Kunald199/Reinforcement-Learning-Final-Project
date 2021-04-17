class epsilonAgent:
  def __init__(self,name):
    self.name=name
    self.eps = 0.5 # probability of choosing random action instead of greedy
    self.alpha = 0.5 # learning rate
    self.verbose = False
    self.state_history = []

  def take_action(self,positions, current_board, symbol):

    r = np.random.rand()
    best_state = None
    if r < self.eps:
        return positions[random.choice(list(range(0,len(positions))))]

    else:
        if np.random.uniform(0, 1) <= self.exp_rate:
            # take random action
            idx = np.random.choice(len(positions))
            action = positions[idx]
        else:
            value_max = -999
            for p in positions:
                next_board = current_board.copy()
                next_board[p] = symbol
                next_boardHash = self.getHash(next_board)
                value = 0 if self.states_value.get(next_boardHash) is None else self.states_value.get(next_boardHash)
                # print("value", value)
                if value >= value_max:
                    value_max = value
                    action = p
        positions=action
        # print("{} takes action {}".format(self.name, action))
        return positions
    # append a hash state
    def addState(self, state):
        pass

    # at the end of game, backpropagate and update states value
    def feedReward(self, reward):
        pass

    def reset(self):
        pass
