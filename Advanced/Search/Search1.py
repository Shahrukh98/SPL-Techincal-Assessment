def searchPairs(array,num):
    pairs=[]
    for i in range(len(array)):
        for j in range(len(array)):
            if( i == j or array[i]+array[j]!=num):
                continue
            else:
                if({array[j],array[i]} not in pairs):
                    pairs.append({array[i],array[j]})
    return pairs


print(searchPairs([1,2,3,4,5,6,7,8],8))

