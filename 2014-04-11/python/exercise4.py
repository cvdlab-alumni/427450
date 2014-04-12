
from pyplasm import *


def extrude(obj,z):
	return PROD([obj, Q(z)])	

def REDGREENBLUE(color):
	return [color[0]/255.0, color[1]/255.0, color[2]/255.0]

TERRA    = REDGREENBLUE([117,102,63])
VERDE    = REDGREENBLUE([0,128,0])
CELESTE  = REDGREENBLUE([153,203,255])
CASTAGNO = REDGREENBLUE([205,	92,	92]) 
GRIGIO   = REDGREENBLUE([220, 220,220])
TRONCO   = REDGREENBLUE([169,131,7])	 
BISCOTTO = REDGREENBLUE([255,228,196])	

OttagonoEsternoMura  = CIRCLE(5.5)([8,1]);
OttagonoEsterno      = CIRCLE(4.8)([8,1]);
OttagonoEsterno      = DIFFERENCE([OttagonoEsternoMura, OttagonoEsterno])

OttagonoInternoMura  = CIRCLE(3.0)([8,1]);
OttagonoInterno      = CIRCLE(2.2)([8,1]);
OttagonoInterno      = DIFFERENCE([OttagonoInternoMura, OttagonoInterno])

OttagonoLaterale = CIRCLE(1)([8,1]);
Vicolo					 = CUBOID([0.2,1.9]);

OttagonoLateral1 = T(1)(5.9)(OttagonoLaterale)
Vicol1					 = R([1,2])(PI/2)(Vicolo)
Vicol1					 = T(1)(4.8)(Vicol1)
Vicol1					 = T(2)(-0.1)(Vicol1)

OttagonoLateral2 = T(1)(4.1)(OttagonoLaterale)
OttagonoLateral2 = T(2)(4.2)(OttagonoLateral2)
Vicol2					 = R([1,2])(3*PI/4)(Vicolo)
Vicol2					 = T(1)(3.45)(Vicol2)
Vicol2					 = T(2)(3.35)(Vicol2)

OttagonoLateral3 = T(2)(5.9)(OttagonoLaterale)
Vicol3					 = T(2)(2.9)(Vicolo)
Vicol3					 = T(1)(-0.1)(Vicol3)

OttagonoLateral4 = T(1)(-4.2)(OttagonoLaterale)
OttagonoLateral4 = T(2)(4.2)(OttagonoLateral4)
Vicol4					 = R([1,2])(-3*PI/4)(Vicolo)
Vicol4					 = T(1)(-3.35)(Vicol4)
Vicol4					 = T(2)(3.45)(Vicol4)

OttagonoLateral5 = T(1)(-5.9)(OttagonoLaterale)
Vicol5					 = R([1,2])(-PI/2)(Vicolo)
Vicol5					 = T(1)(-4.8)(Vicol5)
Vicol5					 = T(2)(0.1)(Vicol5)

OttagonoLateral6 = T(1)(-4.1)(OttagonoLaterale)
OttagonoLateral6 = T(2)(-4.2)(OttagonoLateral6)
Vicol6					 = R([1,2])(-PI/4)(Vicolo)
Vicol6					 = T(1)(-3.45)(Vicol6)
Vicol6					 = T(2)(-3.35)(Vicol6)

OttagonoLateral7 = T(2)(-5.9)(OttagonoLaterale)
Vicol7					 = T(2)(-4.8)(Vicolo)
Vicol7					 = T(1)(-0.1)(Vicol7)

OttagonoLateral8 = T(1)(4.1)(OttagonoLaterale)
OttagonoLateral8 = T(2)(-4.2)(OttagonoLateral8)
Vicol8					 = R([1,2])(PI/4)(Vicolo)
Vicol8					 = T(1)(3.35)(Vicol8)
Vicol8					 = T(2)(-3.45)(Vicol8)

Porta					   = CUBOID([0.7,0.78]);
Port1						 = R([1,2])(-PI/8)(Porta)
Port1					   = T(2)(2.0)(Port1)
Port1					   = T(1)(0.44)(Port1)

Port2						 = R([1,2])(PI/8)(Porta)
Port2						 = R([1,2])(PI/2)(Port2)
Port2					   = T(1)(-1.74)(Port2)
Port2					   = T(2)(-1.1)(Port2)

Port3						 = R([1,2])(PI/8)(Porta)
Port3					   = T(1)(0.77)(Port3)
Port3					   = T(2)(-2.7)(Port3)

