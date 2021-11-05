const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000 );
const renderer = new THREE.WebGLRenderer();

renderer.setSize( window.innerWidth,window.innerHeight );
document.body.appendChild( renderer.domElement );

const geometry = new THREE.BoxGeometry();
const material = new THREE.MeshBasicMaterial( {color: 0x00ff00} );
material.wireframe = true;
const cube = new THREE.Mesh( geometry, material );

const pivot = new THREE.Object3D();

pivot.add( cube );		
scene.add( pivot );

camera.position.z = 5;
cube.position.x = 1;

draw = function () 
{
	requestAnimationFrame( draw );
	renderer.render( scene, camera );
	pivot.rotation.x += 0.01;
	pivot.rotation.y += 0.01;
};
draw();
