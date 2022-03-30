import math








Nominal = 1.39
Compounding = 60


Effective = ((1 + (Nominal / Compounding) )** Compounding) - 1

print(Effective)