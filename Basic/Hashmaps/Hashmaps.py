def shareSubString(strA,strB):
    result = False
    charsA = {}
    charsB = {}
    for i in strA:
        if( i not in charsA):
            charsA[i] = len(charsA)+1
    j=1
    for i in strB:
        if( i in charsA):
            charsB[i]= charsA[i]
            result = True
        else:
            charsB[i]=len(charsA)+j
            j+=1
    return result

print(shareSubString("abcd",'def'))


def compareMaps(map1,map2):
    similarity=[]
    result = True
    if(len(map1) > len(map2)):
        for i in map1:
            if ( i not in map2):
                result = False
            elif( map1[i] != map2[i] ):
                result = False
            else:
                similarity.append(i)
    else:
        for i in map2:
            if ( i not in map1):
                result = False
            elif( map1[i] != map2[i] ):
                result = False
            else:
                similarity.append(i)
    if(not result):
        ## We will print similarity only when the result is false, because when the maps are similar, it is implied that all the elements are same
        print(f"The similar elements are : {similarity}")
    return result

print(compareMaps({"a":1,"b":2,"c":3},{"c":3,"b":2,"a":1}))

print(compareMaps({"a":1,"b":2,"d":3},{"x":3,"c":2,"a":1}))