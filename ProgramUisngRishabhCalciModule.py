#using RishabhCalci module in our Python program

import RishabhCalci
print(RishabhCalci.x)
print(RishabhCalci.y)
RishabhCalci.add(14,25)
RishabhCalci.mul(10,25)
RishabhCalci.sub(125,25)
RishabhCalci.div(100,25)


import RishabhCalci as r
print(r.x)
print(r.y)
r.add(14,25)
r.mul(10,25)
r.sub(125,25)
r.div(100,25)

from RishabhCalci import x,add
print(x)
add(156,987)

from RishabhCalci import add as a,mul as p
a(100,560)
p(256,10)

from RishabhCalci import *
print(x)
print(y)
add(125,652)
mul(10,25)
sub(156,56)
div(140,70)