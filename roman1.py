def to_roman (integer):
    result=''
    if int(integer)!=integer:
        break()
    while integer>=1000:
        integer=integer-1000
        result=result+'M'
    while 100<=integer<=399:
        
        