Frontone				 	   	= CUBOID([0.6,1.8]);
Frontone				     	= R([1,2])(-PI/8)(Frontone)
Frontone				     	= T(2)(1.2)(Frontone)
Frontone				     	= T(1)(-5.2)(Frontone)
Porte	               	= STRUCT([Port1, Port2, Port3])
OttagonoInternoTetto 	= OttagonoInterno
OttagonoInternoIntero = OttagonoInterno
OttagonoInterno       = DIFFERENCE([OttagonoInterno, Porte]) 
Ottagoni              = STRUCT([OttagonoEsterno, OttagonoInterno])
OttagoniLaterali      = STRUCT([OttagonoLateral1, OttagonoLateral2, OttagonoLateral3, OttagonoLateral4,
													     OttagonoLateral5, OttagonoLateral6, OttagonoLateral7, OttagonoLateral8 
													    ])
Vicoli 	= STRUCT([Vicol1, Vicol2, Vicol3, Vicol4, Vicol5, Vicol6, Vicol7, Vicol8]);

OttagonoLateraleG = CIRCLE(1.1)([8,1]);
OttagonoLateralG1 = T(1)(5.9)(OttagonoLateraleG)
OttagonoLateralG2 = T(1)(4.1)(OttagonoLateraleG)
OttagonoLateralG2 = T(2)(4.2)(OttagonoLateralG2)
OttagonoLateralG3 = T(2)(5.9)(OttagonoLateraleG)
OttagonoLateralG4 = T(1)(-4.2)(OttagonoLateraleG)
OttagonoLateralG4 = T(2)(4.2)(OttagonoLateralG4)
OttagonoLateralG5 = T(1)(-5.9)(OttagonoLateraleG)
OttagonoLateralG6 = T(1)(-4.1)(OttagonoLateraleG)
OttagonoLateralG6 = T(2)(-4.2)(OttagonoLateralG6)
OttagonoLateralG7 = T(2)(-5.9)(OttagonoLateraleG)
OttagonoLateralG8 = T(1)(4.1)(OttagonoLateraleG)
OttagonoLateralG8 = T(2)(-4.2)(OttagonoLateralG8)
OttagoniLateraliG = STRUCT([OttagonoLateralG1, OttagonoLateralG2, OttagonoLateralG3, OttagonoLateralG4,
													  OttagonoLateralG5, OttagonoLateralG6, OttagonoLateralG7, OttagonoLateralG8 ])
OttagonoInternoMura2  = CIRCLE(5.0)([8,1]);
OttagonoInternoTetto2 = CIRCLE(2.2)([8,1]);
OttagonoInternoTetto2 = DIFFERENCE([OttagonoInternoMura2, OttagonoInternoTetto2])
OttagonoEsternoMura1  = CIRCLE(5.7)([8,1]);
OttagonoEsternoMura1	= DIFFERENCE([OttagonoEsternoMura1, OttagonoInternoTetto2])
OttagonoEsternoMura1	= DIFFERENCE([CIRCLE(5.8)([8,1]),OttagonoEsternoMura1 ]);

Vicoli                 = extrude(Vicoli, 5.9)
OttagonoInternoIntero1 = extrude(OttagonoInternoIntero, 2.9)					

floor1  = STRUCT([OttagonoEsternoMura1, OttagoniLateraliG, Frontone, OttagonoInternoIntero1])
floor1	= T(3)(3)(floor1) 					
floor1	= COLOR(RED)(floor1)

Ingresso	= CUBOID([0.6,3]);
Ingresso	= R([1,2])(-PI/8)(Ingresso)
Ingresso	= T(2)(0.8)(Ingresso)
Ingresso	= T(1)(-5.5)(Ingresso)
Ingress2	= CUBOID([0.8,1]);
Ingress2	= R([1,2])(-PI/8)(Ingress2)
Ingress2	= T(2)(1.78)(Ingress2)
Ingress2	= T(1)(-5.5)(Ingress2)
Ingress3	= CUBOID([1.2,0.6]);
Ingress3	= R([1,2])(-PI/8)(Ingress3)
Ingress3	= T(2)(1.84)(Ingress3)
Ingress3	= T(1)(-5.2)(Ingress3)
Ingresso	 = DIFFERENCE([Ingresso,Ingress2])
OttagoniF0 = DIFFERENCE([Ottagoni,Ingress3]) 


OttagonoInterno        = extrude(OttagonoInterno, 1.5)
OttagonoInternoIntero  = extrude(OttagonoInternoIntero, 1.5)
OttagonoInternoIntero0 = T(3)(1.5)(OttagonoInternoIntero) 					



Colonna	  = CUBOID([3.4,3]);

