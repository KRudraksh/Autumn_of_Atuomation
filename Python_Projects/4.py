import numpy as np
x=np.random.normal(size=(20,20))
y = np.array([20], dtype='int32')
for i in range(20):
    x[i]=(float(input("Element:")))

c=x.transpose()
z=np.matmul(c,x)
a=np.linalg.inv(z)
b=np.matmul(a,c)
f=np.matmul(b,y)

print(f)