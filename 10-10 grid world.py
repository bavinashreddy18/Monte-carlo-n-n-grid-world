import numpy as np
import copy
class GridWorld:
    def __init__(self):
        # S O O O
        # O O O *
        # O * O O
        # O * 0 T
        self.qTable = None
        self.actionSpace = ('U', 'D', 'L', 'R')
        self.actions = {
            (0, 0): ('D', 'R'),
            (0, 1): ('L', 'D', 'R'),
            (0, 2): ('L', 'D', 'R'),
            (0, 3): ('L', 'D', 'R'),
            (0, 4): ('L', 'D', 'R'),
            (0, 5): ('L', 'D', 'R'),
            (0, 6): ('L', 'D', 'R'),
            (0, 7): ('L', 'D', 'R'),
            (0, 8): ('L', 'D', 'R'),
            (0, 9): ('L', 'D'),
            (1, 0): ('U', 'D', 'R'),
            (1, 1): ('U', 'L', 'D', 'R'),
            (1, 2): ('U', 'L', 'D', 'R'),
            (1, 3): ('U', 'L', 'D', 'R'),
            (1, 4): ('U', 'L', 'D', 'R'),
            (1, 5): ('U', 'L', 'D', 'R'),
            (1, 6): ('U', 'L', 'D', 'R'),
            (1, 7): ('U', 'L', 'D', 'R'),
            (1, 8): ('U', 'L', 'D', 'R'),
            (1, 9): ('U', 'L', 'D'),
            (2, 0): ('U', 'D', 'R'),
            (2, 1): ('U', 'L', 'D', 'R'),
            (2, 2): ('U', 'L', 'D', 'R'),
            (2, 3): ('U', 'L', 'D', 'R'),
            (2, 4): ('U', 'L', 'D', 'R'),
            (2, 5): ('U', 'L', 'D', 'R'),
            (2, 6): ('U', 'L', 'D', 'R'),
            (2, 7): ('U', 'L', 'D', 'R'),
            (2, 8): ('U', 'L', 'D', 'R'),
            (2, 9): ('U', 'L', 'D'),
            (3, 0): ('U', 'D', 'R'),
            (3, 1): ('U', 'L', 'D', 'R'),
            (3, 2): ('U', 'L', 'D', 'R'),
            (3, 3): ('U', 'L', 'D', 'R'),
            (3, 4): ('U', 'L', 'D', 'R'),
            (3, 5): ('U', 'L', 'D', 'R'),
            (3, 6): ('U', 'L', 'D', 'R'),
            (3, 7): ('U', 'L', 'D', 'R'),
            (3, 8): ('U', 'L', 'D', 'R'),
            (3, 9): ('U', 'L', 'D'),
            (4, 0): ('U', 'D', 'R'),
            (4, 1): ('U', 'L', 'D', 'R'),
            (4, 2): ('U', 'L', 'D', 'R'),
            (4, 3): ('U', 'L', 'D', 'R'),
            (4, 4): ('U', 'L', 'D', 'R'),
            (4, 5): ('U', 'L', 'D', 'R'),
            (4, 6): ('U', 'L', 'D', 'R'),
            (4, 7): ('U', 'L', 'D', 'R'),
            (4, 8): ('U', 'L', 'D', 'R'),
            (4, 9): ('U', 'L', 'D'),
            (5, 0): ('U', 'D', 'R'),
            (5, 1): ('U', 'L', 'D', 'R'),
            (5, 2): ('U', 'L', 'D', 'R'),
            (5, 3): ('U', 'L', 'D', 'R'),
            (5, 4): ('U', 'L', 'D', 'R'),
            (5, 5): ('U', 'L', 'D', 'R'),
            (5, 6): ('U', 'L', 'D', 'R'),
            (5, 7): ('U', 'L', 'D', 'R'),
            (5, 8): ('U', 'L', 'D', 'R'),
            (5, 9): ('U', 'L', 'D'),            
            (6, 0): ('U', 'D', 'R'),
            (6, 1): ('U', 'L', 'D', 'R'),
            (6, 2): ('U', 'L', 'D', 'R'),
            (6, 3): ('U', 'L', 'D', 'R'),
            (6, 4): ('U', 'L', 'D', 'R'),
            (6, 5): ('U', 'L', 'D', 'R'),
            (6, 6): ('U', 'L', 'D', 'R'),
            (6, 7): ('U', 'L', 'D', 'R'),
            (6, 8): ('U', 'L', 'D', 'R'),
            (6, 9): ('U', 'L', 'D'),
            (7, 0): ('U', 'D', 'R'),
            (7, 1): ('U', 'L', 'D', 'R'),
            (7, 2): ('U', 'L', 'D', 'R'),
            (7, 3): ('U', 'L', 'D', 'R'),
            (7, 4): ('U', 'L', 'D', 'R'),
            (7, 5): ('U', 'L', 'D', 'R'),
            (7, 6): ('U', 'L', 'D', 'R'),
            (7, 7): ('U', 'L', 'D', 'R'),
            (7, 8): ('U', 'L', 'D', 'R'),
            (7, 9): ('U', 'L', 'D'),
            (8, 0): ('U', 'D', 'R'),
            (8, 1): ('U', 'L', 'D', 'R'),
            (8, 2): ('U', 'L', 'D', 'R'),
            (8, 3): ('U', 'L', 'D', 'R'),
            (8, 4): ('U', 'L', 'D', 'R'),
            (8, 5): ('U', 'L', 'D', 'R'),
            (8, 6): ('U', 'L', 'D', 'R'),
            (8, 7): ('U', 'L', 'D', 'R'),
            (8, 8): ('U', 'L', 'D', 'R'),
            (8, 9): ('U', 'L', 'D'),
            (9, 0): ('U', 'R'),
            (9, 1): ('U', 'L', 'R'),
            (9, 2): ('U', 'L', 'R'),
            (9, 3): ('U', 'L', 'R'),
            (9, 4): ('U', 'L', 'R'),
            (9, 5): ('U', 'L', 'R'),
            (9, 6): ('U', 'L', 'R'),
            (9, 7): ('U', 'L', 'R'),
            (9, 8): ('U', 'L', 'R'),
        }
        self.rewards = {(9, 9): 10.5, (0, 9): -1, (1, 1): -1, (2, 2): -1, (3, 3): -1, (4, 4): -1, (5, 5): -1, (6, 6): -1, (7, 7): -1, (8, 8): -1, (9, 0): -1, (9, 9): -1}
        self.explored = 0
        self.exploited = 0
        self.initialQtable()

    def initialQtable(self):
      self.qTable = {}
      for state in self.actions:
          self.qTable[state]={}
          for move in self.actions[state]:
              self.qTable[state][move]=0
      print(self.qTable)

    def updateQtable(self, newQ,updateRate=0.05):
        for state in self.qTable:
            for action in self.qTable[state]:
                self.qTable[state][action] = self.qTable[state][action]+(updateRate*(newQ[state][action]-self.qTable[state][action]))
   
    def getRandomPolicy(self):
        policy = {}
        for state in self.actions:
            policy[state] = np.random.choice(self.actions[state])
        return policy

    def reset(self):
        return (0, 0)
        
    def is_terminal(self, s):
        return s not in self.actions

    def getNewState(self,state,action):
      i, j = zip(state)
      row = int(i[0])
      column = int(j[0])
      if action == 'U':
          row -= 1
      elif action == 'D':
          row += 1
      elif action == 'L':
          column -= 1
      elif action == 'R':
          column += 1
      return row,column

    def chooseAction(self, state, policy, exploreRate):
        if exploreRate > np.random.rand():
            self.explored += 1
            return np.random.choice(self.actions[state])
        self.exploited += 1
        return policy[state]

    def move(self, state, policy, exploreRate):
        action = self.chooseAction(state, policy, exploreRate)
        row,column=self.getNewState(state,action)
        if (row, column) in self.rewards:
            return action,(row, column),self.rewards[(row, column)]
        return action,(row, column), 0
        
    def printPolicy(self, policy):
        line = ""
        counter = 0
        for item in policy:
            line += f" | {policy[item]} | "
            counter += 1
            if counter > 9:
                print(line)
                print("----------------------------")
                counter = 0
                line = ""
        print(line)
        print("----------------------------")
        
