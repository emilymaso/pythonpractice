import sys
import numpy as np
#print(sys.argv[0])
#print(len(sys.argv))
#print(sys.argv)
#lines = sys.stdin.readlines()
#lines = [line.strip('\n') for line in lines]
#azi=[]
#eli=[]
#uva=[]
#for line in lines:
#    f=line.split()
#    azi.append(f[0])
#    eli.append(f[1])
#    uva.append(f[2])
count=0
arr=np.zeros(shape=(5,5))
for i in range(5):
    for j in range(5):
        arr[i,j]=count
        count+=1.0
print(arr)

#f = open('result.txt','w')
#for i in range(5):
#    l=arr[i,:]
#    for j in range(5):
#        f.write("%j %5.2f\n" % (l[j]))
#f.close()

np.savetxt('result.txt', arr, delimiter=' ',fmt='%f')
