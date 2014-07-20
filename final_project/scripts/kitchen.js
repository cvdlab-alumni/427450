! function(){
	kitchen = {

	    setKitchen : function(scene){
	      var loader2 = new THREE.OBJMTLLoader();
	      loader2.addEventListener('load', function (event) {
	        var object2 = event.content;
	          object2.rotation.y= Math.PI;
	          object2.scale.set(0.07, 0.07, 0.07);
	          object2.position.set(10.5,1.55,-3.5);
	          scene.add(object2);
	      });
	      loader2.load('models/19.011.0001carol.obj', 'models/19.011.0001carol.obj.mtl', {side: THREE.DoubleSide});
	    },

	    setCook: function(scene){
	      var loader2 = new THREE.OBJMTLLoader();
	      loader2.addEventListener('load', function (event) {
	        var object2 = event.content;
	          object2.rotation.y=Math.PI/2;
	          object2.scale.set(0.06, 0.06, 0.06);
	          object2.position.set(5,1.55,-17);
	          scene.add(object2);
	      });
	      loader2.load('models/cucina.obj', 'models/cucina.mtl', {side: THREE.DoubleSide});
	    },

	    setFridge : function(scene){
	      var loader2 = new THREE.OBJMTLLoader();
	      loader2.addEventListener('load', function (event) {
	        var object2 = event.content;
	          object2.rotation.y=Math.PI;
	          object2.scale.set(1.4, 1.2, 1);
	          object2.position.set(11,10,-12);
	          scene.add(object2);
	      });
	      loader2.load('models/frigorifero_Scene.obj', 'models/frigorifero_Scene.mtl', {color: 0xffffff, side: THREE.DoubleSide});
	    },

	    setMensola : function(scene){
	      var loader2 = new THREE.OBJMTLLoader();
	      loader2.addEventListener('load', function (event) {
	        var object2 = event.content;
	          object2.scale.set(0.07, 0.07, 0.07);
	          object2.rotation.y=Math.PI/2;
	          object2.position.set(1.7,-1,14);
	          scene.add(object2);
	      });
	      loader2.load('models/mensola.obj', 'models/mensola.mtl', {color: 0xffffff, side: THREE.DoubleSide});
	    },

	    setTableAndChair : function(scene){
	      var loader = new THREE.OBJLoader();
	      loader.load('models/table_chairs.obj', function (obj) {
	        global_o = obj;
	        var texture = THREE.ImageUtils.loadTexture("models/Wood.jpg")
	        var material = new THREE.MeshPhongMaterial();
	        texture.wrapS =  texture.wrapT = THREE.RepeatWrapping;
	        texture.repeat.set(3,3)
	        material.map = texture;
	        mesh = new THREE.Mesh(obj.children[0].geometry, material);
	        mesh.scale.set(0.8,0.9,0.8);
	        mesh.position.set(16.1,1.55,-16.3);
	        scene.add(mesh);
	      });
	    }
	}
	return kitchen;
}()