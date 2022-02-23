#mean highpass 

import numpy as np

def getat(image,at_y,at_x,ks,default = 0):
    ret = []
    sx,sy=at_x-int(ks/2),at_y-int(ks/2)
    sxc = at_x-int(ks/2)
    for j in range(ks):
        temp = []
        for i in range(ks):
            val = default
            if(inImage(image,sx,sy)):
                val = image[sy][sx]
            temp.append(val)
            sx+=1
        sy+=1
        sx=sxc
        ret.append(temp)
    return ret

def inImage(image,x,y):
    sy = len(image)
    sx = len(image[0])
    #print(f"{x}/{y}")
    if(x<0 or y<0 or y>=sy or x>=sx):
        return False
    else:
        return True

#change the input here
image = [
    [10,20,10,20],
    [10,10,10,10],
    [10,20,10,20],
    [10,10,10,10],
]

mean = np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]
])/9

highpass = np.array([
    [-1,-1,-1],
    [-1,8,-1],
    [-1,-1,-1]
])

def kernalfilter(image,kernal):
    print(f"Given image : \n{image}")
    ret = []
    for y in range(len(image)):
        temp=[]
        for x in range(len(image[0])):
            arr = np.array(getat(image,y,x,len(kernal)))
            val = np.sum(np.multiply(arr,kernal))
            if(val<0):
                val = 0
            if(val>255):
                val = 255
            temp.append(val)
            print(f"{x = };{y = }\n\n{arr}\n\nsum = {val:.2f}\n-----------")
        ret.append(temp)
    ret = np.round(np.array(ret),2)
    print(f"sol : \n{ret}")
    return ret

kernalfilter(image,mean)
print()
input("press enter to exit...")

