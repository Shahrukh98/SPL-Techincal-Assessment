def rotLeft(array,shift):
    if(shift==0 or len(array)==1):
        return array
    elif(shift>len(array)):
        shift=shift%len(array)
    for i in range(shift):
        temp=array[0]
        for j in range(0,len(array)-1):
            array[j]=array[j+1]
        array[len(array)-1]=temp
    return array

def reverseArr(array):
    revArr=[]
    tempArr=array
    for i in range(len(array)):
        temp = rotLeft(tempArr,1)
        revArr.insert(0,temp[len(temp)-1])
        tempArr=tempArr[0:len(tempArr)-1]
    return revArr


array1= [1,2,3,4,5]
array2= [6,7,8,9,10]
num = 2

print(f"The array {array} after {num} left rotation(s) is {rotLeft(array,num)}")

#  a. Can we use the rotLeft function written above to achieve this?
#       Yes, we can employ rotLeft by reducing the length of the array by 1 in each iteration, that way we will have the initial element of the array at the end.


print(f"The reversed array of {array} will be {reverseArr(array)}")


#  b. What will be the complexity of the program in terms of time if we solve it using rotLeft function?
#       If we use rotLeft to reverse the array, the first iteration will take time N (which is length of the array), and each subsequent iteration will take 1 less element, so complexity will be N * (N-1) * (N-2) ... 2 * 1, compressing these terms we get N factorial. The time complexity of the program will be N!.