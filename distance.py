#calculating distance
import math
x1=float(input("enter x1: "))
y1=float(input("enter y1: "))
x2=float(input("enter x2: "))
y2=float(input("enter y2: "))

dis=((x2-x1)**2+(y2-y1)**2)
dist=math.sqrt(dis)
print("distance is {}".format(dist))
