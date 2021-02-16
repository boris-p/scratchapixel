def zCrossProduct(a, b, c):
    return (a[0]-b[0])*(b[1]-c[1])-(a[1]-b[1])*(b[0]-c[0])


vt = [(6, 14), (6, 3), (6, 3), (22, 3), (8, 8)]

print(zCrossProduct(*vt[0:3]))
print(zCrossProduct(*vt[1:4]))
print(zCrossProduct(*vt[2:5]))
print(zCrossProduct(*vt[3:5], vt[0]))
print(zCrossProduct(vt[4], vt[0], vt[1]))


print('and now reversed')
vt.reverse()
print(zCrossProduct(*vt[0:3]))
print(zCrossProduct(*vt[1:4]))
print(zCrossProduct(*vt[2:5]))
print(zCrossProduct(vt[4], vt[0], vt[1]))
print(zCrossProduct(vt[4], vt[0], vt[1]))
