fireball = {
    positionStyle  : Type.SPHERE,
    positionBase   : new THREE.Vector3( 3.8, 6.4, -13.3 ),
    positionRadius : 0.1,
        
    velocityStyle : Type.SPHERE,
    speedBase     : 0.11,
    speedSpread   : 0.11,

    particleTexture : THREE.ImageUtils.loadTexture( 'images/smokeparticle.png' ),

    sizeTween    : new Twin( [0, 0.01], [0.8, 0.8] ),
    opacityTween : new Twin( [0.7, 1], [1, 0] ),
    colorBase    : new THREE.Vector3(0.02, 1, 0.4),
    blendStyle   : THREE.AdditiveBlending,  

    particlesPerSecond : 30,
    particleDeathAge   : 1.5,   
    emitterDeathAge    : 60
}

rain = {

    positionStyle    : Type.CUBE,
    positionBase     : new THREE.Vector3( 48.5, 10.4, -5 ),
    positionSpread   : new THREE.Vector3( 1, 0, 1 ),

    velocityStyle    : Type.CUBE,
    velocityBase     : new THREE.Vector3( 0, -7, 0 ),
    velocitySpread   : new THREE.Vector3( 5, 5, 5 ), 
    accelerationBase : new THREE.Vector3( 0, -5,0 ),
    
    particleTexture : THREE.ImageUtils.loadTexture( 'images/raindrop2flip.png' ),

    sizeBase    : 1,
    sizeSpread  : 1,
    colorBase   : new THREE.Vector3(0.66, 1.0, 0.7), // H,S,L
    colorSpread : new THREE.Vector3(0.00, 0.0, 0.2),
    opacityBase : 0.8,

    particlesPerSecond : 100,
    particleDeathAge   : 1.0,       
    emitterDeathAge    : 60
}