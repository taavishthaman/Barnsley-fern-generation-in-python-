import matplotlib.pyplot as plt
from random import randint

#Setting coordinates of the triangle
X1=-10
Y1=0

X2=10
Y2=0

X3=0
Y3=10

X0=0
Y0=0

x_coo = []
y_coo = []

for i in range(0,100000):
    r = randint(1,3)
    
    if r==1:
        X0 = (X0+X1)/2
        Y0 = (Y0+Y1)/2
        
    if r==2:
        X0 = (X0+X2)/2
        Y0 = (Y0+Y2)/2
        
    if r==3:
        X0 = (X0+X3)/2
        Y0 = (Y0+Y3)/2
        
    x_coo.append(X0)
    y_coo.append(Y0)
    
plt.title('Sierpinski Triangle')
plt.scatter(x_coo, y_coo, s=0.3)
