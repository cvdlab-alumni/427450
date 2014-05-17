""" progressive refinement of a block diagram """
from pyplasm import *
from scipy import *
import os,sys
""" import modules from larcc/lib """
#CHANGE THE PATH
sys.path.insert(0, '/Users/cristianroselli/Desktop/lar-cc-master/lib/py')
from lar2psm import *
from simplexn import *
from larcc import *
from largrid import *
from mapper import *
from boolean import *
from sysml import *


def REDGREENBLUE(color):
	return [color[0]/255.0, color[1]/255.0, color[2]/255.0]

def extrude(obj,z):
	return PROD([obj, Q(z)])	

VERDE    = REDGREENBLUE([0,128,0])
GRIGIO   = REDGREENBLUE([220, 220,220])
BISCOTTO = REDGREENBLUE([255,228,196])	
TERRA    = REDGREENBLUE([117,102,63])
ROSSO    = REDGREENBLUE([123,27,2])


DRAW = COMP([VIEW,STRUCT,MKPOLS])
master = assemblyDiagramInit([13,9,2])([[.3,4,.3,2,.3,2,.3,1,.3,1,.3,2,.3],[.3,3,.3,2,.3,4,.3,2,.3],[.3,3]])
V,CV = master

toRemove = [23,21,25,29,33,57,61,65,69,99,101,93,97,105,129,
						133,137,141,165,169,173,177,201,205,59,111,183,
						103,123,159,115,151,155,47,31,67,51,49,209,227,
						229,228,208,226,211,210,214,215,213,212,230,231,
						233,232];
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]

