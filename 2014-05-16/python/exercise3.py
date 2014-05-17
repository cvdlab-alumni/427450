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

DRAW = COMP([VIEW,STRUCT,MKPOLS])

#return number of cells
def cells (larModel):
   celle = []
   lunghezza = range(len(larModel[1]))
   for cell in lunghezza:
      celle.append(cell)
   return celle

#utility function for difference two array
def differenceCells (celle,cellevecchie):
	return set(celle) - set(cellevecchie)

#Create a number of cells if you want to create model starting only from points
def autoAssemblyDiagram(values):
	block = []
	for coordination in values:
		block.append(len(coordination))
	return assemblyDiagramInit(block)(values)

#elimination cells
def elimination(master, toRemove):
 return master[0],[cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

#numbering cells
def numbering(master):
 hpc = SKEL_1(STRUCT(MKPOLS(master)))
 numbering = cellNumbering(master,hpc)(range(len(master[1])),CYAN,2)
 return numbering

#method for multiple merging at the same time, passing an array
def multipleMerging(master,diagram,toMerge):
 cont=0
 for v in toMerge:
    master = diagram2cell(diagram[cont],master,v)
    ++cont
 return master

#method for merge and delete what you want
def mergingElimination(master, diagrams, toMerge, toRemove):
 master = multipleMerging(master, diagrams, toMerge )
 master = elimination( master, toRemove)
 return master

#method for merge and delete what you want after numbering all cells
#paramtric color and dimension for text (setting default to CYAN and 2)
def mergingNumberingElimination(master, diagrams, toMerge, toRemove, color=CYAN, scale=2):
 master = multipleMerging(master, diagrams, toMerge )
 master = elimination( master, toRemove)
 hpc = SKEL_1(STRUCT(MKPOLS(master)))
 hpc =  cellNumbering(master,hpc)(range(len(master[1])),color,scale)
 return hpc

def understandSkeleton(master):
	C,VC = master
	print 'Struttura \n'
	print 'Vertici :'
	for i in C:
		print i
	print 'Facciate :'
	for v in VC:
		print v
	print 'Numero vertici : %d' %(len(C)) 
	print 'Numero facciate : %d' %(len(VC)) 

	return

#example
c = assemblyDiagramInit([2,2,2])([[1,1],[1,1],[1,1]])
master = assemblyDiagramInit([2,2,2])([[2,2],[2,2],[2,2]])
master = mergingElimination(master, [c,c], [7,6], [10,11,14,12])

DRAW(master)

newmaster =  assemblyDiagramInit([2,2,2])([[2,2],[2,2],[2,2]])
newmaster = mergingNumberingElimination(newmaster, [c,c], [7,6], [10,11,14,12])

VIEW(newmaster)

understandSkeleton(master)


