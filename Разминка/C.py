import math

n = list(map(int, input().split()))

a = n[:2]
b = n[2:]

target_circle = 0
target_line = 0

xr = (a[0]**2 + a[1]**2)**(1/2)
yr = (b[0]**2 + b[1]**2)**(1/2)

if xr >= yr:
    target_circle += xr - yr
    target_line += xr
elif yr > xr:
    target_circle += yr - xr
    target_line += xr

target_line += yr

x = a[0]-b[0]
y = a[1]-b[1]
angle = 0

if yr != 0 and xr != 0:
    angle_a = math.atan2(a[1],a[0])
    angle_b = math.atan2(b[1],b[0])
    if angle_a >= 0 and angle_b >= 0:
        angle = abs(angle_a - angle_b)
    elif angle_a >= 0 and angle_b < 0 or angle_a < 0 and angle_b >= 0:
        angle = min(2 * math.pi - (abs(angle_a) + abs(angle_b)), (abs(angle_a) + abs(angle_b)))
    elif angle_a < 0 and angle_b < 0:
        angle = abs(angle_a - angle_b)
    angle = angle * 180 / math.pi
    target_circle += math.pi * min(xr,yr) * abs(angle) / 180

print(min(target_circle,target_line))