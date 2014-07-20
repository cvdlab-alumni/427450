function settingPointer(){
	
	 havePointerLock = 'pointerLockElement' in document || 'mozPointerLockElement' in document || 'webkitPointerLockElement' in document;

      if ( havePointerLock ) {
          element = document.body;
          var pointerlockchange = function ( event ) {
            if ( document.pointerLockElement === element || document.mozPointerLockElement === element || document.webkitPointerLockElement === element ) {
              $("#pointer").fadeIn(1000);
              pointerControls.enabled = true;
              pointerControls.isOnObject( false );
              ray.ray.origin.copy( pointerControls.getObject().position );
              ray.ray.origin.y -= 10;
              var intersections = ray.intersectObjects( objs );
              if ( intersections.length > 0 ) {
                var distance = intersections[ 0 ].distance;
                if ( distance > 0 && distance < 10 ) {
                  pointerControls.isOnObject( true );
                }
              }
              trackballControls.reset()
              camera.position.set(0,0,0)
              pointerControls.getObject().position = new THREE.Vector3( 10, 5, -10 );
            } else {
              $("#pointer").fadeOut(1000);
              camera.position.set(10,10,50);
              pointerControls.enabled = false;
            }
          }

        var pointerlockerror = function ( event ) {
          console.log('error')
        }
        document.addEventListener( 'pointerlockchange', pointerlockchange, false );
        document.addEventListener( 'mozpointerlockchange', pointerlockchange, false );
        document.addEventListener( 'webkitpointerlockchange', pointerlockchange, false );
        document.addEventListener( 'pointerlockerror', pointerlockerror, false );
        document.addEventListener( 'mozpointerlockerror', pointerlockerror, false );
        document.addEventListener( 'webkitpointerlockerror', pointerlockerror, false );
      }

}