#selection sort
import time
def selection (input):
    n = len(input)
    for i in range(n):
        minimum = i
        for j in range(i+1,n):
            if input[j] < input[minimum]:
                minimum = j
                input[i], input[minimum] = input[minimum], input[i]
    return input
execution_time = time.time() #declaring time
print(selection([50, 90, 30, 20, 10])) #calling function
print("Time taken:", time.time() - execution_time) #calling function time
Selection_time = time.time() - execution_time

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

if Selection_time > Bubblesort_time:
    print("Selection sort algorithm kicks ass")
else:
    print("Bubble sort algoritm kicks ass")