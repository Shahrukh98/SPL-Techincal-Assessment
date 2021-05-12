def findAbsMin(array):
    if(len(array)!=0):
        # Comparing the last and the first element and taking it as the initial absolute minimum
        minDiff=abs(array[-1]-array[0])
        # Then we iterate along the whole array checking the absolute adjacent minimum
        for i in range(len(array)-1):
            minDiff=min(minDiff,abs(array[i]-array[i+1]))
        return minDiff

result = findAbsMin([10, 12, 13, 15, 10])
print(result)