# Monte carlo:- n*n grid world
<p align="center">
  <img width="400" height="270" src="https://github.com/bavinashreddy18/Monte-carlo-n-n-grid-world/blob/main/gridworld.png">
  </p>

## ***Developers*** 👦👦
                1. Murukuri S V S V Vasanth (College🏛️: IIIT NAYA RAIPUR,✉️- murukuri20102@iiitnr.edu.in)
                2. B.Avinash Reddy (College🏛️: IIIT NAYA RAIPUR,✉️- bavinashreddy18@gmail.com)
                
## ***Description*** 📝
                 Considered a grid world of size 10*10. Where 10 of the states are blocked and one state is set as a
                 goal state. By using reinforcement learning monte carlo algorithm, we computed the optimum policy
                 for agent to reach goal state from a starting point. Here policy is stochastic nature and implemented 
                 in python.
# Reinforcement-Learning-technique:- 10*10 Gridworld using Monte carlo in python
  Solving a simple 10*10 Gridworld almost similar to openAI gym frozenlake using Monte-Carlo method Reinforcement Learning
  the method used is policy iteration whitch is one of fundamental manners of Dynamic Programing.  

     | S | O | O | O | O | O | O | O | O | * |  
     | O | * | O | O | O | O | O | O | O | O |  
     | O | O | * | O | O | O | O | O | O | O |  
     | O | O | O | * | O | O | O | O | O | O |
     | O | O | O | O | * | O | O | O | O | O |  
     | O | O | O | O | O | * | O | O | O | O |  
     | O | O | O | O | O | O | * | O | O | O |  
     | O | O | O | O | O | O | O | * | O | O |
     | O | O | O | O | O | O | O | O | * | O |  
     | * | O | O | O | O | O | O | O | O | G |  
 
     S = Start state    O = Normal State
     * = Blocked State  G = Goal State  
  
Our agent goal is to find policy to go from S(start) state to T(goal) state with maximum reward(or minimum negative reward)  
valid actions are storend in GridWorld actions array. Positive and negative rewards in each state is stored in Gridworld  "Rewards" dictionary and can be modified by user. The current rewards for *(blocked) state and T(goal) state has been set to:  

              self.rewards = {(9, 9): 10.5, (0, 9): -1, (1, 1): -1, (2, 2): -1, (3, 3): -1, (4, 4): -1, (5, 5): -1, (6, 6): -1, 
              (7, 7): -1, (8, 8): -1, (9, 0): -1, (9, 9): -1}  
              
## ***Algorithm Flow*** 📃

  First we initialize a random policy that indicate prefered moves in every state: 
  
    U = going up  
    D = going down  
    L = going left  
    R = going right  
  
  We initialize Q table like below: 
 
    (0, 0): {'D': 0, 'R': 0},
    (0, 1): {'L': 0, 'D': 0, 'R': 0},
    (0, 2): {'L': 0, 'D': 0, 'R': 0},
    (0, 3): {'L': 0, 'D': 0, 'R': 0},
    (0, 4): {'L': 0, 'D': 0, 'R': 0},
    (0, 5): {'L': 0, 'D': 0, 'R': 0},
    (0, 6): {'L': 0, 'D': 0, 'R': 0},
    (0, 7): {'L': 0, 'D': 0, 'R': 0},
    (0, 8): {'U': 0, 'D': 0, 'R': 0},
    (0, 9): {'L': 0, 'D': 0},
    (1, 0): {'U': 0, 'D': 0, 'R': 0},
    (1, 1): {'U': 0, 'L': 0, 'D': 0, 'R': 0},
    (1, 2): {'U': 0, 'L': 0, 'D': 0, 'R': 0},
    (1, 3): {'U': 0, 'L': 0, 'D': 0, 'R': 0},
    (1, 4): {'U': 0, 'L': 0, 'D': 0, 'R': 0},
    (1, 5): {'U': 0, 'L': 0, 'D': 0, 'R': 0},
    (1, 6): {'U': 0, 'L': 0, 'D': 0, 'R': 0},
    (1, 7): {'U': 0, 'L': 0, 'D': 0, 'R': 0},
    (1, 8): {'U': 0, 'L': 0, 'D': 0, 'R': 0},
    (1, 9): {'U': 0, 'L': 0, 'D': 0},
    ................................
    ................................
    (9, 0): {'U': 0, 'R': 0},
    (9, 1): {'U': 0, 'L': 0, 'R': 0},
    (9, 2): {'U': 0, 'L': 0, 'R': 0},
    (9, 3): {'U': 0, 'L': 0, 'R': 0},
    (9, 4): {'U': 0, 'L': 0, 'R': 0}}
    (9, 5): {'U': 0, 'L': 0, 'R': 0},
    (9, 6): {'U': 0, 'L': 0, 'R': 0},
    (9, 7): {'U': 0, 'L': 0, 'R': 0},
    (9, 8): {'U': 0, 'L': 0, 'R': 0}
 
We start using monte carlo sampling to our generated policy. we play untill end of the episode and after episode termination we count over every transiton in reverse and use the transiton reward to update Q-table and as well as policy till convergence of policy which will be optimal policy. For choosing next action at each state of game we use epsilon greedy method. 


