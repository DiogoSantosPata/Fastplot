import socket
import numpy as np

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
