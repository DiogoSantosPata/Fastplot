<font face="Verdana" size="3" color="black">

<h1>Fast_Plot_Python_in_the_Browser</h1>
<h3>fastplot</h3>

<p align="left|right|center|justify">
Fast and real-time plotting in Python is still far from being achieved. <br>
fastplot takes advantage of the rendering capabilities of modern web-browsers and Javascript to quickly update visualisations.  <br>
Get the best of both worlds: Python to compute, JavaScript to render. <br>
As you can see this package its still in early stage.... please help :) <br>
Author: Diogo Santos-Pata, 2016 <br>
</p>

<img src="FastPlot.png" width="300" height="600">

<h1>How to use it: </h1>
<p>

From your console type: 

<li> <i>python web_viz_udp.py </i> </li> <br> 

That will setup a Tornado server to communicate between python and javascript.  <br>

Next, open in your favourite browser: <br>

<li> <i> index.html </i> </li>  <br>

Now, you are all set to let your python script perform its crazy computations and all you need to do to 
plot data is to call the <i>sender()</i> function.
To see it in action right away, try to run: <li> <i>main.py </i> </li> 

</p>

<h3>Dependencies:</h3>
<li>  <a href="http://www.tornadoweb.org/en/stable/"> Tornado</a>  </li>
<li>  <a href="https://docs.python.org/2/library/socket.html"> Socket</a>  </li>
