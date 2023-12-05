import numpy as np
import matplotlib.pyplot as plt
d_t=0.001
x_0=-0.2
v_0=0.5

xaxis=[]
aaxis=[]
vaxis=[]

time=np.arange(0,100.001,d_t)

for t in time:
    x=(1-0.025*(d_t**2))*x_0 + v_0*d_t + 2*0.00008*(d_t**2)*(x_0)**3
    xaxis.append(x)
    a_0=4*0.00008*(x_0**3)-2*0.025*x_0
    a=4*0.00008*(x**3)-2*0.025*x
    aaxis.append(a)
    v=v_0+((a_0+a)/2)*d_t
    vaxis.append(v)
    x_0=x
    v_0=v
    a_0=a
print(xaxis)
print(aaxis)
print(vaxis)
#plt.title("Phase Space")
plt.plot(xaxis,vaxis)
plt.xlabel("x")
plt.ylabel("p")
plt.savefig("PS-SDWP.png")
#%%
