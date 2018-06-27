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
##    print(profiles)
##    print('hello')
    
profiles3=np.reshape(profiles,(len(latprof),np.shape(k)[1]))

profmat=np.asmatrix(profiles3)

M=[]
indmax=[]
elev=[]

elev=np.amax(profiles3, axis=1)

##l=profmat.max(axis=1)


for i in range(len(latprof)):
    l=np.nonzero(profiles3[i]==elev[i])[0][0] #YESS Found the mistake a 0 was missing Wohoo!
    M.append(l)

count,division=np.histogram(M,bins=20)
##plt.hist(M, bins=20)
##plt.show()

E=np.nonzero(count==max(count))[0][0]
diffindX=abs(M-count[E])

tolerance=65
mintol=round(count[E]-tolerance)
maxtol=round(count[E]+tolerance)

prof=[]
indmax2=[]
G=[]

for i in range(len(latprof)):
    if diffindX[i]>tolerance:
        prof=profiles3[i,mintol:maxtol]
        G=np.nonzero(profiles3[i]==max(prof))[0][0]
        indmax2.append(G)
    else:
        indmax2.append(M[i]);
        
diffindX2=abs(indmax2-count[E])


vect=np.linspace(0,len(latprof),len(latprof))
vect=np.round(vect)
plt.pcolormesh(profiles3,cmap='RdBu_r',shading='flat')
plt.plot(indmax2,vect,'b')
plt.title('Finding coastal escarpement, example:Western Ghats-India')
plt.show()
