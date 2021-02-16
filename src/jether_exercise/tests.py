import math


def zCrossProduct(a, b, c):
    return (a[0]-b[0])*(b[1]-c[1])-(a[1]-b[1])*(b[0]-c[0])


# vt = [(6, 14), (6, 3), (6, 3), (22, 3), (8, 8)]

# print(zCrossProduct(*vt[0:3]))
# print(zCrossProduct(*vt[1:4]))
# print(zCrossProduct(*vt[2:5]))
# print(zCrossProduct(*vt[3:5], vt[0]))
# print(zCrossProduct(vt[4], vt[0], vt[1]))


# print('and now reversed')
# vt.reverse()
# print(zCrossProduct(*vt[0:3]))
# print(zCrossProduct(*vt[1:4]))
# print(zCrossProduct(*vt[2:5]))
# print(zCrossProduct(vt[4], vt[0], vt[1]))
# print(zCrossProduct(vt[4], vt[0], vt[1]))


vt = [(3, 14), (6, 3), (22, 3), (8, 8)]
tt = [(5, 10), (5, 5), (10, 5)]

# counter clock wise
cross = [(12, 6),
         (18, 6),
         (18, 12),
         (12, 12),
         (12, 18),
         (6, 18),
         (6, 12),
         (0, 12),
         (0, 6),
         (6, 6),
         (6, 0),
         (12, 0)]


def point_angle(a, b, c):
    rad = math.atan2(
        c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0])
    ang = math.degrees(rad)
    print('rad angle is', rad)
    ang = ang + 360 if ang < 0 else ang

    z_cross_product = (a[0]-b[0])*(b[1]-c[1])-(a[1]-b[1])*(b[0]-c[0])
    return (ang, z_cross_product)


print(point_angle(vt[2], vt[1], vt[0]))
print(point_angle(vt[0], vt[1], vt[2]))

print(point_angle(tt[2], tt[1], tt[0]))
print(point_angle(tt[0], tt[1], tt[2]))

print("cross test")
signs = [print(point_angle(a, b, c))
         for a, b, c in zip(cross[2:], cross[1:], cross)]

print("reversed cross test")
cross.reverse()
signs = [print(point_angle(a, b, c))
         for a, b, c in zip(cross[2:], cross[1:], cross)]


rectangle = [(0, 0),
             (6, 0),
             (6, 6),
             (0, 6)]

print('-------------------------------------------')
print('-------------------------------------------')
print('-------------------------------------------')
print('rectangle')
[print(point_angle(a, b, c))
 for a, b, c in zip(rectangle[2:], rectangle[1:], rectangle)]

print('reversed rectangle')
rectangle.reverse()
[print(point_angle(a, b, c))
 for a, b, c in zip(rectangle[2:], rectangle[1:], rectangle)]

rotated_rectangle = [(4.208044, -1.067017),
                     (7.067017, 4.208044),
                     (1.791956, 7.067017),
                     (-1.067017, 1.791956)
                     ]

print('-------------------------------------------')
print('-------------------------------------------')
print('-------------------------------------------')
print('rotated_rectangle')
[print(point_angle(a, b, c))
 for a, b, c in zip(rotated_rectangle[2:], rotated_rectangle[1:], rotated_rectangle)]

print('reversed rotated_rectangle')
rotated_rectangle.reverse()
[print(point_angle(a, b, c))
 for a, b, c in zip(rotated_rectangle[2:], rotated_rectangle[1:], rotated_rectangle)]
