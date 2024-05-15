import matplotlib.pyplot as plt

def f1(x,y,z,t):
    return 10*(y-x)
def f2(x,y,z,t):
    return    x*(28-z)-y
    
def f3(x,y,z,t):
    return x*y-8*z/3


x =0
y =1
z = 0
t = 0
h = 0.01
X = [0]
Y = [1]
Z = [0]
T = [0]

for i in range(10000):
    a1 = h*f1(x,y,z,t)
    b1 = h*f2(x,y,z,t)
    c1 = h*f3(x,y,z,t)
    
    a2 = h*f1(x+a1/2 , y + a1/2 ,z +a1/2, t+ h/2)
    b2 = h*f2(x+b1/2 , y + b1/2 ,z +b1/2, t+ h/2)
    c2 = h*f3(x+c1/2 , y + c1/2 ,z +c1/2, t+ h/2)
    
    a3 =h*f1(x+a2/2 , y + a2/2 ,z +a2/2, t+ h/2)
    b3 = h*f2(x+b2/2 , y + b2/2 ,z +b2/2, t+ h/2)
    c3 = h*f1(x+c2/2 , y + c2/2 ,z + c2/2, t+ h/2)
    
    a4 = h*f1(x+a3,y+a3,z+a3,t+h)
    b4 = h*f2(x+b3,y+b3,z+b3,t+h)
    c4 = h*f3(x+c3,y+c3,z+c3,t+h)
    
    
    x = x + ((a1+2*(a2+a3)+a4)/6)
    y= y + ((b1+2*(b2+b3)+b4)/6)
    z = z + ((c1+2*(c2+c3)+c4)/6)    
    t = t+h
    
    
    X.append(x)
    Y.append(y)
    Z.append(z)



plt.plot(X,Y,'-')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
plt.plot(X,Z,'-')
plt.xlabel('X')
plt.ylabel('Z')
plt.show()

plt.plot(Z,Y,'-')
plt.xlabel('Z')
plt.ylabel('Y')
plt.show()


