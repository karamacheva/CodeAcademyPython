def isValidPassword(passwd):
    '''
    This is a function to check if password is valid
    '''
    countLower,countUpper,countDigit,countSpecial=0,0,0,0
    if(len(passwd)<8 or len(passwd)>15):
        return False
    for i in passwd:
        if (i>='a' and i<='z'):
            countLower+=1
        if (i>='A' and i<='Z'):
            countUpper+=1
        if (i>='0'and i<='9'):
            countDigit+=1
        if(i=='$' or i=='#' or i=='@'):
            countSpecial+=1
    sumCharacters=countLower+countUpper+countDigit+countSpecial
    if(countLower>=2 and countUpper>=1 and countDigit>=3 and countSpecial>=1 and sumCharacters==len(passwd)):
        return True
    else:
        return False 
        
#passwd1='ABdv1234@7'
#passwd2='aF1#'
#passwd3='2w3E'
#passwd4='2We3345'
#print(isValidPassword(passwd1))
#print(isValidPassword(passwd2))
#print(isValidPassword(passwd3))
#print(isValidPassword(passwd4))                       
listofPasswd=['ABdv1234@7','aF1#','2w3E','2We3345']
listofValidPasswd=[i for i in listofPasswd if isValidPassword(i)==True]
print(listofValidPasswd)