# A simple generic DVR
# The quantum mechaanical problem into consideration is :
#                                "1-D Quantum system with coordinate x restricted to the interval (a,b)"
# For,  (a,b)=(-infinty,+infinity)                   -----QMSHO

###################################################################################################
# The grid point reperesentaion (matrix representation) of the kinetic energy operator is as follows:
###################################################################################################
import numpy as np

a=-20
b=20

def t(i, j):
    if i == j:
        d = 3.2898681337
    else:
        d = 2 / (i - j) ** 2
    c = (0.5 / d_x ** 2) * float((-1) ** (i - j)) * float(d)
    return c


r = 500   #Number of Basis Functions will be 2r, whereas number of diagonal entries will be (2r+1)*(2r+1), in which the middlemost entry of the square matrix (that willl be formed) will be 0.
m = []
d_x = (b-a) /(2*r+1)
for i in range(-r, r + 1):
    rows = []
    for j in range(-r, r + 1):
        x = t(i, j)
        rows.append(x)
    m.append(rows)
M = np.array(m)
print(M)

#################################################################################################
# The grid point representation (matrix representation) of potential energy operator is as follows:
#################################################################################################
import numpy as np


def v(x):
    k = 1
    z = 0.5 * k * (x) ** 2
    return z

xaxis = np.arange(a,b,d_x)
yaxis=[]
for x in xaxis:
    yaxis.append(v(x))
print("length=", len(xaxis), "xaxis=", xaxis)
print("length=", len(yaxis), "yaxis=", yaxis)
N = np.diag(yaxis)
print("N=", N)
##################################################################################
# The grid point representation (Matrix representation) of Hamiltonian is as follows:
##################################################################################
H = M + N
print("The Hamiltonian Matrix")
print(H)
eigenvalues, eigenvectors = np.linalg.eigh(H)
print("********************************************************")
print("Eigenvalues")
print("********************************************************")
print(eigenvalues)
print("********************************************************")
print("Eigenvectors")
print(eigenvectors)
print("********************************************************")
import numpy as np
import matplotlib.pyplot as plt

y = eigenvectors[:, int(input("The Wavefunction You wanna dance with="))]
print(y)
plt.figure(num=0, dpi=120)
plt.plot(xaxis,yaxis)
plt.plot(xaxis, y)
plt.title("Wavefunctions assocaited with QMSHO")
plt.xlabel("x=grid=p*d_x")
plt.ylabel("Psi")
# We are only getting limited no. of bound staes because oue boundries are not (-infinity, infinity) but (a,b), so bound states are boundry dependent.

