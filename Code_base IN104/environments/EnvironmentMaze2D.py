__author__ = "Florence Carton"
__credits__ = ["Florence Carton", "Freek Stulp", "Antonin Raffin"]

import random
from environments.Environment import Environment
import time
from environments.cree_labyrinthe import cree_labyrinthe
from environments.cree_labyrinthedur import cree_labyrinthedur
from environments.cree_labyrinthedur2 import cree_labyrinthedur2
from math import sqrt

class EnvironmentMaze2D(Environment):

    LEFT = 0
    RIGHT = 1
    HIGH = 2
    LOW = 3
    


    def __init__(self,params):
        
        n = int(params['num_cells_maze2D'])
        q=2
        Q=[]
        r=1
        while(n>q):
            r=n%q
            if (r==0):
                Q.append(q)
            q+=1
        w=Q[random.randint(0,len(Q)-1)]
        while (w<sqrt(n)//3 or w>(sqrt(n)-sqrt(n)//10)):
            w=Q[random.randint(0,len(Q)-1)]
        h=n//w
        

        
        self.num_states=n #crée une grille de largeur w de hauteur hen fct de numcellesgrid
        self.h=h
        self.w=w 
        
        # Check if there are enough cells 
        assert self.num_states>1, "Number of cells must be 2 or larger"
        
        # Number of actions is always 2 (LEFT, RIGHT)
        self.num_actions = 4
  
        # Set to most right cell (will change in reset(...) anyway)
        self.current_state  =  0

        # end state
        self.terminal_state = random.randint(0,self.num_states) # arbitrary
    
    
        self.lab=cree_labyrinthedur2(self.num_states,self.terminal_state,self.h,self.w)
        self.viewer = None


    def step(self, action):
        """See documentation in the base class"""
        
        # Decrease agent_cell by 1 if you go left, but only if you are not
        # in the left-most cell already
        if action==EnvironmentMaze2D.LEFT:
            if self.current_state%self.w>0 and self.lab[self.current_state-1]==1:
                self.current_state -= 1

        # Increase agent_cell by 1 if you go right, but only if you are not
        # in the right-most cell already
        if action==EnvironmentMaze2D.RIGHT:     
            if self.current_state%self.w<(self.w-1) and self.lab[self.current_state+1]==1:
                self.current_state += 1
        
        # Decrease agent_cell by 1 if you go left, but only if you are not
        # in the left-most cell already
        if action==EnvironmentMaze2D.HIGH:
            if self.current_state//self.w>0 and self.lab[self.current_state-self.w]==1:  
                self.current_state -= self.w

        # Increase agent_cell by 1 if you go right, but only if you are not
        # in the right-most cell already
        if action==EnvironmentMaze2D.LOW:     
            if self.current_state//self.w<(self.h-1) and self.lab[self.current_state+self.w]==1:
                self.current_state += self.w 
        
        
        is_done = self.current_state == self.terminal_state
       
        if is_done:
            # If you are in the terminal state, you've found the exit: reward!
            reward = 1000
        else:
            # Still wandering around: -1 penalty for each move
            reward = -1
  
        next_state = self.current_state
      
        return [next_state,reward,is_done]
        

    def reset(self):
        """See documentation in the base class"""

        # Put agent at random position (but not in a terminal state)
        cell = random.randint(0,self.num_states-1)
        while cell == self.terminal_state or self.lab[cell]==0:
            cell = random.randint(0,self.num_states-1)
        self.current_state = cell
        
        # Return first observed state
        return self.current_state


    def render(self):
        screen_width = 500
        screen_height = 500
        cell_width = screen_width/self.w
        cell_height = screen_height/self.h

        if self.viewer is None:
            from gym.envs.classic_control import rendering
            self.viewer = rendering.Viewer(screen_width, screen_height)

            l,r,t,b = 0, cell_width, cell_height, 0
            cell = rendering.FilledPolygon([(l,b), (l,t), (r,t), (r,b)])
            cell.set_color(0,0,1) # blue for current state
            
            endo=self.terminal_state
            endx=endo%self.w*cell_width
            endy = endo//self.w*cell_height
            c,d,e,f=endx, endx+cell_width, endy+cell_height, endy
            end = rendering.FilledPolygon([(c,f), (c,e), (d,e), (d,f)])
            end.set_color(1,0,0) # red for end state (note : end state is 0)
            self.viewer.add_geom(end)
            
            for i in range(self.num_states):
                lb = self.lab[i]
                if lb==0:
                    lbx = i%self.w*cell_width
                    lby = i//self.w*cell_height
                    laby = rendering.FilledPolygon([(l+lbx,b+lby), (l+lbx,t+lby), (r+lbx,t+lby), (r+lbx,b+lby)])
                    laby.set_color(0,1,0) # green for maze
                    self.viewer.add_geom(laby)
            
            self.celltrans = rendering.Transform()
            cell.add_attr(self.celltrans)
            self.viewer.add_geom(cell)
            


        if self.current_state is None: return None
        
        state = self.current_state
        cellx = state%self.w*cell_width
        celly = state//self.w*cell_height
        self.celltrans.set_translation(cellx,celly)
        
        
        

        
        time.sleep(0.01)


        return self.viewer.render()


    def close(self):
        if self.viewer: self.viewer.close()