import random
from agents.Agent import Agent


class agentsarsa(Agent):

    def __init__(self, params):
        """See documentation in the base class"""
        Agent.__init__(self, params)
        self.q=[[0]*self.num_actions]*self.num_states
        self.hasard=0.1
    
    def start(self, initial_state):
        """See documentation in the base class"""

        action = self.policy(initial_state)
        return action

    def step(self, reward, action, prev_state, state):
        """See documentation in the base class"""
        #trouver ce qu'on va faire après
        new_action = self.policy(state)
        #mise à jour
        alpha=0.8
        gamma=0.2
        if action!=-1:
            self.q[prev_state][action]=self.q[prev_state][action]+alpha*(reward+gamma*self.q[state][new_action]-self.q[prev_state][action])
        
        new_action=action
        print(action)
        return action
        
    def policy(self, state):
        """See documentation in the base class"""
        maxi=[]
        equal=-1
        #print(self.q)
        for i in range(self.num_actions):
            if self.q[state][i]>max(self.q[state]):
                maxi=[i]
                equal=0
            if self.q[state][i]==max(self.q[state]):
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
                

