from pyplasm import *

Colonna	  = CUBOID([2.6,3]);

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

facciataPrincipale = CUBOID([2.6,6,0.5])

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

mock_up_3D = Facciate
mock_up_3D	= R([2,3])(-PI/2)(mock_up_3D)

VIEW(mock_up_3D);
