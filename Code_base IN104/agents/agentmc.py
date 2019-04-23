# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:02:32 2019

@author: Louise
"""

import random
from scipy import *
import numpy as np
from agents.Agent import Agent


class agentmc(Agent):
    
    def __init__(self, params):
        """See documentation in the base class"""
        
        Agent.__init__(self, params)
        self.q=zeros((self.num_states, self.num_actions))
        self.rewards=[[[]]*self.num_states]*self.num_actions #matrice des R, va grandir à chaque fin de chemin
        

    def start(self, initial_state):
        """See documentation in the base class"""
        
        action = self.policy(initial_state)
        self.chemin=[[initial_state, action,0]]  #matrice pour stocker le chemin, réinitialisée à chaque début de chemin
        return action

        
    def step(self, reward, state, prev_state,action,is_done):
        """See documentation in the base class"""
        
        action = self.policy(state)
        self.chemin.append([state,action,reward])

        
        if is_done==True :
            for i in range (len(self.chemin)):
                etat,action=self.chemin[len(self.chemin)-i-1]
                c=self.rewards[action][etat]
                c.append(self.num_states-len(self.chemin)+i)
                self.rewards[action][etat]=c
            
            for d in self.chemin:
                self.q[d]=np.mean(self.rewards[d[1]][d[0]])
                                           
        return action
        
    def policy(self, state):
        """See documentation in the base class"""
        maxi=[]
        R=0.01
        for i in range(self.num_actions):
            if self.q[state][i]==max(self.q[state]):
                maxi.append(i)
        r=random.random()
        if r>=R:
            a=random.randint(0,len(maxi))
            return(maxi[a])
        else:
            return(random.randint(0,self.num_actions))
        