toMerge = 24
diagram = assemblyDiagramInit([3,1,2])([[1.6,0.8,1.6],[.3],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
toRemove = [181]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

toMerge = 78
diagram = assemblyDiagramInit([3,1,2])([[1,0.1,0.8],[.3],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
toRemove = [187]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

toMerge = 133
diagram = assemblyDiagramInit([3,1,2])([[0.1,0.8,0.1],[.3],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
toRemove = [189]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

toMerge = 71
diagram = assemblyDiagramInit([1,3,2])([[0.3],[.6,0.8,.6],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
toRemove = [193]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

toMerge = 93
diagram = assemblyDiagramInit([1,3,2])([[0.3],[1.6,0.8,1.6],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
toRemove = [197]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

toMerge = 146
diagram = assemblyDiagramInit([1,3,2])([[0.3],[.6,0.8,.6],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
toRemove = [201]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

toMerge = 63
diagram = assemblyDiagramInit([1,3,2])([[0.3],[.6,0.8,.6],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
toRemove = [205]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

toMerge = 32
diagram = assemblyDiagramInit([1,3,2])([[0.3],[1.1,0.8,1.1],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
toRemove = [209]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

toMerge = 151
diagram = assemblyDiagramInit([1,3,2])([[0.3],[.6,0.8,.6],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
toRemove = [213]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

toMerge = 11
diagram = assemblyDiagramInit([1,3,3])([[0.3],[1,2,1],[.8,1.4,.5]])
master = diagram2cell(diagram,master,toMerge)
toRemove = [219]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

toMerge = 3
diagram = assemblyDiagramInit([1,3,3])([[0.3],[1,1,1],[.8,1.4,.5]])
master = diagram2cell(diagram,master,toMerge)
toRemove = [226]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

toMerge = 42
diagram = assemblyDiagramInit([3,1,3])([[0.5,1,0.5],[0.3],[.8,1.4,.5]])
master = diagram2cell(diagram,master,toMerge)
toRemove = [233]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

toMerge = 69
diagram = assemblyDiagramInit([3,1,3])([[0.5,1,0.5],[0.3],[.8,1.4,.5]])
master = diagram2cell(diagram,master,toMerge)
toRemove = [240]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

toMerge = 150
diagram = assemblyDiagramInit([3,1,3])([[0.5,1,0.5],[0.3],[.8,1.4,.5]])
master = diagram2cell(diagram,master,toMerge)
toRemove = [247]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

slave = larApply(t(2,2,0))(master)
slave = larApply(s(1,-1,1))(slave)

palazzo = assemblyDiagramInit([1,2,4])([[10],[5,5],[1.5,1.5,1.5,1.5]])
palazzo = diagram2cell(master,palazzo,0)
palazzo = diagram2cell(master,palazzo,0)
palazzo = diagram2cell(master,palazzo,0)
palazzo = diagram2cell(master,palazzo,0)

palazzo = diagram2cell(slave,palazzo,0)
palazzo = diagram2cell(slave,palazzo,0)
palazzo = diagram2cell(slave,palazzo,0)
palazzo = diagram2cell(slave,palazzo,0)

pavimento = STRUCT([COLOR(GRIGIO)(CUBOID([20,20,0.2]))])
pavimento = T(3)(-0.2)(pavimento)
pavimento = T(1)(-5)(pavimento)
pavimento = T(2)(-5)(pavimento)

# tetto = STRUCT([COLOR(RED)(CUBOID([10,10,0.1]))])
# tetto = T(3)(6)(tetto)

def lampione():
	lampione = CYLINDER([0.05,2.0])(20)
	lampada = SPHERE(0.2)([20,30])
	lampada = COLOR(YELLOW)(lampada)
	lampada = T(3)(2)(lampada)
	lampione = STRUCT([lampione,lampada])
	return lampione

lampione1 = lampione()
lampione1 = T(1)(-.5)(lampione1)
lampione1 = T(2)(-.5)(lampione1)

lampione2 = lampione()
lampione2 = T(1)(10.5)(lampione2)
lampione2 = T(2)(-.5)(lampione2)

lampione3 = lampione()
lampione3 = T(1)(10.5)(lampione3)
lampione3 = T(2)(10.5)(lampione3)

lampione4 = lampione()
lampione4 = T(1)(-.5)(lampione4)
lampione4 = T(2)(10.5)(lampione4)

palazzo = STRUCT(MKPOLS((palazzo)))
palazzo = COLOR(BISCOTTO)(palazzo)
dom = (PROD([INTERVALS(1)(30),INTERVALS(1)(30)]))

controls3 = [[0.05, -0.01], [0.53, 0.8], [0.79, 1.4], [0.08, 2.5]]
bezier3 = BEZIER(S1)(controls3)
controls4 = [[0.92, 0.03], [1.45, 0.88], [1.49, 1.43], [1.04, 2.48]]
bezier4 = BEZIER(S1)(controls4)

vaso = MAP( BEZIER(S2)([bezier3,bezier4]))(dom)

aiuola = extrude(vaso, .2)
aiuola = SCALE([1,2])([1.25,1.25])(aiuola)
aiuola = T(1)(11.15)(aiuola)
aiuola = T(2)(.2)(aiuola)
aiuola = T(3)(.5)(aiuola)
aiuola = COLOR(VERDE)(aiuola)
vaso = SCALE([1,2])([1.4,1.4])(vaso)
vaso = T(1)(11)(vaso)
vaso = extrude(vaso, .5)
vaso = STRUCT([vaso, aiuola])
vaso2 = T(2)(6.5)(vaso)

ingresso = CUBOID([.3,5.3, 6])
ingresso = T(1)(9.7)(ingresso)
ingresso = T(2)(2.35)(ingresso)
ingresso = COLOR(BISCOTTO)(ingresso)

finestra  = CUBOID([.3,1,0.6])
finestra  = T(1)(9.7)(finestra)
finestra  = T(2)(2.5)(finestra)
finestra  = T(3)(1.5)(finestra)
finestra2 = CUBOID([.3,1,0.6])
finestra2 = T(1)(9.7)(finestra2)
finestra2 = T(2)(6.5)(finestra2)
finestra2 = T(3)(1.5)(finestra2)

finestra3  = CUBOID([.3,1,0.6])
finestra3  = T(1)(9.7)(finestra3)
finestra3  = T(2)(2.5)(finestra3)
finestra3  = T(3)(3.5)(finestra3)
finestra4  = CUBOID([.3,1,0.6])
finestra4  = T(1)(9.7)(finestra4)
finestra4  = T(2)(6.5)(finestra4)
finestra4  = T(3)(3.5)(finestra4)

finestra5  = CUBOID([.3,1,0.6])
finestra5  = T(1)(9.7)(finestra5)
finestra5  = T(2)(2.5)(finestra5)
finestra5  = T(3)(5)(finestra5)
finestra6  = CUBOID([.3,1,0.6])
finestra6  = T(1)(9.7)(finestra6)
finestra6  = T(2)(6.5)(finestra6)
finestra6  = T(3)(5)(finestra6)

portone  = CUBOID([.3,1,1.3])
portone = T(1)(9.7)(portone)
portone = T(2)(4.5)(portone)
ingresso = DIFFERENCE([ingresso, portone, finestra, finestra2, finestra3, finestra4, finestra5, finestra6])

pianerottolo = CUBOID([1.5,5.3,.2])
pianerottolo = T(1)(8.3)(pianerottolo)
pianerottolo = T(2)(2.35)(pianerottolo)
pianerottolo = T(3)(1.5)(pianerottolo)
pianerottolo  = COLOR(BISCOTTO)(ingresso)

pianerottolo2 = CUBOID([1.5,5.3, .2])
pianerottolo2 = T(1)(8.3)(pianerottolo2)
pianerottolo2 = T(2)(2.35)(pianerottolo2)
pianerottolo2 = T(3)(3)(pianerottolo2)
pianerottolo2 = COLOR(BISCOTTO)(pianerottolo2)

pianerottolo3 = CUBOID([1.5,5.3, .2])
pianerottolo3 = T(1)(8.3)(pianerottolo3)
pianerottolo3 = T(2)(2.35)(pianerottolo3)
pianerottolo3 = T(3)(4.5)(pianerottolo3)
pianerottolo3 = COLOR(BISCOTTO)(pianerottolo3)

stradina = CUBOID([5,1])
stradina = T(1)(10)(stradina)
stradina = T(2)(4.5)(stradina)
stradina = COLOR(TERRA)(stradina)

prato = CUBOID([5,3])
prato = T(1)(2.5)(prato)
prato = T(2)(-4.5)(prato)
prato = COLOR(VERDE)(prato)

prato2 = CUBOID([5,3])
prato2 = T(1)(2.5)(prato2)
prato2 = T(2)(11.5)(prato2)
prato2 = COLOR(VERDE)(prato2)

terrazzo = CUBOID([10,10,.1])
terrazzo = T(3)(6)(terrazzo)
terrazzo  = COLOR(ROSSO)(terrazzo)

VIEW(STRUCT([pavimento, palazzo,lampione1,lampione2,lampione3,lampione4, 
						 vaso, vaso2, ingresso, pianerottolo, pianerottolo2, pianerottolo3, stradina, prato, prato2, terrazzo]))

