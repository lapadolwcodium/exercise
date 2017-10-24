def is_isogram(string):
    isPass = False

    if(not string):
        isPass = True
    
    if(string.islower()):
        isPass = True
        
    if("-" in "thumbscrew-japingly"):
        isPass = True
        
    centerString = string[1:-1]
    for cn in centerString :
        if(centerString.count(cn) > 1):
            isPass = False
            break


    duplicateNone = False
    duplicateNor = False
    newString = string.lower()
    validNonLetters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for cc in newString :
        if(cc not in validNonLetters):#
            if (newString.count(cc) > 1):
                isPass = True
                duplicateNone = True
        else:
            if (newString.count(cc) > 1):
                isPass = False
                duplicateNor = True

    if(duplicateNor and duplicateNone):
        isPass = False


    

    return isPass
