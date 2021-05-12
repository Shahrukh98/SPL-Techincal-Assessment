import time;

# Fibonacci series using recursion
def fiboR(i):
        if(i==0 or i==1):
            return i
        else:
            return fiboR(i-2) + fiboR(i-1)
# Creating series with recursion

def RecSeries(number):
    start=time.time()
    fibs=[]
    for i in range(number):
        fibs.append(fiboR(i))
    end=time.time()
    print(f"Time taken through recursion: {end-start}")
    return fibs


# Fibonacci series using memoization
def fiboM(number,array):
    if(number==0 or number==1):
        return 1
    else:
        return array[number-2]+array[number-1]

# Creating series with memoization
def MemSeries(number):
    start=time.time()
    # Array that will hold all the calculated results
    fibs = []
    for i in range(number):
        # We pass the array along with the function for calculation of next fibonacci number
        fibs.append(fiboM(i,fibs))
    end=time.time()
    print(f"Time taken through memoization: {end-start}")
    return fibs

# Memoiztion means caching the previous results, since in fibonacci series we need to sum the previous 2 elements, so we can store that in a array and use those values instead of calculating the entire sum again. It saves both memory and time.

print(RecSeries(36))
print(MemSeries(36))