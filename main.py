import numpy as np
import socket
from time import sleep


UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP


def sender( index, msg):
	message_string = msg

	# Normalizing the values...
	if index == '1.0': message_string = np.around( (msg - msg.min())/(msg.max() - msg.min()), decimals=2)

	# Stack horizontal index and message...
	message_string = np.hstack( ( [index], message_string) )

	# Add ';' in between values so that JS can parse them later
	message_string = ";".join( message_string.astype(str)  )

	# Send it!
	sock.sendto(message_string, (UDP_IP, UDP_PORT))


def main():	

	counter = 0

	msg_2 = ['d','a','c','X']   	
	msg_3 = np.ones(20) * 0.5 # line plot data
	msg_4 = np.random.uniform(0,1,3)  # hist plot data

	while True:  # whatever you are gonna do

		sleep(.1)

		# compute some values
		msg_1 = np.random.uniform(0,1,5*5)


		msg_3 = np.roll(msg_3, -1)
		if    msg_3[-2] < 0.1: msg_3[-1] = msg_3[-2] + .1
		elif  msg_3[-2] > 0.9: msg_3[-1] = msg_3[-2] - .1
		else: msg_3[-1] = msg_3[-2] + np.random.uniform(-.1,.1)

		msg_4 = np.random.uniform(0.4,1,3)

		# Prepare the array format in sender function
		sender( '1.0', msg_1 )
		sender( '2.0', [msg_2[counter%4]] )
		sender( '3.0', msg_3 )
		sender( '4.0', msg_4 )

		counter += 1

if __name__ == '__main__':
	main()