
print()

(x1,y1) = [int(x) for x in input("x1 y1 = ").split()]
(x2,y2) = [int(x) for x in input("x2 y2 = ").split()]

from math import sqrt
#euclidian distance
def de(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)
#city block distance
def d4(x1,y1,x2,y2):
    return abs(x2-x1)+abs(y2-y1)
#chess board distance
def d8(x1,y1,x2,y2):
    return max([abs(x2-x1),abs(y2-y1)])
print()
print(f"eluclidian distance de = {de(x1,y1,x2,y2):.3f}")
print(f"cityblock distance  d4 = {d4(x1,y1,x2,y2):.1f}")
print(f"chessboard distance d8 = {d8(x1,y1,x2,y2):.1f}")
print()
input("press enter to exit...")