def extrude(obj,z):
	return PROD([obj, Q(z)])

Finestra  = CIRCLE(0.1)([30,1]);
Finestra1	= CUBOID([0.2,0.4]);
Finestra1	= T(1)(-0.1)(Finestra1)
Finestra1	= STRUCT([Finestra,Finestra1])
Finestra1	= T(1)(1.3)(Finestra1)
Finestra1	= T(2)(1.1)(Finestra1)
Finestra2	= CUBOID([0.2,0.4]);
Finestra2	= T(1)(-0.1)(Finestra2)
Finestra2	= STRUCT([Finestra,Finestra2])
Finestra2	= T(1)(1.3)(Finestra2)
Finestra2	= T(2)(1.7)(Finestra2)

Facciata 	= DIFFERENCE([Colonna, Finestra1])
Facciata  = extrude(Facciata, 0.5)

Facciata1	= R([1,3])(PI/8)(Facciata)
Facciata1 = T(3)(-5.2)(Facciata1)
Facciata1	= T(1)(0.73)(Facciata1)
Facciata1	= T(2)(-3)(Facciata1)

FacciataG 	= DIFFERENCE([Colonna, Finestra2])
FacciataG  = extrude(FacciataG, 0.5)

Facciata1G	= R([1,3])(PI/8)(FacciataG)
Facciata1G  = T(3)(-5.2)(Facciata1G)
Facciata1G	= T(1)(0.73)(Facciata1G)
Facciata1G	= T(2)(-6)(Facciata1G)

north  = STRUCT([Facciata1, Facciata1G])


Facciata8	  = T(3)(9.4)(Facciata1)
Facciata8	  = T(1)(-3.9)(Facciata8)
Facciata8G	= T(3)(9.4)(Facciata1G)
Facciata8G	= T(1)(-3.9)(Facciata8G)
south       = STRUCT([Facciata8, Facciata8G])
south       = R([1,3])(PI)(south)
south				= T(3)(9.4)(south)
south				= T(1)(-3.9)(south)

Facciata3  = T(3)(5.1)(Facciata)
Facciata3  = T(1)(-1.3)(Facciata3)
Facciata3	 = R([1,3])(7*PI/8)(Facciata3)
Facciata3	 = T(2)(-3)(Facciata3)
Facciata3G = T(3)(5.1)(FacciataG)
Facciata3G = T(1)(-1.3)(Facciata3G)
Facciata3G = R([1,3])(7*PI/8)(Facciata3G)
Facciata3G = T(2)(-6)(Facciata3G)

nord_west  = STRUCT([Facciata3, Facciata3G]) 
nord_west   = R([1,3])(PI)(nord_west)
nord_west	  = T(3)(-9.4)(nord_west)
nord_west	  = T(1)(-3.9)(nord_west)


Facciata6	  = T(3)(9.4)(Facciata3)
Facciata6	  = T(1)(3.9)(Facciata6)
Facciata6G	= T(3)(9.4)(Facciata3G)
Facciata6G	= T(1)(3.9)(Facciata6G)
nord_east = STRUCT([Facciata6, Facciata6G])

Facciata4  = R([1,3])(5*PI/8)(Facciata)
Facciata4	 = T(3)(0.7)(Facciata4)
Facciata4	 = T(1)(5.2)(Facciata4)
Facciata4  = T(2)(-3)(Facciata4)
Facciata4G = R([1,3])(5*PI/8)(FacciataG)
Facciata4G = T(3)(0.7)(Facciata4G)
Facciata4G = T(1)(5.2)(Facciata4G)
Facciata4G = T(2)(-6)(Facciata4G)

east = STRUCT([Facciata4, Facciata4G])

Facciata5	 = T(1)(-9.4)(Facciata4)
Facciata5  = T(3)(-3.9)(Facciata5)
Facciata5G = T(1)(-9.4)(Facciata4G)
Facciata5G = T(3)(-3.9)(Facciata5G)

west = STRUCT([Facciata5, Facciata5G])
west   = R([1,3])(PI)(west)
west	 = T(1)(-9.4)(west)
west   = T(3)(-3.9)(west)

Facciata7  = R([1,3])(3*PI/8)(Facciata)
Facciata7	 = T(3)(-3.2)(Facciata7)
Facciata7	 = T(1)(4.2)(Facciata7)
Facciata7  = T(2)(-3)(Facciata7)
Facciata7G = R([1,3])(3*PI/8)(FacciataG)
Facciata7G = T(3)(-3.2)(Facciata7G)
Facciata7G = T(1)(4.2)(Facciata7G)
Facciata7G = T(2)(-6)(Facciata7G)

