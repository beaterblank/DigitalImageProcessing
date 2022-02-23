v = [56,8,-2,4,14,-8,6,-2]

def avg(v):
    if(len(v)==1):
        return
    a = []
    d = []
    for i in range(0,len(v),2):
        a.append((v[i]+v[i+1])/2)
        d.append((v[i]-v[i+1])/2)
    print(f"{len(a)} \n{a = } \n{d = }\n")
    avg(a)
        
print(f"\nGiven V = {v}\n")
avg(v)