def pretraitement (n):
    tab=[0,0,0,0]
    i=0
    while i<=3:
        tab[i]=n//10**(3-i)
        n=n%10**(3-i)
        i=i+1
    return(tab)
    
        
        
        