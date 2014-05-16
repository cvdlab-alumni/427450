""" progressive refinement of a block diagram """
from pyplasm import *
from scipy import *
import os,sys
""" import modules from larcc/lib """
sys.path.insert(0, '/Users/cristianroselli/Desktop/lar-cc-master/lib/py')
from lar2psm import *
from simplexn import *
from larcc import *
from largrid import *
from mapper import *
from boolean import *

from sysml import *
DRAW = COMP([VIEW,STRUCT,MKPOLS])
																											 # "3"        "5.5"	
master = assemblyDiagramInit([13,9,2])([[.3,4,.3,2,.3,  2,.3,1,  .3,1,.3,2,.3],[.3,3,.3,2,.3,4,.3,2,.3],[.3,3]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
VIEW(hpc)

toRemove = [23,21,25,29,33,57,61,65,69,99,101,93,97,105,129,133,137,141,
						165,169,173,177,201,205,59,111,183,103,123,159,115,151,155,
						47,31,67,51,49,209,227,229,228,208,226,211,210,214,215,213,212,230,231,233,232];
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
VIEW(hpc)