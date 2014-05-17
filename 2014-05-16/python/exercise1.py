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
master = assemblyDiagramInit([13,9,2])([[.3,4,.3,2,.3,2,.3,1,.3,1,.3,2,.3],[.3,3,.3,2,.3,4,.3,2,.3],[.3,3]])
V,CV = master

toRemove = [23,21,25,29,33,57,61,65,69,99,101,93,97,105,129,133,137,141,
						165,169,173,177,201,205,59,111,183,103,123,159,115,151,155,
						47,31,67,51,49,209,227,229,228,208,226,211,210,214,215,213,212,230,231,233,232];
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
DRAW(master)
