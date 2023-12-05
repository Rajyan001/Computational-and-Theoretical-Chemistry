import numpy as np
import matplotlib.pyplot as plt
d_t=0.001
x_0=80
v_0=0.5

xaxis=[]
aaxis=[]
vaxis=[]

time=np.arange(0,200.001,d_t)

#assigning values to constants
D_e=7.61
x_e=74.1
beta=0.0193
for t in time:
    x=(1-0.025*(d_t**2))*x_0 + v_0*d_t + 2*0.00008*(d_t**2)*(x_0)**3
    xaxis.append(x)
    a_0=-2*D_e*beta*np.exp(-beta*(x_0-x_e))*(1-np.exp(-beta*(x_0-x_e)))
    a=-2*D_e*beta*np.exp(-beta*(x-x_e))*(1-np.exp(-beta*(x-x_e)))
    aaxis.append(a)
    v=v_0+((a_0+a)/2)*d_t
    vaxis.append(v)
    x_0=x
    v_0=v
    a_0=a
#plotting the phase space
plt.plot(xaxis,vaxis)
plt.xlabel("x")
plt.ylabel("p")
plt.savefig("PS-MP.png")
_#%%

#%%

#%%

#%%

#%%
