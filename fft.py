import numpy as np

image = [
[ 1,4,5,6 ],
[ 3, 5,5,2],
[ 3,6,7,8],
[8,7,6,5],
]

fft2 = [
    [0.707,0.707],
    [0.707,-0.707]
]


fft4 = [
    [1,1,1,1],
    [1,-1j,-1,1j],
    [1,-1,1,-1],
    [1,1j,-1,-1j],
]

def fft(image,A):
    print()
    print(f"Given image = \n{image}\n\nA = \n{A}\n")
    ia = np.round(np.dot(A,image),4)
    At = np.transpose(A)
    print(f"A * image = \n{ia}")
    sol = np.round(np.dot(ia,At),4)
    print(f"\nA * image * At = \n{sol}")
    return sol


def power(image):
    s = 0
    for i in image:
        for j in i:
            s+=j*j
    return s

ans = fft(image,fft4)
