# this function valid if a string s ∈ [a-z]
def isAlphanumeric(s):
    res = s.isalpha()
    return res

# function that counts the frequency of each element of the string s
def counter(s):
    dicfrec = {}
    for char in s:
            cant = s.count(char)
            if dicfrec:
                if (char in dicfrec)==False:
                  dicfrec[char] = cant
            else:
                dicfrec[char] = cant  
    return dicfrec

#this function creates a dictionary with the number of repetitions each value in the counter list
def counterfrec(frec):
    dic = {}
    for x in frec:
        cant = frec.count(x)
        dic[x] = cant
    return (dic)

#function validates our string s
def isValid(s):
    dic_frec=counter(s)
    frec_char = set(dic_frec.values())
    if len(frec_char) == 1:
        return True
    else:
        frec_group = counterfrec(list(dic_frec.values()))
        for a,b in frec_group.items():
            if (a == b) and (a==1):
                return True
        #get the keys and values to my dictionary
        keys= list(frec_group.keys())
        values=list(frec_group.values())
        dif = abs(keys[0]-keys[1])
        if (dif == 1):
            for x in values:
                if x == 1:
                    return True          
    return False        


        
#main program 
def main(string):
    if isAlphanumeric(string):
        if isValid(string):
            return "YES"
        else:
            return "NO"
    return "cannot validate string should be valid"  
