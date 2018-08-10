import numpy as np
import matplotlib.pyplot as plt
np_a=np.array([1,2,3])
#print(np_a)
np_b=np.array([4,5,6])
#print(np_b)
np_sum=np_a+np_b

print(np_sum)
for i in np_sum:
    print(i)
print(np_sum.sum(axis=0))
print(np_a.sum())
print(np.vstack((np_a, np_b)))
print(np.hstack((np_a, np_b)))

x=[1,2,3,4]
y=[20,40,50,60]
