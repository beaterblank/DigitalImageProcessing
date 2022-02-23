import numpy as np

image = [
    [1,2],
    [2,1],
]

dct2 = [
    [0.707,0.707],
    [0.707,-0.707]
]


dct4 = [
    [0.5,0.5,0.5,0.5],
    [0.653,0.271,-0.271,-0.653],
    [0.5,-0.5,-0.5,0.5],
    [0.271,-0.653,0.63,-0.271],
]

def dct(image,A):
    print()
    print(f"Given image = \n{image}\n\nA = \n{A}\n")
    ia = np.round(np.dot(A,image),2)
    print(f"A * image = \n{ia}")
    sol = np.round(np.dot(ia,A),2)
    print(f"\nA * image * A = \n{sol}")
    return sol

dct(image,dct2)

print()
input("press enter to exit...")