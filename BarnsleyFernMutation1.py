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
    
    if r>=1 and r<=2:
        x_coo.append(0)
        y_coo.append(0.25*(y_coo[curr])-0.4)
        
    if r>=3 and r<=86:
        x_coo.append(0.95*(x_coo[curr])+0.005*(y_coo[curr])-0.002)
        y_coo.append(-0.005*(x_coo[curr])+0.93*(y_coo[curr])+0.5)
        
    if r>=87 and r<=93:
        x_coo.append(0.035*(x_coo[curr])-0.2*(y_coo[curr])-0.09)
        y_coo.append(0.16*(x_coo[curr])+0.04*(y_coo[curr])+0.02)
        
    if r>=94 and r<=100:
        x_coo.append(-0.04*(x_coo[curr])+0.2*(y_coo[curr])+0.083)
        y_coo.append(0.16*(x_coo[curr])+0.04*(y_coo[curr])+0.12)
        
    curr+=1

plt.title('Barnsley Fern Mutation')    
plt.scatter(x_coo,y_coo,s=0.3,edgecolor='green')
        
    

        