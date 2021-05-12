def recursiveMean(_array,_length):
    return _array[0]/_length if len(_array)==1 else recursiveSum(_array[:len(_array)-1],_length)+_array[len(_array)-1]/_length

x= [1,2,3,4,5,6,7,8,9,10]

print(recursiveMean(x,len(x)))
