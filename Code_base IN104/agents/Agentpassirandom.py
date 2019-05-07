__author__ = "Florence Carton"
__credits__ = ["Florence Carton", "Freek Stulp", "Antonin Raffin"]

import random
from scipy import *
from agents.Agent import Agent


class Agentpassirandom(Agent):

    def __init__(self, params):
        """See documentation in the base class"""
        Agent.__init__(self, params)
        self.q=zeros((self.num_states, self.num_actions))
        #self.q=[[]*self.num_actions]*self.num_states

        
        
    def start(self, initial_state):
        """See documentation in the base class"""

        action = self.policy(initial_state)
        return action

    def step(self, reward, state, prev_state,action,is_done,num_actions):
        """See documentation in the base class"""
        
        alpha=0.9
        gamma=0.9
        max_next=self.q[state][0] #max_next le max(a) des q(s,a)
        j=1
        while j<self.num_actions:
            if self.q[state][j]>max_next:
                max_next=self.q[state][j]
            
            j=j+1
        self.q[prev_state][action]=self.q[prev_state][action]+alpha*(reward+gamma*max_next-self.q[prev_state][action])
        action = self.policy(state)
        return action
        
    def policy(self, state):
        """See documentation in the base class"""
        maxi=[]
        R=0.05
        for i in range(self.num_actions):
            if self.q[state][i]==max(self.q[state]):
                maxi.append(i)
        r=random.random()
        if r>=R:
            a=random.randint(0,len(maxi))
            print(a)
            return(maxi[a])
        else:
            return(random.randint(0,self.num_actions-1))
        
        