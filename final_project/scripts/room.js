! function(){
  room = {

    setTable : function(scene){
      var loader2 = new THREE.OBJMTLLoader();
      loader2.addEventListener('load', function (event) {
        var object2 = event.content;
          object2.scale.set(1.8, 1.8, 1.8);
          object2.position.set(25,1.5,-25);
          scene.add(object2);
      });
      loader2.load('models/StylishDesk.obj', 'models/StylishDesk.mtl', {side: THREE.DoubleSide});
    },
  
    setDesk : function(scene){
      var loader2 = new THREE.OBJMTLLoader();
      loader2.addEventListener('load', function (event) {
        var object2 = event.content;
          object2.rotation.y=-Math.PI/2;
          object2.scale.set(0.02, 0.025, 0.02);
          object2.position.set(56.5,1.55,-40);
          scene.add(object2);
      });
      loader2.load('models/Desk1 Polygon.obj', 'models/Desk1 Polygon.obj.mtl', {side: THREE.DoubleSide});
    },

    setChair : function(scene){
      var loader2 = new THREE.OBJMTLLoader();
      loader2.addEventListener('load', function (event) {
        var object2 = event.content;
          object2.rotation.y=Math.PI/2;
          object2.scale.set(0.05, 0.05, 0.05);
          object2.position.set(54,1.55,-39);
          scene.add(object2);
      });
      loader2.load('models/cho036.obj', 'models/cho036.obj.mtl', {side: THREE.DoubleSide}); 
    },

    setLibrary : function(scene){
      var loader3 = new THREE.OBJMTLLoader();
      loader3.addEventListener('load', function (event) {
        var object3 = event.content;
          object3.rotation.y=-Math.PI/2;
          object3.scale.set(0.04, 0.04, 0.04);
          object3.position.set(56,1.5,-48);
          scene.add(object3);
      });
      loader3.load('models/13.001.0001teen.obj', 'models/13.001.0001teen.obj.mtl', {side: THREE.DoubleSide}); 
    },

    setMacbookPro : function(scene){
      var loader2 = new THREE.OBJMTLLoader();
      loader2.addEventListener('load', function (event) {
        var object2 = event.content;
          object2.rotation.y=-Math.PI/2;
          object2.scale.set(0.002, 0.0025, 0.002);
          object2.position.set(55.5,6,-40);
          scene.add(object2);
      });
      loader2.load('models/macbook_pro_15_.obj', 'models/macbook_pro_15_.obj.mtl', {side: THREE.DoubleSide}); 
    },

    setBed: function(scene){
      var loader2 = new THREE.OBJMTLLoader();
      loader2.addEventListener('load', function (event) {
        var object2 = event.content;
          object2.scale.set(5.5, 3, 4);
          object2.position.set(68.5,1.5,-12);
          object2.rotation.y=-Math.PI/2;
          object2.castShadow = true;
          object2.receiveShadow = true;
          scene.add(object2);
      });
      loader2.load('models/bed1.obj', 'models/bed1.mtl', {side: THREE.DoubleSide});
     var loader3 = new THREE.OBJMTLLoader();
      loader3.addEventListener('load', function (event) {
        var object = event.content;
          object.scale.set(3, 6, 4);
          object.rotation.y=-Math.PI/2;
          object.position.set(57,1.5,-32);
          object.castShadow = true;
          object.receiveShadow = true;
          scene.add(object);
      });
      loader3.load('models/bed1.obj', 'models/bed1.mtl', {side: THREE.DoubleSide});
    },

    setWardrobe: function(scene){
      var loader2 = new THREE.OBJMTLLoader();
      loader2.addEventListener('load', function (event) {
        var object2 = event.content;
          object2.rotation.y=Math.PI/2;
          object2.scale.set(0.04, 0.04, 0.04);
          object2.position.set(53.5,1.55,-7);
          scene.add(object2);
      });
      loader2.load('models/wardrobe1.obj', 'models/wardrobe1.mtl', {side: THREE.DoubleSide});

      var loader1 = new THREE.OBJMTLLoader();
      loader1.addEventListener('load', function (event) {
        var object2 = event.content;
          object2.rotation.y=-Math.PI/2;
          object2.scale.set(0.035, 0.04, 0.04);
          object2.position.set(68,1.55,-23);
          scene.add(object2);
      });
      loader1.load('models/wardrobe1.obj', 'models/wardrobe1.mtl', {side: THREE.DoubleSide});
    },
  }
  return room;
}()