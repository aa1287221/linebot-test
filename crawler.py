import numpy as np
a=[27,17,200,50]
b=[24,15,200,70]
c=[27,15,150,50]
d=[30,16,150,70]
np.savez('plant.npz',gold=a,santa=b,spring=c,tiger=d)