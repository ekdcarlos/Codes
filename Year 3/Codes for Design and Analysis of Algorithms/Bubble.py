import time
def Bubblesort(input):
    n = len(input)
    for i in range(n):
        isswappable = False
        for j in range(0,n-i-1):
            if input[j] > input[j+1]:
                input[j], input[j+1] = input[j+1], input[j]
                isswappable = True
        if not isswappable:
            break 
    return input
execution_time = time.time()
print(Bubblesort([50, 90, 30, 20, 10]))
print("Time taken:", time.time() - execution_time)
Bubblesort_time =  time.time() - execution_time