import numpy as np
from numpy import loadtxt
lines=np.genfromtxt('Rockpaperscissors.txt',dtype='str')
col1=np.array(lines[:,0])
col2=np.array(lines[:,1])
col2[col2 == 'X'] = 1
col2[col2 == 'Y'] = 2
col2[col2 == 'Z'] = 3
col2=col2.astype(np.float)
mkam=col1[col2==1]
mpap=col1[col2==2]
mnoz=col1[col2==3]
wyg=(len(mkam[mkam=='C'])+len(mpap[mpap=='A'])+len(mnoz[mnoz=='B']))*6
rem=(len(mkam[mkam=='A'])+len(mpap[mpap=='B'])+len(mnoz[mnoz=='C']))*3
print('Suma punktow to: ', sum(col2)+wyg+rem)
