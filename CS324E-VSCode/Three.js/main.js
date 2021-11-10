const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth,window.innerHeight );
document.body.appendChild( renderer.domElement );

const scene = new THREE.Scene();

// camera init
const camera = new THREE.PerspectiveCamera(50,window.innerWidth/window.innerHeight, 0.1, 1000);
camera.position.set(0, 0, 100);
scene.add(camera);

// orbit controls
let controls = new THREE.OrbitControls(camera, renderer.domElement);
controls.update();

//floor

const floor_geometry = new THREE.PlaneGeometry( 1000, 1000, 1, 1 );
const floor_material = new THREE.MeshBasicMaterial( {color: 0x202020, side: THREE.DoubleSide} );
const floor_mesh = new THREE.Mesh( floor_geometry, floor_material );
floor_mesh.rotation.x = -Math.PI / 2;
floor_mesh.position.y = -50;

const floor = new THREE.Object3D();
floor.add(floor_mesh);

//cube 1: green
const cube_geometry = new THREE.BoxGeometry(20, 20, 20);
const cube_material = new THREE.MeshBasicMaterial( {color: 0x00ff00} );
const cube_mesh = new THREE.Mesh( cube_geometry, cube_material );
const cube = new THREE.Object3D();
cube.rotation.x = 0;
cube.rotation.y = 0;
cube.rotation.z = 0;
cube.add( cube_mesh );	

scene.add( floor_mesh );
scene.add( cube );

draw = function () 
{
	requestAnimationFrame( draw );

	controls.update();

	renderer.render( scene, camera );
	
};
draw();
