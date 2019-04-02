import numpy as np
import random
import math
import pickle

theta = math.atan(.2/.6)
#radius = .09 / math.sin(theta)
radius = .35
# x from (b(0),b(1)), y from (b(2),b(3))
# possible points in [-1:0, -1:1]
b = [radius - 1.8, -radius, radius - 1, 1 - radius]
genCoorVST = np.zeros([300,4,2])

def distance(p1, p2):
    d = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    return d < (2*radius)
    
k = 0
while k < 100:
    first    = [random.uniform(b[0],b[1]), random.uniform(b[2],b[3])]
    second   = [random.uniform(b[0],b[1]), random.uniform(b[2],b[3])]
    third    = [random.uniform(b[0],b[1]), random.uniform(b[2],b[3])]
    fourth   = [random.uniform(b[0],b[1]), random.uniform(b[2],b[3])]
    if  distance(first,second) or distance(first,third) or distance(first,fourth) or distance(second,third) or distance(second,fourth) or distance(third,fourth): 
        k = k
    else: 
        genCoorVST[k,0] = first
        genCoorVST[k,1] = second
        genCoorVST[k,2] = third
        genCoorVST[k,3] = fourth
        k = k+1

print(np.shape(genCoorVST))
print("done")
f = open('genCoorVST.pckl', 'wb')
pickle.dump(genCoorVST,f)
f.close()