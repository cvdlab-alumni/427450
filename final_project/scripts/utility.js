! function(){
	utility = {
		
		createMesh: function(geom, imageFile, repeat) {
      if (imageFile && repeat){
          var texture = THREE.ImageUtils.loadTexture("images/" + imageFile)
          var material = new THREE.MeshPhongMaterial({side: THREE.DoubleSide});
          texture.wrapS =  texture.wrapT = THREE.RepeatWrapping;
          texture.repeat.set(repeat[0],repeat[1])
          material.map = texture;
          material.castShadow = true;
      }else{
        var material = new THREE.MeshPhongMaterial( {color: 0xffffff} );
      }
      var mesh = new THREE.Mesh( geom, material );
      return mesh;
    },

		mkPlaneGeometry:function (side1, side2, positionX, positionY, positionZ, texture, repeat) {
      if(typeof texture == 'string'){
        var plane = this.createMesh(new THREE.PlaneGeometry(side1,side2), texture, repeat);
      }else if(typeof texture == 'object'){
        var geometry = new THREE.PlaneGeometry(side1,side2)
        var material = new THREE.MeshPhongMaterial( texture );
        var plane = new THREE.Mesh( geometry, material );
      }else{
        var geometry = new THREE.PlaneGeometry(side1,side2)
        var material = new THREE.MeshPhongMaterial( {color: texture, side: THREE.DoubleSide} );
        var plane = new THREE.Mesh( geometry, material );
      }
      plane.position.set(positionX,positionY,positionZ);
      plane.castShadow = true;
      plane.receiveShadow = true;
      plane.rotation.x = Math.PI/2;
      return plane;
    },

    mkDoor : function(side1, side2,side3, positionX, positionY, positionZ, texture, toIntersect){
    	var door = new THREE.Object3D();
    	
      var geometry = new THREE.BoxGeometry(side1,side2, side3, 1)
      var plane =  this.createMesh(geometry, texture, [1,1]);
      // plane.position.set(positionX,positionY,positionZ);
      // plane.rotation.y = Math.PI/2; 
    	door.add(plane)
      // var geometry = new THREE.RingGeometry( 0.3, 0.1, 32 );
			// var material = new  THREE.MeshPhongMaterial( {specular: 0xffffff, color: 0xADB2BD, shininess: 100, metal: true, side: THREE.DoubleSide })
			// var serratura = new THREE.Mesh( geometry, material );
			// serratura.rotation.y = Math.PI/2;
			// serratura.position.set(positionX+0.5,positionY-1.4,positionZ);
			// door.add(serratura);
			// var geometry = new THREE.CylinderGeometry(0.1,0.1,0.4,50,50)
			// var maniglia1 = new THREE.Mesh( geometry, material );
			// maniglia1.rotation.z = Math.PI/2;
			// maniglia1.position.set(positionX+0.55,positionY-1.4,positionZ);
			// door.add(maniglia1)
			// var geometry = new THREE.CylinderGeometry(0.1,0.1,1,50,50)
			// var maniglia2 = new THREE.Mesh( geometry, material );
			// maniglia2.position.set(positionX+0.65,positionY-0.9,positionZ);
			// door.add(maniglia2)
			// var geometry = new THREE.RingGeometry( 0.3, 0.1, 32 );
			// var serraturaR = new THREE.Mesh( geometry, material );
			// serraturaR.rotation.y = Math.PI/2;
			// serraturaR.position.set(positionX-0.5,positionY-1.4,positionZ);
			// door.add(serraturaR);
			// var geometry = new THREE.CylinderGeometry(0.1,0.1,0.4,50,50)
			// var maniglia1R = new THREE.Mesh( geometry, material );
			// maniglia1R.rotation.z = Math.PI/2;
			// maniglia1R.position.set(positionX-0.55,positionY-1.4,positionZ);
			// door.add(maniglia1R)
			// var geometry = new THREE.CylinderGeometry(0.1,0.1,1,50,50)
			// var maniglia2R = new THREE.Mesh( geometry, material );
			// maniglia2R.position.set(positionX-0.65,positionY-0.9,positionZ);
			// door.add(maniglia2R)
      door.position.set(positionX, positionZ, -positionY);
      door.rotation.y = Math.PI/2; 

      plane.open = false
      toIntersect.push(plane);
      plane.interact = function(){
        if(!this.open){
         this.rotation.x =  Math.PI/2;
         this.position.z += 1;
         this.position.y += 2; 
         this.open = true;
       }else{
         this.rotation.x =  0;
         this.position.z -= 1;
         this.position.y -= 2; 
        this.open = false;
       }
      }

      return door
    },

    mkWindows: function(width,height, positionX, positionY, positionZ, rotate, toIntersect){
      var finestra = new THREE.Object3D();
      var antaSx = this.createAnta(width, height, null,  toIntersect, true);
      finestra.add(antaSx);
      var antaDx = this.createAnta(width, height, null,  toIntersect, true);
      antaDx.position.x = width/2;
      finestra.add(antaDx);
      finestra.position.set(positionX,positionY,positionZ);
      finestra.rotation[rotate[0]] = Math.PI/2
      finestra.rotation[rotate[1]] = Math.PI/2
      return finestra;
    },

    mkWindow: function(width, height, positionX, positionY, positionZ, rotate, toIntersect){
      var finestra = new THREE.Object3D();
      var anta = this.createAnta(width*2, height, rotate, toIntersect);
      finestra.add(anta);
      finestra.position.set(positionX,positionY,positionZ);
      if(rotate && typeof rotate == 'object'){
        finestra.rotation[rotate[0]] = Math.PI/2
        finestra.rotation[rotate[1]] = - Math.PI/2
      }
      return finestra
    },

    pictureFrame: function( width, height){
      var rectShape = new THREE.Shape();
      rectShape.moveTo( 0,0 );
      rectShape.lineTo( width/2, 0 );
      rectShape.lineTo( width/2, height );
      rectShape.lineTo( 0,height );
      rectShape.lineTo( 0, 0 );
      var hole1 = new THREE.Path();
      hole1.moveTo(width/20,height/10);
      hole1.lineTo(9*width/20,height/10);
      hole1.lineTo(9*width/20,9*height/10);
      hole1.lineTo(width/20,9*height/10);
      hole1.lineTo(width/20,height/10);
      rectShape.holes.push(hole1);
      return rectShape;
    },

    createAnta: function(width, height, rotate, toIntersect, double){
      var anta = new THREE.Object3D();
      var options = {amount: 1,bevelEnabled: false};
      var shape = this.createMesh(new THREE.ExtrudeGeometry(this.pictureFrame(width, height), options));
      anta.add(shape);
      var vetroX = width*2/5;
      var vetroY = height*4/5;
      var vetroZ = .2;
      var geometry = new THREE.BoxGeometry( vetroX,vetroY,vetroZ );
      var material = new THREE.MeshLambertMaterial( {color: 0x87cefa, transparent: true, opacity: .5} );
      var vetro = new THREE.Mesh( geometry, material );
      vetro.position.set(vetroX/2+width/20,vetroY/2+height/10,vetroZ/2);
      anta.add( vetro );
      if(rotate){
        anta.rotation.x = Math.PI/2;
        anta.rotation.y = Math.PI/2;
        anta.rotation.z = Math.PI/2;
      }
      toIntersect.push(vetro)
      toIntersect.push(shape)
      vetro.close = true;
      shape.close = true;
      if(double){
        var evento = function(){
          if(!this.close){
           this.parent.rotation.y = 0
           this.close = true;
         }else{
          this.parent.rotation.y =  Math.PI/2
          this.close = false;
         }
        }
      }else{
         var evento = function(){
          if(!this.close){
           this.parent.rotation.y = Math.PI/2
           this.close = true;
         }else{
          this.parent.rotation.y = - Math.PI/2
          this.close = false;
         }
        }
      }
      vetro.interact = evento
      shape.interact = evento
      return anta ;
    },
    
    mkLamp: function(posx, posz, name , toIntersect){

      var lamp = new THREE.Object3D();
      var lampGeometry = new THREE.SphereGeometry(0.5,30,30);
      var lampMaterial = new THREE.MeshLambertMaterial( { color: 0xffffff , opacity: 0.3, transparent: true} );
      var sphere = new THREE.Mesh(lampGeometry,lampMaterial);
      var cupolaGeometry = new THREE.SphereGeometry( 0.8, 32, 16, 0, 2 * Math.PI, 0, Math.PI / 2 );
      var cupolaMaterial = new THREE.MeshPhongMaterial( { color: 0xADB2BD } );
      var cupola = new THREE.Mesh(cupolaGeometry,cupolaMaterial);
      cupolaMaterial.side = THREE.DoubleSide
      cupola.rotation.x = Math.PI/2
      
      var baseGeometry = new THREE.CylinderGeometry(0.07,0.07,2,50,50);
      var baseMaterial = new THREE.MeshPhongMaterial( { color: 0x000000 } );
      var base = new THREE.Mesh(baseGeometry,baseMaterial);
      baseMaterial.side = THREE.DoubleSide
      base.rotation.x = Math.PI/2
      base.position.z = 1.5  
      spotLight =  new THREE.PointLight( 0xF0DC82, 0, 20 );
      spotLight.castShadow = true;
      spotLight.target = lamp;
      sphere.relativeLight = spotLight;
      sphere.on = false
      lamp.position.set(posx, 14, posz);
      lamp.add(sphere)
      lamp.add(spotLight)
      lamp.add(cupola)
      lamp.add(base)
      lamp.name  = name;
      lamp.rotation.x = -Math.PI/2;
      toIntersect.push(sphere);
      sphere.interact = function(){
        if(!this.on){
         this.relativeLight.intensity = 1;
         this.on = true;
       }else{
        this.relativeLight.intensity = 0;
        this.on = false;
       }
      }

      return lamp
    },

    mkWall: function(side1,side2,texture,repeat,posX,posY,posZ){
      var plane = this.createMesh(new THREE.PlaneGeometry(side1,side2), texture, repeat);
      plane.rotation.x =  Math.PI/2;
      plane.position.set(posX+side1/2,posY,posZ+side2/2);
      plane.receiveShadow = true;
     return plane;
      },

    mkWallDoor: function(wall_sideX,wall_sideY,door_sideX,door_sideY,texture,wall_posX,wall_posY,wall_posZ,door_pos){
      var rectShape = new THREE.Shape();
      rectShape.moveTo( 0,0 );
        rectShape.lineTo( door_pos,0 );
        rectShape.lineTo( door_pos,door_sideY );
        rectShape.lineTo( door_pos+door_sideX,door_sideY );
        rectShape.lineTo( door_pos+door_sideX,0 );
        rectShape.lineTo( wall_sideX,0 );
        rectShape.lineTo( wall_sideX,wall_sideY );
        rectShape.lineTo( 0,wall_sideY );
        rectShape.lineTo( 0,0 );
        
      var plane = this.createMesh(new THREE.ShapeGeometry( rectShape ), texture, [5,5]);
      plane.rotation.x = Math.PI/2;

      plane.position.set(wall_posX,wall_posY,wall_posZ);
      plane.receiveShadow = true;
      return plane;
    },

    mkWallWindow: function(wall_sideX,wall_sideY,hole_sideX,hole_sideY,texture,repeat,wall_posX,wall_posY,wall_posZ,hole_posX,hole_posY){
      var rectShape = new THREE.Shape();
      rectShape.moveTo( 0,0 );
        rectShape.lineTo( wall_sideX,0 );
        rectShape.lineTo( wall_sideX,wall_sideY );
        rectShape.lineTo( 0,wall_sideY );
        rectShape.lineTo( 0,0 );

        var hole = new THREE.Path();
      hole.moveTo(hole_posX,hole_posY);
      hole.lineTo(hole_posX+hole_sideX,hole_posY);
      hole.lineTo(hole_posX+hole_sideX,hole_posY+hole_sideY);
      hole.lineTo(hole_posX,hole_posY+hole_sideY);
      hole.lineTo(hole_posX,hole_posY);
      rectShape.holes.push(hole);
        

      var plane = this.createMesh(new THREE.ShapeGeometry( rectShape ), texture, repeat);
      plane.rotation.x = Math.PI/2;

      plane.position.set(wall_posX,wall_posY,wall_posZ);
      plane.receiveShadow = true;
      plane.castShadow = true;

      return plane;
    },

    mkWallWindowDoor : function(wall_sideX,wall_sideY,hole_sideX,hole_sideY,door_sideX,door_sideY,texture,wall_posX,wall_posY,wall_posZ,hole_posX,hole_posY,door_pos){
      var rectShape = new THREE.Shape();
      rectShape.moveTo( 0,0 );
      rectShape.lineTo( door_pos,0 );
      rectShape.lineTo( door_pos,door_sideY );
      rectShape.lineTo( door_pos+door_sideX,door_sideY );
      rectShape.lineTo( door_pos+door_sideX,0 );
      rectShape.lineTo( wall_sideX,0 );
      rectShape.lineTo( wall_sideX,wall_sideY );
      rectShape.lineTo( 0,wall_sideY );
      rectShape.lineTo( 0,0 );

      var hole = new THREE.Path();
      hole.moveTo(hole_posX,hole_posY);
      hole.lineTo(hole_posX+hole_sideX,hole_posY);
      hole.lineTo(hole_posX+hole_sideX,hole_posY+hole_sideY);
      hole.lineTo(hole_posX,hole_posY+hole_sideY);
      hole.lineTo(hole_posX,hole_posY);
      rectShape.holes.push(hole);
      

      var plane = createMesh(new THREE.ShapeGeometry( rectShape ), texture, [5,5]);
      plane.rotation.x = Math.PI/2;

      plane.position.set(wall_posX,wall_posY,wall_posZ);
      plane.receiveShadow = true;
      plane.castShadow = true;


      return plane;
    },

    mkWalls: function(){
          //carta da parati
          var heigh_floor = 1.53;
          var heigh_wall = 15;
          var walls = new THREE.Object3D();        
          //cucina
          var  kitchen = new THREE.Object3D();
          walls.add(kitchen);
          var textureKitchen = "CucinaPattern.jpg"; 
          //parete finestra_forno
          var par1 = this.mkWallWindow(26.4,heigh_wall,4.8,7.8,textureKitchen,[2,2],1.6,1.55,heigh_floor,5,4.4);
          par1.rotation.y = Math.PI/2;
         // par1.rotation.x = - Math.PI/2;

          kitchen.add(par1);
          //parete2 lavabo
          var par2 = this.mkWall(20,heigh_wall,textureKitchen,[5,5],1.55,1.55,heigh_floor);
          par2.rotation.y = Math.PI;
          kitchen.add(par2);
          //parete3 porta corridoio
          var par3 = this.mkWallDoor(26.4,heigh_wall,4,11.5,textureKitchen,21.4,28,heigh_floor,17);
          par3.rotation.y = -Math.PI/2;
          kitchen.add(par3);
           //parete4 salone
          var par4 = this.mkWallDoor(20,heigh_wall,4,12,textureKitchen,1.55,27.9,heigh_floor,8);
          kitchen.add(par4);
   
          var corridoioKitchen = new THREE.Object3D();
          walls.add(corridoioKitchen); 
          var textureCorridoio = "StanzinoECorridoio.jpg"; 

          //parete porta kitchen
          var par1 = this.mkWallDoor(26.4,heigh_wall,4,12,textureCorridoio,23.05,1.55,heigh_floor,5.4);
          par1.rotation.y = Math.PI/2;
          corridoioKitchen.add(par1);
          //parete without anything
          var par2 = this.mkWall(10,heigh_wall,textureCorridoio,[5,5],23,27.9,heigh_floor);
          corridoioKitchen.add(par2);
          // porta corridioi centrale
          var par3 = this.mkWallDoor(26.4,heigh_wall,4,12,textureCorridoio,32.9,28,heigh_floor,3);
          par3.rotation.y = -Math.PI/2;
          corridoioKitchen.add(par3);
          //finestra
          var par4 = this.mkWallWindow(10,heigh_wall,4.8,7.8,textureCorridoio,[2,2],33,1.55,heigh_floor,2.7,4.4);
          par4.rotation.y = Math.PI;
          corridoioKitchen.add(par4);


          var bagno = new THREE.Object3D();
          walls.add(bagno); 
          var textureBagno = "piastrella.jpg"; 
          //parete cesso
          var par1 = this.mkWall(15,heigh_wall,textureBagno,[20,20],27.1,9,heigh_floor);
          par1.rotation.y = Math.PI/2;
          bagno.add(par1);
          //parete porta
          var par2 = this.mkWallDoor(16.5,heigh_wall,4,12,textureBagno,34.6,16.4,heigh_floor,6);
          bagno.add(par2);
          // parete doccia
          var par3 = this.mkWall(15,heigh_wall,textureBagno,[20,20],43.4,9,heigh_floor);
          par3.rotation.y = -Math.PI/2;
          bagno.add(par3);
          //finestra
          var par4 = this.mkWallWindow(16.5,heigh_wall,4.8,7.8,textureBagno,[2,2],51,1.55,heigh_floor,9,4.4);
          par4.rotation.y = Math.PI;
          bagno.add(par4);


          var camera = new THREE.Object3D();
          walls.add(camera); 
          var textureCamera = "StanzePattern.jpg"; 
          //parete vuota lato cesso
          var par1 = this.mkWall(15,heigh_wall,textureCamera,[5,5],45.1,9,heigh_floor);
          par1.rotation.y = Math.PI/2;
          camera.add(par1);
          //parete porta
          var par2 = this.mkWallDoor(16.5,heigh_wall,4,12,textureCamera,52.6,16.4,heigh_floor,0.5);
          camera.add(par2);
          // parete verso esterno
          var par3 = this.mkWall(15,heigh_wall,textureCamera,[5,5],61.4,9,heigh_floor);
          par3.rotation.y = -Math.PI/2;
          camera.add(par3);
          //finestra
          var par4 = this.mkWallWindow(16.5,heigh_wall,4.8,7.8,textureCamera,[2,2],69,1.55,heigh_floor,2.6,4.4);
          par4.rotation.y = Math.PI;
          camera.add(par4);

          var salone = new THREE.Object3D();
          walls.add(salone); 
          var textureSalone = "SalonePattern.jpg"; 
          //parete finestra
          var par1 = this.mkWallWindow(31.5,heigh_wall,9.6,7.8,textureSalone,[2,2],1.6,29.5,heigh_floor,5.3,4.4);
          par1.rotation.y = Math.PI/2;
          salone.add(par1);
          //parete porta cucina
          var par2 = this.mkWallDoor(31.5,heigh_wall,4,12,textureSalone,33,29.6,heigh_floor,19.5);
          par2.rotation.y = Math.PI;
          salone.add(par2);
          // parete verso esterno
          var par3 = this.mkWallDoor(31.5,heigh_wall,4,12,textureSalone,32.9,61,heigh_floor,3);
          par3.rotation.y = -Math.PI/2;
          salone.add(par3);
          //finestra
          var par4 = this.mkWall(31.5,heigh_wall,textureSalone,[5,5],1.55,60.9,heigh_floor);
          salone.add(par4);

          var stanza = new  THREE.Object3D();
          walls.add(stanza); 
          var textureStanza = "StanzePattern.jpg"; 
          //parete porta
          var par1 = this.mkWallDoor(20,heigh_wall,4,12,textureStanza,46.02,29.6,heigh_floor,8);
          par1.rotation.y = Math.PI/2;
          salone.add(par1);
          //parete verso stanze
          var par2 = this.mkWall(11.5,heigh_wall,textureStanza,[5,5],46,29.6,heigh_floor);
          par2.rotation.y = Math.PI;
          salone.add(par2);
          // parete verso esterno
          var par3 = this.mkWall(20,heigh_wall,textureStanza,[5,5],47.48,39.5,heigh_floor);
          par3.rotation.y = -Math.PI/2;
          salone.add(par3);
          //parete verso ingresso
          var par4 = this.mkWall(11.5,heigh_wall,textureStanza,[5,5],46,49.45,heigh_floor);
          salone.add(par4);

          var stanzina = new  THREE.Object3D();
          walls.add(stanzina); 
          var textureStanza = "StanzinoECorridoio.jpg"; 
          //parete porta
          var par1 = this.mkWallDoor(10,heigh_wall,4,12,textureStanza,59.1,18,heigh_floor,3);
          par1.rotation.y = Math.PI/2;
          stanzina.add(par1);
          //parete verso stanze
          var par2 = this.mkWall(10,heigh_wall,textureStanza,[5,5],59,18.1,heigh_floor);
          par2.rotation.y = Math.PI;
          stanzina.add(par2);
          // parete verso esterno
          var par3 = this.mkWall(10,heigh_wall,textureStanza,[5,5],63.9,23,heigh_floor);
          par3.rotation.y = -Math.PI/2;
          stanzina.add(par3);
          //parete verso ingresso
          var par4 = this.mkWall(10,heigh_wall,textureStanza,[5,5],59,27.9,heigh_floor);
          stanzina.add(par4);


          return walls
    },

    objToScene: function(scene, objs){
        for(obj in objs){
          scene.add(objs[obj]);
        }
    }

	}
	return utility;
}()