enviroment = GridWorld()
policy = enviroment.getRandomPolicy()
enviroment.printPolicy(policy)

# example optimal policy = {(0, 0): 'R', (0, 1): 'R', (0, 2): 'D', (0, 3): 'D', (1, 0): 'R', (1, 1): 'D', (1, 2): 'D', (1, 3): 'D',
#           (2, 0): 'R', (2, 1): 'D', (2, 2): 'R', (2, 3): 'D', (3, 0): 'R', (3, 1): 'R', (3, 2): 'R'}

for i in range(1001):
  estimatedQ = copy.deepcopy(enviroment.qTable)
  collectedSampls = 0
  for j in range(1000):
    trajectory = []
    state = enviroment.reset()
    stepCounts=0

    while (not enviroment.is_terminal(state)) and (stepCounts<30):
      action,nextState, reward = enviroment.move(state, policy, exploreRate=0.05)
      trajectory.append(((state, action), reward))
      state=nextState
      stepCounts+=1
    collectedSampls += 1
    rewards=0
    for item in reversed(trajectory):
            q,reward=zip(item)
            rewards +=0.9*(reward[0])
            estimatedQ[q[0][0]][q[0][1]] = estimatedQ[q[0][0]][q[0][1]] + ((1 / collectedSampls) * (rewards - estimatedQ[q[0][0]][q[0][1]]))
    enviroment.updateQtable(estimatedQ)
    for state in policy:
        policy[state] = max(enviroment.qTable[state], key=enviroment.qTable[state].get)
  if (i%100)==0:
    print(f"\n\n\n step:{i}")
    enviroment.printPolicy(policy)

print(f"exploited:{enviroment.exploited}  explored:{enviroment.explored}")