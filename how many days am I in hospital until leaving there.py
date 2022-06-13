#Until leaving hospital, how many days?

import math


#Lymphatic vessels radius of 24-January, 7-February and normal
r_2 = 20.5
r_1 = 18.0
r_0 = 5.0

#Pi
pi = 3.141

#days
t_0 = 15

#Lymphatic vessels length which have cancer
l = int(input("Input proper length of lymphatic vessels having cancer:"))

#How small the thickness of lymphatic vessels radius because of anti-cancer agent per day
r_per = ((pi * l * r_2 * r_2) - (pi * l * r_1 * r_1)) / t_0

#How small the thickness of lymphatic vessels radius because of anti-cancer agent
t = 1
r = 18.0

#How long is the lymphatic vessel radius
print(math.sqrt((r_1 * r_1) - ((r_per * 38) / (pi * l))))

while r > r_0:
    r = math.sqrt((r_1 * r_1) - ((r_per * t) / (pi * l)))
    t += 1

print(t - 1 - 38)