sud_east  = STRUCT([Facciata7, Facciata7G])

facciataPrincipale = CUBOID([3,6,0.5])

Laterali  = CIRCLE(0.1)([30,1]);
Laterali1	= CUBOID([0.2,5.5]);
Laterali1	= T(1)(-0.1)(Laterali1)
Laterali1	= STRUCT([Laterali,Laterali1])
Laterali2	= STRUCT([Laterali,Laterali1])
Laterali2 = T(1)(0.3)(Laterali2)
Laterali2 = T(2)(0.5)(Laterali2)
Laterali1	= T(1)(2.3)(Laterali1)
Laterali1	= T(2)(0.5)(Laterali1)
Laterali1 = extrude(Laterali1, 0.3)
Laterali2 = extrude(Laterali2, 0.3)

porta   = CIRCLE(0.5)([30,1]);
porta1	= CUBOID([1,1.7]);
porta1	= T(1)(-0.5)(porta1)
porta	  = STRUCT([porta,porta1])
porta	  = T(1)(1.3)(porta)
porta	  = T(2)(4.5)(porta)
porta   = extrude(porta, 0.3)

portaInterno	 = CUBOID([0.8,1.5, 1]);
portaInterno	 = T(1)(-0.5)(portaInterno)
portaInterno	 = T(1)(1.4)(portaInterno)
portaInterno	 = T(2)(4.5)(portaInterno)

Finestrella   = CIRCLE(0.2)([30,1]);
Finestrella1	= CUBOID([0.4,0.5]);
Finestrella1	= T(1)(-0.2)(Finestrella1)
Finestrella1	= STRUCT([Finestrella,Finestrella1])
Finestrella1	= T(1)(1.3)(Finestrella1)
Finestrella1	= T(2)(1.7)(Finestrella1)
Finestrella1  = extrude(Finestrella1, 0.5)

frontone	= CUBOID([1.8,0.8,0.5]);
frontone	= T(1)(0.4)(frontone)
frontone	= T(2)(2.2)(frontone)
frontone	= T(3)(-0.2)(frontone)

triangolo = MKPOL([ [[0,0],[0.9,0.7],[1.8,0]],[[1,2,3]], None ])
triangolo = extrude(triangolo, 0.3)
triangolo	= T(3)(-0.2)(triangolo)
triangolo = R([1,2])(PI)(triangolo)
triangolo	= T(1)(2.2)(triangolo)
triangolo	= T(2)(3)(triangolo)

frontone = DIFFERENCE([frontone, triangolo])

facciataPrincipale = DIFFERENCE([facciataPrincipale, Laterali1, Laterali2, porta, Finestrella1, portaInterno])
facciataPrincipale = STRUCT([facciataPrincipale, frontone])

principal  = R([1,3])(3*PI/8)(facciataPrincipale)
principal	 = T(3)(-3.2)(principal)
principal	 = T(1)(4.2)(principal)
principal	 = T(2)(-3)(principal)
principal  = T(2)(-3)(principal)
principal  = R([1,3])(PI)(principal)

Facciate = STRUCT([north, east, south, nord_west, nord_east, west, sud_east, principal])

Facciate = Facciate
Facciate	= R([2,3])(-PI/2)(Facciate)

floor0    = STRUCT([OttagoniF0, OttagoniLaterali, Vicoli, Ingresso, OttagonoInterno, OttagonoInternoIntero0, Facciate])

floor2    = STRUCT([OttagonoInternoTetto2])
floor2		= T(3)(6)(floor2) 					
floor2		= COLOR(BROWN)(floor2)

floor21 = EXTRUDE([1,OttagoniLaterali,7])


prato    = COLOR(VERDE)(CUBOID([110,110]))
prato    = T(1)(-55)(prato)
prato    = T(2)(-55)(prato)
prato    = T(3)(-0.1)(prato)
piazzaleG = COLOR(TERRA)(CIRCLE(25)([25,1]));
piazzale = COLOR(BISCOTTO)(CIRCLE(10)([25,1]));

casale  = CUBOID([5,10,3])
casale  = T(2)(26)(casale)
casale2 = CUBOID([5.3,8,2])
casale2 = T(2)(27)(casale2)
casale2 = T(1)(-3.5)(casale2)
casale  = STRUCT([casale, casale2])
casale  = R([1,2])(PI/8)(casale)
casale  = COLOR(GRIGIO)(casale) 


