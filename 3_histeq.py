from tabulate import tabulate
from numpy import transpose as t

hist = [8,14,16,12,2,3,4,2]

levels = range(len(hist))
n = sum(hist)
pk = [x for x in hist]
sum =0
sk = []
for i in pk:
    sum+=i
    sk.append(sum)
skxm = [x*(len(hist)-1)/n for x in sk]
sol = [round(x) for x in skxm]
print()
print("Hist equalization : \n")
all = [levels,hist,pk,sk,skxm,sol]
print(tabulate(t(all),headers=["Gray\nLevel","\nnk","\ncount(n)","cumulative\ncount",f"New Intensity\n=c*(L-1)/sum(n)","Intensity\nafter HE"],floatfmt=(".0f",".0f",".0f",".0f",".2f",".0f")))
print()
input("press enter to exit...")
