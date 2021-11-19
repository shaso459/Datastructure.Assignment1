list=[[1,12,3],[14,5,16],[7,8,9],[10,11,12],[13,14,15]]

def shmeth(li):
    return [item[-1] for item in li]

def factorial(x):
    return 1 if (x==1 or x==0) else x * factorial(x-1)

factorial_hold=[]

print("The last element of each sub list is : " , shmeth(list))

for i in list:
    factorial_hold.append(factorial(i[-1]))

print("The factorial of The last element of each sub list is : " , factorial_hold)