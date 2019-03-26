def to_roman (integer):
    result=''
    if int(integer)!=integer:
        break()
    
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
    
