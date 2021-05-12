def insertNum(array,number):
    if(len(array)==0):
        return [number]
    else:
        for i in range(len(array)):
            if(array[i]>number):
                array.insert(i,number)
                return array
            else:
                array.append(number)
                return array


def DistributeArray(array,pivot):
    if(len(array)%2 == 0):
        # return "Pivot is not in array"
        left = array[0:len(array)/2]
        right = array[len(array)/2:len(array)-1]
        print(left,right)
    else:
        left=[]
        right=[]
        for i in array:
            if(i!=pivot):    
                if(i<pivot):
                    left=insertNum(left,i)
                else:
                    right=insertNum(right,i)
        return left+[pivot]+right


print(DistributeArray([30,1,-1,-2,2,-3,3,0],0))

