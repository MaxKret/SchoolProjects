const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth,window.innerHeight );
document.body.appendChild( renderer.domElement );

const scene = new THREE.Scene();

// camera init
const camera = new THREE.PerspectiveCamera(45,window.innerWidth/window.innerHeight, 0.1, 1000);
camera.position.set(0, 30, 150);

//lights
const bulb = new THREE.SphereGeometry( 2, 16, 8 );
const pointLight1 = new THREE.PointLight(0xFF0000, 4, 50);
pointLight1.add( new THREE.Mesh( bulb, new THREE.MeshBasicMaterial( { color: 0xff0000 } ) ) );
pointLight1.position.set( -30, 30, 20 );

const dirLight1 = new THREE.DirectionalLight(0x0000FF, 0.125);
dirLight1.add( new THREE.Mesh( bulb, new THREE.MeshBasicMaterial( { color: 0x0000FF } ) ) );
dirLight1.position.set( 40, 30, 20 );

// orbit controls
let controls = new THREE.OrbitControls(camera, renderer.domElement);
controls.update();

//floor
const floor_geometry = new THREE.BoxGeometry( 1000, 5, 1000 );
const floor_material = new THREE.MeshBasicMaterial( {color: 0x202020, side: THREE.DoubleSide} );
const floor_mesh = new THREE.Mesh( floor_geometry, floor_material );
const floor = new THREE.Object3D();
floor.position.y = -10;
floor.add(floor_mesh);

//cube 1: green
const cube1_geometry = new THREE.BoxGeometry(10, 10, 10);
const cube1_material = new THREE.MeshBasicMaterial( {color: 0x00ff00} );
const cube1_mesh = new THREE.Mesh( cube1_geometry, cube1_material );
const cube1 = new THREE.Object3D();
cube1.position.x = 20;
cube1.position.z = 60;
cube1.add( cube1_mesh );

//sphere 1: grey
const sphere1_geometry = new THREE.SphereGeometry(8);
const sphere1_material = new THREE.MeshBasicMaterial( {color: 0x9F9F9F} );
const sphere1_mesh = new THREE.Mesh( sphere1_geometry, sphere1_material );
const sphere1 = new THREE.Object3D();
sphere1.position.x = -20;
sphere1.position.z = 40;
sphere1.add( sphere1_mesh );

//cube 2: white
const cube2_geometry = new THREE.BoxGeometry(10, 10, 10);
const cube2_material = new THREE.MeshPhongMaterial( {color: 0xFFFFFF} );
const cube2_mesh = new THREE.Mesh( cube2_geometry, cube2_material );
const cube2 = new THREE.Object3D();
cube2.position.x = 10;
cube2.position.z = 0;
cube2.add( cube2_mesh );

//sphere 2: grey
const sphere2_geometry = new THREE.SphereGeometry(8);
const sphere2_material = new THREE.MeshPhongMaterial( {color: 0x9F9F9F} );
const sphere2_mesh = new THREE.Mesh( sphere2_geometry, sphere2_material );
const sphere2 = new THREE.Object3D();
sphere2.position.x = -20;
sphere2.position.z = -20;
sphere2.add( sphere2_mesh );


scene.add( camera );
scene.add( pointLight1 );
scene.add( dirLight1 );
scene.add( floor );
scene.add( cube1 );
scene.add( sphere1 );
scene.add( cube2 );
scene.add( sphere2 );

draw = function () 
{
	requestAnimationFrame( draw );

	controls.update();

	renderer.render( scene, camera );
	
};
draw();
