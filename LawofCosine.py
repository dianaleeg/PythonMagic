import math
from turtle import *


#inputs
fl = float(input("first length: "))
sl = float(input("second length:"))
fangle = float(input("Angle: "))

#calculate hypotenuse
hyp1 = ((pow(fl,2) + pow(sl,2) - ((2)*(fl)*(sl)*math.cos(math.radians(fangle)))))

#square root
hyp2 = (pow(hyp1, 0.5))
print(hyp2)

#calculate fl angle
fl_angle = ((pow(sl,2)) + (pow(hyp2,2)) - (pow(fl, 2)))/ ((2)*(sl)*(hyp2))

#arccos of fl_angle
fl_angle = math.acos(fl_angle)

#convert from radians to degrees
fl_angle = math.degrees(fl_angle)
print(fl_angle)

## DRAWING ##

me = Turtle() 
me.goto(0,0)
me.down()
me.forward(fl)
me.left(180-fangle)
me.forward(sl)
me.left(180-fl_angle)
me.forward(hyp2)