## ***Random policy*** 🗨️
        | D |  | L |  | R |  | R |  | R |  | R |  | R |  | D |  | D |  | L |
        ----------------------------
        | U |  | L |  | L |  | R |  | D |  | R |  | D |  | D |  | L |  | U |
        ----------------------------
        | D |  | L |  | L |  | L |  | U |  | D |  | U |  | L |  | D |  | L |
        ----------------------------
        | U |  | R |  | R |  | D |  | U |  | D |  | D |  | U |  | L |  | U |
        ----------------------------
        | R |  | L |  | D |  | R |  | U |  | R |  | D |  | D |  | U |  | U |
        ----------------------------
        | R |  | R |  | U |  | D |  | R |  | U |  | L |  | D |  | U |  | L |
        ----------------------------
        | U |  | R |  | D |  | R |  | L |  | L |  | U |  | R |  | U |  | L |
        ----------------------------
        | D |  | L |  | U |  | U |  | D |  | D |  | R |  | L |  | D |  | D |
        ----------------------------
        | D |  | U |  | R |  | L |  | D |  | R |  | D |  | D |  | R |  | U |
        ----------------------------
        | R |  | L |  | U |  | L |  | R |  | R |  | U |  | U |  | L |

## ***Step: 0*** ▶️

        | D |  | R |  | R |  | L |  | L |  | L |  | L |  | L |  | L |  | L |
        ----------------------------
        | D |  | L |  | R |  | U |  | U |  | U |  | U |  | U |  | U |  | U |
        ----------------------------
        | D |  | L |  | D |  | U |  | U |  | U |  | U |  | U |  | U |  | U |
        ----------------------------
        | D |  | L |  | L |  | U |  | U |  | U |  | U |  | U |  | U |  | U |
        ----------------------------
        | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |
        ----------------------------
        | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |
        ----------------------------
        | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |
        ----------------------------
        | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |
        ----------------------------
        | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |
        ----------------------------
        | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |

  ## ***Step: 100*** ⏭️
  
        | D |  | R |  | D |  | R |  | L |  | R |  | L |  | L |  | L |  | L |
        ----------------------------
        | D |  | R |  | R |  | R |  | D |  | R |  | L |  | U |  | U |  | U |
        ----------------------------
        | R |  | D |  | U |  | U |  | R |  | D |  | U |  | U |  | U |  | U |
        ----------------------------
        | D |  | D |  | L |  | D |  | R |  | U |  | U |  | U |  | U |  | U |
        ----------------------------
        | D |  | L |  | L |  | L |  | L |  | U |  | U |  | U |  | U |  | U |
        ----------------------------
        | R |  | L |  | L |  | U |  | U |  | U |  | U |  | U |  | U |  | U |
        ----------------------------
        | R |  | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |
        ----------------------------
        | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |
        ----------------------------
        | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |
        ----------------------------
        | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |
 
## ***Step: 500*** ⏲️

        | D |  | R |  | R |  | R |  | R |  | L |  | R |  | L |  | L |  | L |
        ----------------------------
        | D |  | R |  | R |  | U |  | L |  | D |  | L |  | D |  | D |  | L |
        ----------------------------
        | D |  | D |  | D |  | R |  | U |  | U |  | D |  | R |  | L |  | U |
        ----------------------------
        | D |  | D |  | D |  | R |  | R |  | U |  | R |  | R |  | U |  | U |
        ----------------------------
        | D |  | D |  | L |  | D |  | L |  | R |  | R |  | L |  | U |  | U |
        ----------------------------
        | R |  | L |  | L |  | D |  | L |  | L |  | R |  | D |  | U |  | U |
        ----------------------------
        | R |  | L |  | L |  | D |  | L |  | L |  | L |  | U |  | U |  | U |
        ----------------------------
        | U |  | R |  | L |  | U |  | U |  | L |  | U |  | U |  | U |  | U |
        ----------------------------
        | R |  | R |  | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |
        ----------------------------
        | U |  | R |  | U |  | U |  | U |  | U |  | U |  | U |  | U |
        
## ***Step: 1000*** 🥇

        | D |  | R |  | R |  | D |  | R |  | D |  | D |  | L |  | L |  | L |
        ----------------------------
        | D |  | R |  | R |  | R |  | R |  | U |  | D |  | L |  | L |  | D |
        ----------------------------
        | D |  | D |  | U |  | R |  | D |  | U |  | U |  | D |  | D |  | L |
        ----------------------------
        | D |  | D |  | L |  | D |  | R |  | R |  | U |  | L |  | L |  | U |
        ----------------------------
        | D |  | D |  | R |  | D |  | L |  | R |  | R |  | R |  | U |  | U |
        ----------------------------
        | D |  | L |  | D |  | D |  | L |  | D |  | R |  | R |  | U |  | U |
        ----------------------------
        | R |  | D |  | R |  | D |  | L |  | L |  | L |  | L |  | U |  | U |
        ----------------------------
        | R |  | U |  | D |  | U |  | U |  | L |  | U |  | U |  | U |  | U |
        ----------------------------
        | R |  | R |  | U |  | U |  | U |  | U |  | U |  | U |  | U |  | U |
        ----------------------------
        | U |  | R |  | U |  | U |  | U |  | U |  | U |  | U |  | U |
        ----------------------------



 
