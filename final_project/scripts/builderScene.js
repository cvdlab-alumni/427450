function importHome(){

  var loader = new THREE.OBJLoader();
  loader.load('./models/appartamentoCopia.obj', function (obj) {
    var material = new THREE.MeshLambertMaterial({color: 0xF2F2F2, shading: true, side: THREE.DoubleSide});
    obj.traverse(function (child) {
      if (child instanceof THREE.Mesh) {
        child.material = material;
      }
    });
    mesh = obj;
    obj.rotation.x = -Math.PI/2;
    obj.scale.set(5, 5, 5);
    scene.add(obj);
  });
}

function buildWalls(){
  var walls = utility.mkWalls()
  walls.rotation.x = -Math.PI/2;
  scene.add(walls)
}

function buildVideo(){
      
  if (!navigator.webkitGetUserMedia) {
    fallback();
  } else {
  navigator.webkitGetUserMedia(
    {video: true},  
    function success(stream) {
        video.src = window.URL.createObjectURL(stream);
    }, 
    function fallback(e) {
        video.src = null;
    });
  }

  videoTexture = new THREE.Texture( video );
  var material   = new THREE.MeshLambertMaterial({
     map : videoTexture
  });
  var geometry = new THREE.PlaneGeometry(5.6,4.1)
  videoWebcam = new THREE.Mesh(geometry, material);
  videoWebcam.position.set(14.2,8.45,-60.4)
  scene.add(videoWebcam)

}

function buildAudio(){
  
  audio = document.createElement('audio');
  var source = document.createElement('source');
  source.src = './scripts/suono.mp3';
  audio.appendChild(source);
}

function buildAllRooms(){

  diningRoom.setSofa(scene)
  diningRoom.setTelevision(scene)
  diningRoom.setFlowerPot(scene)
  diningRoom.setTableSofa(scene)
  diningRoom.setCarpetDining(scene)
  diningRoom.setLibraryDining(scene)
  diningRoom.setConditionalAir(scene)
  diningRoom.setAudioBox()

  kitchen.setKitchen(scene)
  kitchen.setCook(scene)
  kitchen.setFridge(scene)
  kitchen.setMensola(scene)
  kitchen.setTableAndChair(scene)

  bathroom.setToilet(scene)
  bathroom.setShower(scene)
  bathroom.setBathSink(scene)
  bathroom.setBidet(scene)
  bathroom.setTowel(scene)

  room.setDesk(scene)
  room.setChair(scene)
  room.setMacbookPro(scene)
  room.setLibrary(scene)
  room.setBed(scene)
  room.setTable(scene)
  room.setWardrobe(scene)

}

function buildDoorsAndwindows(){

  var pavimentoSale = utility.mkPlaneGeometry(34,61,17,1.55,-31,'marmo.jpg',[5,5])
  var pavimentoBagno = utility.mkPlaneGeometry(18,17,43,1.55,-8.5,'piastrella.jpg',[5,5])
  var pavimentoStanza1 = utility.mkPlaneGeometry(18,17,61,1.55,-8.5,'parquet.jpg',[5,5])
  var pavimentoStanza2 = utility.mkPlaneGeometry(12.5,22,51.5,1.55,-40,'parquet.jpg',[5,5])
  var pavimentoCorridoio1 = utility.mkPlaneGeometry(30,11,44,1.55,-56.5,'marmo.jpg',[5,1])
  var pavimentoCorridoio2 = utility.mkPlaneGeometry(37,11,52,1.55,-22.5,'marmo.jpg',[5,1])
  var pavimentoCorridoio3 = utility.mkPlaneGeometry(11,26,40,1.55,-40,'marmo.jpg',[1,3])
  var pavimentoEsterno = utility.mkPlaneGeometry(90, 90, 35, -0.1, -32,'grass.jpg',[5, 5])

  var doorMain = utility.mkDoor(12.35,4,0.9,58.5,56,7.6,'legno.jpg', toIntersect)
  doorMain.rotation.x = - Math.PI/2;
  var door  = utility.mkDoor(12.35,4,0.9,22.5,9,7.6,'legno.jpg', toIntersect)
  door.rotation.x = - Math.PI/2;
  var door2 = utility.mkDoor(12.35,4,0.9,33.5,23,7.6,'legno.jpg', toIntersect)
  door2.rotation.x = - Math.PI/2;
  var door3 = utility.mkDoor(12.35,4,0.9,33.5,56,7.6,'legno.jpg', toIntersect)
  door3.rotation.x = - Math.PI/2;
  var door4 = utility.mkDoor(12.35,4,0.9,58.5,23,7.6,'legno.jpg', toIntersect)
  door4.rotation.x = - Math.PI/2;
  var door5 = utility.mkDoor(12.35,4,0.9,45,39.5,7.6,'legno.jpg', toIntersect)
  door5.rotation.x = - Math.PI/2;

  var door6 = utility.mkDoor(12.35,4,0.9,11.5,29,7.6,'legno.jpg', toIntersect)
  door6.rotation.z = Math.PI/2;
  door6.rotation.y = 0;
  var door7 = utility.mkDoor(12.35,4,0.9,42.38,17,7.6,'legno.jpg', toIntersect)
  door7.rotation.z = Math.PI/2;
  door7.rotation.y = 0;
  var door8 = utility.mkDoor(12.35,4,0.9,55,17,7.6,'legno.jpg', toIntersect)
  door8.rotation.z = Math.PI/2;
  door8.rotation.y = 0;

  var win1 = utility.mkWindow(8,5,0,5.8,-11.5,[], toIntersect)
  win1.rotation.x =  -Math.PI/2;
  var win2 = utility.mkWindow(8,5,25.5,5.8,0,['z','x'], toIntersect)
  var win3 = utility.mkWindow(8,5,37,5.8,0,['z','x'], toIntersect)
  var win4 = utility.mkWindow(8,5,61.5,5.8,0,['z','x'], toIntersect)
  var win5 = utility.mkWindows(10,8,0,5.8,-34.5,[],toIntersect)
  win5.rotation.y = Math.PI/2;

  objs = objs.concat([pavimentoSale, pavimentoBagno, pavimentoStanza1, pavimentoStanza2,
                      pavimentoCorridoio1, pavimentoCorridoio2, pavimentoCorridoio3, doorMain, 
                      door, door2, door3,door4, door5, door6, door7, door8, 
                      win1, win2, win3, win4, win5,pavimentoEsterno])

  utility.objToScene(scene, objs);      
}

function buildLamp(){

    lampArray = [
     {x: 12,   z:-15, name:'cucina'},
     {x: 28,   z:-15, name:'corridoioCucina'},
     {x: 42.5, z:-9.5, name:'bagno'},
     {x: 61,   z:-9.5, name:'camera1'},
     {x: 12,   z:-40, name:'salone1'},
     {x: 23,   z:-50, name:'salone2'},
     {x: 53,   z:-40, name:'camera2'},
     {x: 40,   z:-30, name:'corridoio1'},
     {x: 40,   z:-50, name:'corridoio2'},
     {x: 64,   z:-23, name:'stanzino'}
    ];
      
    for(var i=0;i< lampArray.length; i++){
        var lamp = utility.mkLamp(lampArray[i].x, lampArray[i].z, lampArray[i].name, toIntersect)
        scene.add(lamp)
    } 
}