casale3  = CUBOID([2,10,3])
casale4  = CUBOID([2.8,8,3])
casale5  = CUBOID([3.6,6,3])
casale4  = T(2)(2)(casale4)
casale5  = T(2)(4)(casale5)
casale45 = STRUCT([casale4,casale5]) 
casale2  = STRUCT([casale3, casale45])
casale2  = T(2)(29)(casale2)
casale2  = T(1)(-18)(casale2)
casale2  = R([1,2])(PI/8)(casale2)
casale2  = COLOR(CASTAGNO)(casale2) 

casale3 = CUBOID([4,5,3])
casale3 = T(2)(12)(casale3)
casale3 = T(1)(-16)(casale3)
casale3 = COLOR(CELESTE)(casale3)

def albero():
	albero = CYLINDER([0.2,3.0])(20)
	alberochioma = SPHERE(1)([20,8])
	albero = COLOR(TRONCO)(albero)
	alberochioma = COLOR(VERDE)(alberochioma)
	alberochioma = T(3)(2.3)(alberochioma)
	albero = STRUCT([albero,alberochioma])
	return albero

def cespuglio():
	cespuglio = SPHERE(0.3)([20,8])
	cespuglio = COLOR(VERDE)(cespuglio)
	return cespuglio


cespugli = T([1,2,3])([-23,38,0.5])(cespuglio())
cespugli = [T(1)(4.4), cespugli]
Cespugli = STRUCT( NN(7)(cespugli))

Cespugli2 = STRUCT( NN(7)(cespugli))
Cespugli2 = T([1,2])([10,-80])(Cespugli2)

alberello = T(1)(23)(albero())
alberi = [T(1)(4.4), alberello]
Albero = STRUCT( NN(6)(alberi) )
Albero = [T(2)(5), Albero]

AlberoSu = STRUCT( NN(5)(Albero) )
Albero   = STRUCT( NN(10)(Albero) )
Albero1  = T(2)(-50)(Albero)

Albero2 = T(2)(-50)(AlberoSu)
Albero2 = T(1)(-26)(Albero2)
Albero3 = T(1)(-26)(Albero2)

Albero4 = T(1)(-26)(AlberoSu)
Albero4 = T(2)(25)(Albero4)


Nuvola  = SPHERE(0.3)([20,15])
Nuvola1 = SPHERE(0.5)([20,15])
Nuvola2 = SPHERE(0.7)([20,15])
Nuvola1 = T(1)(-0.3)(Nuvola1)
Nuvola1 = T(3)(-0.3)(Nuvola1)
Nuvola2 = T([1,3])([0.7,-0.4])(Nuvola2)

Nuvola = STRUCT([Nuvola,Nuvola1,Nuvola2])
Nuvola =  T(3)(10)(Nuvola)
Nuvola = SCALE([1,2,3])([10,14,6])(Nuvola)
Nuvola = T([1,2])([12,20])(Nuvola)

Nuvola0 = SPHERE(0.5)([20,15])
Nuvola1 = SPHERE(0.7)([20,15])
Nuvola3 = SPHERE(0.4)([20,15])
Nuvola2 = SPHERE(1)([20,15])
Nuvola1 = T(1)(-0.3)(Nuvola1)
Nuvola1 = T(3)(-0.3)(Nuvola1)
Nuvola2 = T([1,3])([0.7,-0.4])(Nuvola2)
Nuvola3 = T([1,3])([1.2,-0.5])(Nuvola3)

Nuvola0 = SCALE([1,2,3])([1.4,2,1])(Nuvola)
Nuvola0 = T([1,2])([-10,-18])(Nuvola0)

building  = STRUCT([ floor0,floor1,floor2, 
										 prato, floor21, piazzale, piazzaleG, 
										 casale, casale2, casale3, 
										 Albero, Albero1, Albero2, Albero3,Albero4, 
										 Cespugli, Cespugli2,
										 Nuvola, Nuvola0 ])
VIEW(building)


# strada = CUBOID([1.1,20])
# strada = R([1,2])(PI/2)(strada)

# strada2 = CUBOID([1.1,18])
# strada2 = R([1,2])(PI/2)(strada2)
# strada2 = T(2)(10)(strada2)
# strada2 = T(1)(13)(strada2)

# strada3 = CUBOID([1.1,21])
# strada3 = T(2)(-11)(strada3)
# strada3 = T(1)(12)(strada3)

# strada4 = CUBOID([1.1,22])
# strada4 = R([1,2])(PI/2)(strada4)
# strada4 = T(2)(-11)(strada4)
# strada4 = T(1)(13)(strada4)

# strada5 = CUBOID([1,22])

