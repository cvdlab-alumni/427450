! function(){
	diningRoom = {

    setSofa : function(scene){
      var loader = new THREE.OBJMTLLoader();
      loader.addEventListener('load', function (event) {
        var object = event.content;
          object.rotation.y=Math.PI;
          object.scale.set(5.5, 5.5, 5.5);
          object.position.set(14,1.5,-47);
          scene.add(object);
      });
      loader.load('models/simple_sofa.obj', 'models/simple_sofa.mtl', {side: THREE.DoubleSide});
    },

    setTelevision : function(scene){    
      var loader = new THREE.OBJMTLLoader();
      loader.addEventListener('load', function (event) {
        var object = event.content;
          object.scale.set(0.05, 0.05, 0.05);
          object.position.set(11,6,-61);
          scene.add(object);
      });
      loader.load('models/tv.obj', 'models/tv.mtl', {side: THREE.DoubleSide}); 
    },

    setTableSofa : function(scene){
      var loader = new THREE.OBJMTLLoader();
      loader.addEventListener('load', function (event) {
        var object = event.content;
          object.rotation.y=Math.PI/2;
          object.scale.set(1.5, 1.5, 1.5);
          object.position.set(14,1.5,-54);
          scene.add(object);
      });
      loader.load('models/StylishDesk.obj', 'models/StylishDesk.mtl', {side: THREE.DoubleSide});
    },

    setCarpetDining : function(scene){
      var loader = new THREE.OBJMTLLoader();
      loader.addEventListener('load', function (event) {
        var object = event.content;
          object.rotation.y=Math.PI/6;
          object.scale.set(0.03, 0.03, 0.03);
          object.position.set(14,1.55,-54);
          scene.add(object);
      });
      loader.load('models/oriental-rug.obj', 'models/oriental-rug.mtl', {side: THREE.DoubleSide});
    },

    setLibraryDining : function(scene){
      var loader = new THREE.OBJMTLLoader();
      loader.addEventListener('load', function (event) {
        var object = event.content;
          object.rotation.y=Math.PI;
          object.scale.set(0.05, 0.05, 0.05);
          object.position.set(20,5.8,-30);
          scene.add(object);
      });
      loader.load('models/full-bookcase.obj', 'models/full-bookcase.mtl', { side: THREE.DoubleSide});
    },

    setConditionalAir : function(scene){
      var loader = new THREE.OBJMTLLoader();
      loader.addEventListener('load', function (event) {
        var object = event.content;
          object.rotation.y=Math.PI/2;
          object.scale.set(0.05, 0.05, 0.05);
          object.position.set(2,12.5,-51);
          scene.add(object);
      });
      loader.load('models/internal-unity-air-conditioning.obj', 'models/internal-unity-air-conditioning.mtl', { side: THREE.DoubleSide});
    },

    setFlowerPot : function(scene){
      var loader = new THREE.OBJMTLLoader();
      loader.addEventListener('load', function (event) {
        var object = event.content;
          object.scale.set(5, 5, 5);
          object.position.set(3,1.5,-31);
          scene.add(object);
      });
      loader.load('models/maceta.obj', 'models/maceta.mtl', {side: THREE.DoubleSide}); 
    },

    setAudioBox : function(){
      var geometry = new THREE.BoxGeometry( 6.5, 1, 0.2, 1)
      var material = new THREE.MeshPhongMaterial( { color: 0x000000 } );
      var box =  new THREE.Mesh(geometry, material);
      box.position.set(14.4,4.5,-60.8);
      toIntersect.push(box)
      box.play = false;
      box.interact = function(){
        if(!this.play){
         this.play = true;
         audio.play();
       }else{
        this.play = false;
        audio.pause();
       }
      }
      scene.add(box)
	 }
}
	return diningRoom;
}()