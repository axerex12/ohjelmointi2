import numpy as np
a = 2.493
b = 0.911
aa = 137.7
bb = 62.3
lista = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]
print("1a")
print("%.2f" %np.degrees(a))
print("1b")
print("%.2f" %np.degrees(b))
print("2a")
print("%.2f" %np.radians(aa))
print("2b")
print("%.2f" %np.radians(bb))

for i in lista:
  print(f"{i} astetta {"%.3f" % np.radians(i)}")

kateetti1 = 1.6
kateetti2 = 2.3

hypotenuusakahteen = kateetti1*kateetti1 + kateetti2*kateetti2

print(f"hypotenuusa on {"%.1f" % np.sqrt(hypotenuusakahteen)} metriä ")