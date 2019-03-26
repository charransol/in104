def pretraitement (n):
    tab=[0,0,0,0]
    i=0
    while i<=3:
        tab[i]=n//10**(3-i)
        n=n%10**(3-i)
        i=i+1
    return(tab)
    

def to_lettre (integer,a,b,c):
    result=''
    #if int(integer)!=integer:
     #   break()
    
    if 5<=integer<=8:
        result=result+b
        integer=integer-5
    while 1<=integer<=3:
        result=result+a
        integer=integer-1
    if integer==4:
        result=result+a+b
    if integer==9:
        result=result+a+c
    return(result)
    
def to_roman(n):
    result=''
    tab=pretraitement(n)
    i=0
    while i<=3:
        if i==0:
            a='M'
            b=''
            c=''
        
        if i==1:
            a='C'
            b='D'
            c='M'
        if i==2:
            a='X'
            b='L'
            c='C'
        if i==3:
            a='I'
            b='V'
            c='X'
        
        integer=tab[i]
        result=result+to_lettre(integer,a,b,c)
        i+=1
    return(result)
    
        
        