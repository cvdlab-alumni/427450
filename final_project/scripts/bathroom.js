! function(){
  bathroom = { 

    setToilet : function(scene){
      var loader = new THREE.OBJLoader();
      loader.load('models/toilet.obj', function (obj) {
        var multiMaterial = [new THREE.MeshLambertMaterial({color: 0xffffff, side: THREE.DoubleSide})];
        mesh = THREE.SceneUtils.createMultiMaterialObject(obj.children[0].geometry, multiMaterial);
        mesh.scale.set(0.007,0.008,0.008);
        mesh.position.set(35.5,1.55,-11.5);
        mesh.rotation.x= -Math.PI/2;
        scene.add(mesh);
      });
    },

    setShower : function(scene){
      var loader2 = new THREE.OBJMTLLoader();
      loader2.addEventListener('load', function (event) {
        var object2 = event.content;
          object2.scale.set(0.17, 0.15, 0.17);
          object2.position.set(48,1.5,-4.5);
          scene.add(object2);
      });
      loader2.load('models/3dm-shower.obj', 'models/3dm-shower.obj.mtl', {side: THREE.DoubleSide});
    },

    setBidet : function(scene){
      var loader2 = new THREE.OBJMTLLoader();
      loader2.addEventListener('load', function (event) {
        var object2 = event.content;
          object2.rotation.y=Math.PI/2;
          object2.scale.set(0.08, 0.07, 0.07);
          object2.position.set(36,1.55,-9.3);
          scene.add(object2);
      });
      loader2.load('models/bidet.obj', 'models/bidet.mtl', {side: THREE.DoubleSide});
    },

    setBathSink : function(scene){
      var loader2 = new THREE.OBJMTLLoader();
      loader2.addEventListener('load', function (event) {
        var object2 = event.content;
          object2.rotation.y=Math.PI;
          object2.scale.set(0.3, 0.3, 0.3);
          object2.position.set(49.3,2.7,-11.5);
          scene.add(object2);
      });
      loader2.load('models/Lavabo.obj', 'models/Lavabo.obj.mtl', {side: THREE.DoubleSide});
    },

    setTowel : function(scene){
      var loader2 = new THREE.OBJMTLLoader();
      loader2.addEventListener('load', function (event) {
        var object2 = event.content;
          object2.scale.set(0.3, 0.1, 0.3);
          object2.position.set(49.3,2,-16);
          scene.add(object2);
      });
      loader2.load('models/towel.obj', 'models/towel.obj.mtl', {side: THREE.DoubleSide});
    },
  }
  return bathroom;
}()