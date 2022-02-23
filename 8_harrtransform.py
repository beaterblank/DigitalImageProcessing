import numpy as np

image = [
    [5,4],
    [-3,0],
]

harr2 = [
    [0.707,0.707],
    [0.707,-0.707]
]

def harr(image,A):
    print()
    print(f"Given image = \n{image}\n\nA = \n{A}\n")
    ia = np.round(np.dot(A,image),2)
    At =  np.transpose(A)
    print(f"A * image = \n{ia}")
    sol = np.round(np.dot(ia,At),2)
    print(f"\nA * image * A = \n{sol}")
    return sol

harr(image,harr2)

print()
input("press enter to exit...")