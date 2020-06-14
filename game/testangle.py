import math

x1=2
y1=1
x2=5
y2=5

angle = math.atan((y2-y1)/(x2-x1)) * 57.29
print(angle)

angle = math.atan2(y2-y1,x2-x1) * 57.29
print(angle)
