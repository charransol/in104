import random
from agents.Agent import Agent


class Agent_Qlearning(Agent):

    def __init__(self, params):
        """See documentation in the base class"""
        Agent.__init__(self, params)
        self.q=[[0]*self.num_actions]*self.num_states
        self.hasard=0.2
    
    def start(self, initial_state):
        """See documentation in the base class"""

        action = self.policy(initial_state)
        return action

    def step(self, reward, state):
        """See documentation in the base class"""

        action = self.policy(state)
        return action
        
    def policy(self, state):
        """See documentation in the base class"""
        maxi=[]
        equal=-1
        for i in range(num_actions):
            if q[state][i]>max(q[state]):
                maxi=[i]
                equal=0
            if q[state][i]==max(q[state]):
                equal=1
                maxi.append(i)
        if equal !=0 :
            return(maxi[random.randint(0,len(maxi)-1)])
        else:
            r=random.random()
            if r<=self.hasard:
                return(maxi[random.randint(0,len(maxi)-1)])
                
            else:
                return(maxi[0])