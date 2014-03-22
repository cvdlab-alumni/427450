from pyplasm import *

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

Frontone				 	   = CUBOID([0.6,1.8]);
Frontone				     = R([1,2])(-PI/8)(Frontone)
Frontone				     = T(2)(1.2)(Frontone)
Frontone				     = T(1)(-5.2)(Frontone)
Porte	               = STRUCT([Port1, Port2, Port3])
OttagonoInternoTetto = OttagonoInterno
OttagonoInterno      = DIFFERENCE([OttagonoInterno, Porte]) 
Ottagoni             = STRUCT([OttagonoEsterno, OttagonoInterno])
OttagoniLaterali     = STRUCT([OttagonoLateral1, OttagonoLateral2, OttagonoLateral3, OttagonoLateral4,
													     OttagonoLateral5, OttagonoLateral6, OttagonoLateral7, OttagonoLateral8 
													    ])
Vicoli 	= STRUCT([Vicol1, Vicol2, Vicol3, Vicol4, Vicol5, Vicol6, Vicol7, Vicol8]);
floor1  = STRUCT([Ottagoni, OttagoniLaterali, Vicoli, Frontone])
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
floor0     = STRUCT([OttagoniF0, OttagoniLaterali, Vicoli, Ingresso])


floor2    = STRUCT([OttagonoInternoTetto])
floor2		= T(3)(6)(floor2) 					
floor2		= COLOR(GREEN)(floor2)
building  = STRUCT([floor0,floor1,floor2])

VIEW(building);