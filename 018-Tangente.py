import math
an = float(input('digite o angulo q deseja?'))
r = math.radians(an)
s = math.sin(r)
c = math.cos(r)
t = math.tan(r)
print('\n Se o angulo for {} \n\n O seno será {:.3f} \n\n O coseno será {:.3f} \n\n E a trangente será {:.3f}'.format(an, s, c, t))