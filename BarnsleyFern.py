import matplotlib.pyplot as plt
from random import randint

x_coo = []
y_coo = []

x_coo.append(0)
y_coo.append(0)

curr=0

#Affine transformations. For more info : https://en.wikipedia.org/wiki/Barnsley_fern
for i in range(1,50000):
    r = randint(1,100)
    
    if r==1:
        x_coo.append(0)
        y_coo.append(0.16*(y_coo[curr]))
        
    if r>=2 and r<=86:
        x_coo.append(0.85*(x_coo[curr])+0.04*(y_coo[curr]))
        y_coo.append(-0.04*(x_coo[curr])+0.85*(y_coo[curr])+1.6)
        
    if r>=87 and r<=93:
        x_coo.append(0.2*(x_coo[curr])-0.26*(y_coo[curr]))
        y_coo.append(0.23*(x_coo[curr])+0.22*(y_coo[curr])+1.6)
        
    if r>=94 and r<=100:
        x_coo.append(-0.15*(x_coo[curr])+0.28*(y_coo[curr]))
        y_coo.append(0.26*(x_coo[curr])+0.24*(y_coo[curr])+0.44)
        
    curr+=1
 
plt.title('Barnsley Fern')
plt.scatter(x_coo,y_coo,s=0.3,edgecolor='green')
        
    

        