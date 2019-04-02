__author__ = "Tit"
__credits__ = ["Tit", "Louise"]

import random
from agents.Agent import Agent


class AgentRandom(Agent):

    def __init__(self, params):
        """See documentation in the base class"""
        Agent.__init__(self, params)
        self.q=[[0]*self.num_actions]
        
        
    def start(self, initial_state):
        """See documentation in the base class"""

        action = self.policy(initial_state)
        return action

    def step(self, reward, state):
        """See documentation in the base class"""
        alpha=0.8
        gamma=0.5
        action = self.policy(state)
        next=EnvironmentGrid1D.step(action) #next=[next_state, reward, is_done]
        max_next=self.q[next[0]][0] #max_next designera le max(a) des q(s(t+1),a)
        j=1
        while j<self.num_actions:
            if self.q[next[0]][j]>max_next:
                max_next=self.q[next[0]][j]
            j=j+1
        self.q[state][action]=self.q[state][action]+alpha*(gamma*max_next-self.q[state][action])
        return action
        
    def policy(self, state):
        """See documentation in the base class"""

        return random.randint(0,self.num_actions-1) # Returns a random action
