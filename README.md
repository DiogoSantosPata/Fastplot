<font face="Verdana" size="3" color="black">
<h1>Fastplot</h1>

<p align="left|right|center|justify">
Fast and real-time plotting in Python is still far from being achieved. <br>
fastplot takes advantage of the rendering capabilities of modern web-browsers and Javascript to quickly update visualisations.  <br>
Get the best of both worlds: Python to compute, JavaScript to render. <br>
As you can see this package its still in early stage.... please help :) <br>
</p>

<img src="FastPlot.png" width="150" height="300">

<h1>How to install it: </h1>
<h4>Set server</h4>

<li>Open a terminal window </li>
<li>Go to ('cd') the <i>fastplot</i> directory you downloaded</li>
<li>Go to ('cd') the <i>fastplot_server</i> directory</li>
<li> Type: `sudo chmod 755 fastplot` </li>
<li>Open the .profile file by typing: `nano .profile` </li>
<li>At the end of the file paste: `export PATH="$your/path/folder/here/fastplot_server:$PATH"`  (make sure to set the correct path)</li> 

<li>Save the .profile file, exit, and type `source .profile`  </li> 

Now you should be able to execute the `fastplot` command everywhere in your machine and see the message: <br>
`Running fastplot server...`


<h4>Install fastplot python library</h4>

<p>
<li>Go back to ('cd') the <i>fastplot</i> directory you downloaded</li>
<li>Type: `sudo python setup.py install`  </li>
If all goes well, you should see something like: <br>
</p>
```
Installed /Library/Python/2.7/site-packages/fastplot-0.0.1-py2.7.egg
Processing dependencies for fastplot==0.0.1
Finished processing dependencies for fastplot==0.0.1
```
:+1:







<h1>How to use it: </h1>

1. From your console type `fastplot` in order to run the server
2. Now you are free to run your python script using the `fastplot` library

<h5>An example of a minimal python script:</h5>
```
import fastplot
import numpy as np

while True:  # whatever you are gonna do

	# compute some values
	msg_1 = np.random.uniform(0,1,30)
	msg_2 = np.random.uniform(0,1,(10,10))
	msg_3 = np.random.uniform(0.4,1,20)

	# use fastplot to plot those values in the browser...
	fastplot.plot( 'Example of line plot', msg_1 )
	fastplot.pcolor( 'Example of pcolor', msg_2 )
	fastplot.barplot( 'Example of line barplot', msg_3 )
```



<h3>Dependencies:</h3>
<li>  <a href="http://www.tornadoweb.org/en/stable/"> Tornado</a>  </li>
<li>  <a href="https://docs.python.org/2/library/socket.html"> Socket</a>  </li>
