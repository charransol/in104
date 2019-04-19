from environments.Environment import Environment
from scipy import *


def cree_labyrinthe(n,s,h,w):
    #n=EnvironmentGrid2D.num_states
    lab=zeros(n+1)
    #s=EnvironmentGrid2D.terminal_state
    #h=EnvironmentGrid2D.h
    #w=EnvironmentGrid2D.w
    
    haut=0
    droite=1
    bas=2
    gauche=3
    lab[s]=1
    dir1=random.randint(0,4)
    dir2=random.randint(0,4)
    extremite=[s]

    
    while (len(extremite)!=0):
        for e in extremite:
            dir1=random.randint(0,4)
            dir2=random.randint(0,4)
            dir3=random.randint(0,4)
            while dir2==dir1:
                dir2=random.randint(0,4)
            while dir3==dir2 or dir3==dir1:
                dir3=random.randint(0,4)
            e1=e
            e2=e
            e3=e
            c1=0
            c2=0
            c3=0
            if (dir1==haut):
                for i in range(3):
                    if e1//w>0 and lab[e1-w]==0:
                        c1+=1
                        lab[e1-w]=1
                        e1=e1-w
                if c1==3:
                    extremite.append(e-3*w)
            
            if (dir1==bas):
                for i in range(3):
                    if e1//w<(h-1) and lab[e1+w]==0:
                        c1+=1
                        lab[e1+w]=1
                        e1=e1+w
                if c1==3:
                    extremite.append(e+3*w)
                    
            if (dir1==droite):
                for i in range(3):
                    if e1%w<(w-1) and lab[e1+1]==0:
                        c1+=1
                        lab[e1+1]=1
                        e1=e1+1
                if c1==3:
                    extremite.append(e+3)
                    
            if (dir1==gauche):
                for i in range(3):
                    if e1%w>0 and lab[e1-1]==0:
                        c1+=1
                        lab[e1-1]=1
                        e1=e1-1
                if c1==3:
                    extremite.append(e-3)
                    
            if (dir2==haut):
                for i in range(3):
                    if e2//w>0 and lab[e2-w]==0:
                        c2+=1
                        lab[e2-w]=1
                        e2=e2-w
                if c2==3:
                    extremite.append(e-3*w)
            
            if (dir2==bas):
                for i in range(3):
                    if e2//w<(h-1) and lab[e2+w]==0:
                        c2+=1
                        lab[e2+w]=1
                        e2=e2+w
                if c2==3:
                    extremite.append(e+3*w)
                    
            if (dir2==droite):
                for i in range(3):
                    if e2%w<(w-1) and lab[e2+1]==0:
                        c2+=1
                        lab[e2+1]=1
                        e2=e2+1
                if c2==3:
                    extremite.append(e+3)
                    
            if (dir2==gauche):
                for i in range(3):
                    if e2%w>0 and lab[e2-1]==0:
                        c2+=1
                        lab[e2-1]=1
                        e2=e2-1
                if c2==3:
                    extremite.append(e-3)
            
            '''if (dir3==haut):
                for i in range(3):
                    if e3//w>0 and lab[e3-w]==0:
                        c3+=1
                        lab[e3-w]=1
                        e3=e3-w
                if c3==3:
                    extremite.append(e-3*w)
            
            if (dir3==bas):
                for i in range(3):
                    if e3//w<(h-1) and lab[e3+w]==0:
                        c3+=1
                        lab[e3+w]=1
                        e3=e3+w
                if c3==3:
                    extremite.append(e+3*w)
                    
            if (dir3==droite):
                for i in range(3):
                    if e3%w<(w-1) and lab[e3+1]==0:
                        c3+=1
                        lab[e3+1]=1
                        e3=e3+1
                if c3==3:
                    extremite.append(e+3)
                    
            if (dir3==gauche):
                for i in range(3):
                    if e3%w>0 and lab[e3-1]==0:
                        c3+=1
                        lab[e3-1]=1
                        e3=e3-1
                if c3==3:
                    extremite.append(e-3) '''
            
            extremite.remove(e)
                    
                    
    return(lab)    
        
        
        
    
    
 