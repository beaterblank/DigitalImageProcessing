import numpy as np 
print()

image = [
    [22,148,148,21],
    [23,149,154,22],
    [25,148,167,21],
    [25,154,149,23],
]

c1 = 50 #log transfrom
c2 = 10 #powelaw transform
g = 0.2
max_value = 255 #l-1


print("Given :")
print(f"{np.round(image,3)}")
print()
image =  np.array(image)

def negate(image,max_value):
    return max_value - image ;
def logtransform(image,normalize=True):
    if(normalize):
        image = rangenormalize(image)
    return np.log10(1+image) ;
def powelawtransform(image,g,normalize=True):
    if(normalize):
        image = rangenormalize(image)
    return np.power(image,g)
def rangenormalize(image):
    range = np.amax(image)-np.amin(image)
    return image/range


print(f"{c1 = } ;{c2 = }; {g = } ; {max_value = }")
print()
print(rangenormalize(image))
print(f"Neagative : \n{np.round(negate(image,255),2)}\n")
print(f"log transform : \n{np.round(logtransform(image),2)}\n")#true to make range normalized
print(f"log transform * c(={c1}) : \n{np.round(logtransform(image)*c1,2)}\n")#true to make range normalized
print(f"Powelaw : \n{np.round(powelawtransform(image,g),2)}\n")#true to make range normalized
print(f"Powelaw * c(={c2}) : \n{np.round(powelawtransform(image,g)*c2,2)}\n")#true to make range normalized

print()
input("press enter to exit...") 