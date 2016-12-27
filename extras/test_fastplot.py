from fastplot import fastplot as fp
import numpy as np
from time import sleep

def main():

	while True:  # whatever you are gonna do

		sleep(.1)

		# compute some values
		msg_1 = np.random.uniform(0,1,30)
		msg_2 = np.random.uniform(0,1,(10,10))
		msg_3 = np.random.uniform(0.4,1,20)

		# use fastplot to plot those values in the browser...
		fp.plot( 'Example of line plot', msg_1 )
		fp.pcolor( 'Example of pcolor', msg_2 )
		fp.barplot( 'Example of line barplot', msg_3 )

if __name__ == '__main__':
	main()
