# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 14:14:08 2019

@author: Louise
"""

import random
import matplotlib.pyplot as plt
from scipy import *
from agents.Agent import Agent


class agentsarsa(Agent):

    def __init__(self, params):
        """See documentation in the base class"""
        Agent.__init__(self, params)
        self.q=zeros((self.num_states, self.num_actions))
        self.hasard=0.1
    
    def start(self, initial_state):
        """See documentation in the base class"""

        action = self.policy(initial_state)
        return action

    def step(self, reward, state, prev_state, action,is_done):
        """See documentation in the base class"""
        #trouver ce qu'on va faire après
        new_action = self.policy(state)
        #mise à jour
        alpha=0.9
        gamma=0.9
#            print('q', self.q)
#            print('ps', prev_state)
#            print('s', state)
#            print('a', action)
#            print('na', new_action)
        self.q[prev_state][action]=self.q[prev_state][action]+alpha*(reward+gamma*self.q[state][new_action]-self.q[prev_state][action])
#            print('new q', self.q)
        
#        print('ok')
        return new_action
        
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
            return(maxi[a])
        else:
            return(random.randint(0,self.num_actions-1))
