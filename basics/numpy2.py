import numpy as np

a1= np.array([
    [1,2],
    [2,1]
    ])

#print(a1[1,0])

# similarly for slicing a1[start: stop]


a2= np.array([
    [1,2,3],
    [2,1,4]
    ])

print(a2[0:2])   # first two rows extract
print(a2[:,1])  # all rows coloumn 1
