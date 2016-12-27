import socket
import numpy as np
import os
import webbrowser

class fastplot():
	"""
	Fast_Plot_Python_in_the_Browser [fastplot] is a python class used to easily 
	visualise your data in your favourite browser. 
	Get the best of both worlds: Python to compute, JavaScript to render. 

	As you can see the this package is still in early stage, please help :)

	https://github.com/DiogoSantosPata/Fast_Plot_Python_in_the_Browser
	Author: Diogo Santos-Pata, 2016
	"""

	UDP_IP = "127.0.0.1"
	UDP_PORT = 5005
	sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

	### open browser

	html_doc = """
	<html>

<style>
	body{ background-color: rgb(40,40,40); }
</style>

<title>FastPlot</title>

<body onload='init()'>

	<div>
		<button onclick='reconnect()'>Reconnect</button>
		<button onclick='quit()'>Pause</button>
	</div>

</body>

<!-- Websocket -->
<script type='text/javascript'>
// Config
var port = 9000;
var host = 'ws://127.0.0.1:'+port; // No need to change this if using localhost

//Declare Variables
var socket;
var explodedValues;
var counter = 0;
var ctx;
var net_color =  'rgba(250,0,0,'  // 'rgba(220,110,20,' //'rgba(0,0,255,';  // 'rgba(0,0,250,';   


function init() {
	try {
		socket = new WebSocket(host);
		console.log('WebSocket status '+socket.readyState);
		socket.onopen    = function(msg) { 
							   console.log('Welcome - status '+this.readyState); 
						   };

		socket.onmessage = function(msg) {														
		  				    explodedValues = msg.data.split(';');
    						drawVisualization();    						
						   };

		socket.onclose   = function(msg) { 
							   console.log('Disconnected - status '+this.readyState); 
						   };
	}
	catch(ex){ 
		console.log(ex); 
	}
	
}

function quit(){
	if (socket != null) {
		console.log('Close Socket');
		socket.close();
		socket=null;
	}
}
function reconnect() {
	quit();
	init();
}





function build_canvas (canvas_name)
{

	div = document.createElement('span');

	document.getElementsByTagName('body')[0].appendChild(div);

	title = document.createElement('p');
	title.textContent = canvas_name;
	title.style.color = 'white';
	div.appendChild(title)


	canvas = document.createElement('canvas');
	canvas.id = canvas_name;
	canvas.style.border = '1px solid white';
	canvas.width  = window.innerWidth  * 0.3; // canvas_width  ||  window.innerWidth  * 0.9;
	canvas.height = window.innerHeight * 0.3; // canvas_height ||  window.innerHeight * 0.9;	
	context = canvas.getContext('2d');

	div.appendChild(canvas)

	var body = document.getElementsByTagName('body')[0];
	body.appendChild(div);
}


function run_pcolor()
{
	if( document.getElementById(explodedValues[1]) ) { canvas = document.getElementById( explodedValues[1] ); }
	else{ build_canvas(explodedValues[1]); }

	ctx_1 = canvas.getContext('2d');
	ctx_1.clearRect(0, 0, canvas.width, canvas.height);
	ctx_1.fillStyle = 'rgba(255,255,255,1)'; //'rgba(255,255,255,1)';
	ctx_1.fillRect(0, 0, canvas.width, canvas.height);

	// var size_loop = Math.sqrt(  explodedValues.length - 3 );  /// remove 3, cause of the first 2 indexes
	var square_width = canvas.width/explodedValues[3] ; 
	var square_height = canvas.height/explodedValues[2] ; 


	counter = 4;
	for(var x=0;x<explodedValues[3];x++){
		for(var y=0;y<explodedValues[2];y++){
			ctx_1.fillStyle = net_color+explodedValues[counter]+')';
			ctx_1.fillRect(x*square_width, y*square_height, square_width, square_height);


			counter = counter + 1;
		}
	}
}




function run_plot()
{	
	if( document.getElementById(explodedValues[1]) ) { canvas = document.getElementById( explodedValues[1] ); }
	else{ build_canvas(explodedValues[1]); }

	ctx = canvas.getContext('2d');
	ctx.beginPath();
	ctx.clearRect(0, 0, canvas.width, canvas.height);
	
	ctx.fillStyle = 'white';
	ctx.fillRect(0, 0, canvas.width, canvas.height);

	ctx.beginPath();

	ctx.lineWidth = 3.5;
	ctx.moveTo(0, explodedValues[1]*canvas.height );

	for(var i=2; i<explodedValues.length; i++)
	{	
		ctx.lineTo(i*(canvas.width/explodedValues.length)  , explodedValues[i]*canvas.height  );
	}

	ctx.strokeStyle = 'red';
	ctx.stroke();
}


function run_barplot()
{
	if( document.getElementById(explodedValues[1]) ) { canvas = document.getElementById( explodedValues[1] ); }
	else{ build_canvas(explodedValues[1]); }

	ctx = canvas.getContext('2d');
	ctx.clearRect(0, 0, canvas.width, canvas.height);
	ctx.fillStyle = 'rgba(255,255,255,1)';

	bar_width = canvas.width / (explodedValues.length-2);

	for(var i=2; i<explodedValues.length; i++)
	{	
		ctx.fillRect( bar_width*(i-2), canvas.height, bar_width, explodedValues[i]*-canvas.height);
	}	
}


function drawVisualization()
{
	if ( explodedValues[0] == 'pcolor' ){ run_pcolor(); }
	if ( explodedValues[0] == 'plot' ){ run_plot(); }
	if ( explodedValues[0] == 'barplot' ){ run_barplot(); }
};

</script>


</html>
	"""



	path_of_index = os.getcwd()+'/temp.html'
	f = open(path_of_index,'w')
	f.write(html_doc)
	f.close()
	path_of_index = 'file://'+path_of_index
	webbrowser.open(path_of_index)



	@staticmethod
	def build_canvas( canvas_name ):				
		fastplot.sock.sendto(message_string, (fastplot.UDP_IP, fastplot.UDP_PORT))		

	@staticmethod
	def pcolor( canvas_name, msg):
		msg_shape = msg.shape  ## Get shape of input		
		msg = np.ravel(msg)    ## Flatten the array into 1d
		message_string = np.around( (msg - msg.min())/(msg.max() - msg.min()), decimals=2) # Normalizing the values...	
		message_string = np.hstack( ( ['pcolor',canvas_name,msg_shape[0],msg_shape[1]], message_string) ) # Stack horizontal index and message...		
		message_string = ";".join( message_string.astype(str)  ) # Add ';' in between values so that JS can parse them later		
		fastplot.sock.sendto(message_string, (fastplot.UDP_IP, fastplot.UDP_PORT)) # Send it!

	@staticmethod
	def plot( canvas_name, msg):	
		msg = np.ravel(msg)			
		message_string = np.around( (msg - msg.min())/(msg.max() - msg.min()), decimals=2) # Normalizing the values...		
		message_string = np.hstack( ( ['plot',canvas_name], message_string) ) # Stack horizontal index and message...		
		message_string = ";".join( message_string.astype(str)  ) # Add ';' in between values so that JS can parse them later		
		fastplot.sock.sendto(message_string, (fastplot.UDP_IP, fastplot.UDP_PORT)) # Send it!

	@staticmethod
	def barplot( canvas_name, msg):	
		msg = np.ravel(msg)			
		message_string = np.around( (msg - msg.min())/(msg.max() - msg.min()), decimals=2) # Normalizing the values...		
		message_string = np.hstack( ( ['barplot',canvas_name], message_string) ) # Stack horizontal index and message...		
		message_string = ";".join( message_string.astype(str)  ) # Add ';' in between values so that JS can parse them later		
		fastplot.sock.sendto(message_string, (fastplot.UDP_IP, fastplot.UDP_PORT)) # Send it!

