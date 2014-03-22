from pyplasm import *
plum = [2.21,1.60,2.21]
pointsf0 = [[0,0],[0,12],[30,0], [30,12]]
floor0 = (JOIN(AA(MK)(pointsf0)))
#floor0 = COLOR(plum)(CUBOID([30,12]))
#VIEW(base)


p1= T([1,2,3])([2,2,1])(CUBOID([3,7.5]))
#VIEW(p1)
p2 = T([1,2,3])([8.5,2,1])(CUBOID([3,7.5]))
p3 = T([1,2,3])([18.5,2,1])(CUBOID([3,7.5]))
p4 = T([1,2,3])([25,2,1])(CUBOID([3,7.5]))
sGreen = [0,2.55,1.27]
floor1=COLOR(sGreen)(STRUCT([p1,p2,p3,p4]))
#VIEW(floor1)


l2 = COLOR(GREEN)(CUBOID([27,8.5]))
floor2= T([1,2,3])([1.5,1.5,15])(l2)
#VIEW(floor2)
turq = [1.73,2.34,2.34]
l3 = COLOR(turq)(CUBOID([26,7.5]))
floor3= T([1,2,3])([2,2,21])(l3)
#VIEW(floor3)
model2D = (STRUCT([floor0,floor1,floor2, floor3]))
model2D = R([2,3])(PI/2)(model2D)

floor0 = R([2,3])(PI/2)(CUBOID([30,12,0]))
floor0= T (3)(-2)(floor0)
facciata = T(1)(2)(CUBOID([26,21]))
def disk2D(p): # point function
    u,v = p
    return [v*COS(u)*3.5, v*SIN(u)*3.5] # coordinate functions
domain2D = PROD([INTERVALS(2*PI)(32), INTERVALS(1)(3)]) # 2D domain decompos
cerchioArcoGrande=( MAP(disk2D)(domain2D))
cagTras = T([1,2])([15,8])(cerchioArcoGrande)
int = DIFFERENCE([facciata,cagTras])
#VIEW(int)

def disk2DP(p): # point function
    u,v = p
    return [v*COS(u)*1.75, v*SIN(u)*1.75] # coordinate functions
cerchioArchiPiccoli=( MAP(disk2DP)(domain2D))
cerchioSx = T([1,2])([6.75,7])(cerchioArchiPiccoli)
cerchioDx = T([1,2])([23.25,7])(cerchioArchiPiccoli)
int2 = DIFFERENCE([int,cerchioSx,cerchioDx])
#VIEW(int2)
rettSx= T(1)(5)(CUBOID([3.5,7]))
rettDx= T(1)(21.5)(CUBOID([3.5,7]))
rettCentro =T(1)(11.5) (CUBOID([7,8]))
south=(DIFFERENCE([int2,rettSx,rettDx,rettCentro]))

north = T(3)(7.5)(south)
frontali= STRUCT([south,north])
#VIEW(frontali)
west =R([1,3])(PI/2)(CUBOID([7.5,21]))
west = T(1)(2)(west)
lati3=(STRUCT([frontali, west]))
easth= T(1)(26)(west)
t = R([1,2])(PI)(STRUCT([frontali, west,easth,floor0]))
tt = T(1)(30)(t)
tutto= T(3)(2)(tt)
mock_up_3D=(STRUCT([model2D,tutto]))
VIEW(mock_up_3D)