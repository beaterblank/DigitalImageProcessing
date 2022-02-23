import numpy as np
from math import sqrt

image = np.array([
    [1,2],
    [3,4],
])

A = np.array([
    [1/sqrt(2),1/sqrt(2)],
    [1/sqrt(2),-1/sqrt(2)]
])

def power(image):
    s = 0
    for i in image:
        for j in i:
            s+=j*j
    return s

def transform(image,A):
    print()
    print(f"Given image = \n{image}\n\nGiven A = \n{A}\n")
    print(f"A*At = \n{np.round(np.dot(A,np.transpose(A)),2)}\n")
    At = np.transpose(A)
    ia = np.round(np.dot(A,image),4)
    print(f"A * image = \n{ia}")
    sol = np.round(np.dot(ia,At),4)
    print(f"\nA * image * At = \n{sol}")
    ps = power(sol)
    pi = power(image)
    if(ps==pi):
        print(f"\ntransform preserves power\npower(sol)={ps:.2f}=power(image)")
    else:
        print(f"\ntransform does not preserve power \npower(sol)={ps:.2f}\npower(image)={pi:.3f}")
    return sol

transform(image,A)

print()
input("press enter to exit...")
