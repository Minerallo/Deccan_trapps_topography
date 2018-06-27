import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

tableau=np.loadtxt(r'C:\Users\mikpo\github\Deccan_trapps_topography\etop_india2.txt')

long=tableau[:,0]
lat=tableau[:,1]
elevation=tableau[:,2]

etovect1=np.arange(min(lat),max(lat),(max(lat)-min(lat))/249)
##etovect=etovect1[::-1] #reverse
etovect=etovect1

j=[]
diffeto=[]
for i in range(len(etovect)):
    diffeto=abs(lat-etovect[i])
##    find the first index corresponding to the condition
    ind=np.nonzero(diffeto==min(diffeto))[0][0] 
    j.append(ind)
##    print(j)

latprof=lat[j]

k=[]
profiles=[]
k=np.nonzero(lat==latprof[0])
profiles=elevation[k]

for i in range(1,len(latprof)):
    k=np.nonzero(lat==latprof[i])
    profiles2=elevation[k]
    profiles=np.concatenate((profiles,profiles2))
    print(profiles)
    print('hello')
    
profiles3=np.reshape(profiles,(len(latprof),np.shape(k)[1]))
plt.pcolormesh(profiles3)
plt.show()

##profiles3=np.asmatrix(profiles3)
##plt.plot(profiles3)
##plt.show()

    
