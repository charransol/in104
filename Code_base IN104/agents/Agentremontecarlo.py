__author__ = "Florence Carton"
__credits__ = ["Florence Carton", "Freek Stulp", "Antonin Raffin"]

import random
from scipy import *
from agents.Agent import Agent
from params import default_params


class Agentremontecarlo(Agent):

    def __init__(self, params):
        """See documentation in the base class"""
        Agent.__init__(self, params)
        self.q=zeros((self.num_states, self.num_actions))
        #self.q=[[]*self.num_actions]*self.num_states
        self.passage=zeros((self.num_states, self.num_actions))
        self.chemin=[]
        self.curr_ep=0
        

        
        
    def start(self, initial_state):
        """See documentation in the base class"""

        action = self.policy(initial_state)
        self.chemin.append([initial_state,action,0])
        return action
        self.curr_ep=self.curr_ep+1
        

    def step(self, reward, state, prev_state,action,is_done,num_actions):
        """See documentation in the base class"""
        alpha=10
        self.chemin.append([state,action,0])
        if is_done:
            for i in range(len(self.chemin)):
                self.chemin[i][2]=self.num_states*(1+alpha*i/len(self.chemin))   #calcul de reward pour chaque case+action 
                n=self.passage[self.chemin[i][0]][self.chemin[i][1]]
                self.passage[self.chemin[i][0]][self.chemin[i][1]]+=1
                self.q[self.chemin[i][0]][self.chemin[i][1]]=(self.q[self.chemin[i][0]][self.chemin[i][1]]*n+self.chemin[i][2])/(n+1)

            self.chemin=[]
            self.passage=zeros((self.num_states, self.num_actions))
        if num_actions==default_params()['max_action_per_episode']-1:
            self.chemin=[]
            self.passage=zeros((self.num_states, self.num_actions))
            for i in range(len(self.chemin)):
                self.q[self.chemin[i][0]][self.chemin[i][1]]-=15
        
        action = self.policy(state)
        return action
        
    def policy(self, state):
        """See documentation in the base class"""
        maxi=[]
        R=0.05
        for i in range(self.num_actions):
            if self.q[state][i]>=max(self.q[state])-0.1:
                maxi.append(i)
        r=random.random()
        if r>=R:
            a=random.randint(0,len(maxi))
            return(maxi[a])
        else:
            return(random.randint(0,self.num_actions))
        