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

<h1>How to install it: </h1>
<h4>Set server</h4>
<p>
<li>Open a terminal window </li>
<li>Go to ('cd') the <i>fastplot</i> directory you downloaded</li>
<li>Go to ('cd') the <i>fastplot_server</i> directory</li>
<li>Type: <it>sudo chmod 755 fastplot</it> </li>
<li>Open the .profile file by typing: nano .profile </li>
<li>At the end of the file paste: <i>export PATH="$your/path/folder/here/fastplot_server:$PATH" </i> (make sure to set the correct path)</li> 

<li>Save the .profile file, exit, and type <i> source .profile </i>  </li> 

Now you should be able to execute the 'fastplot' command everywhere in your machine and see the message: <br>
Running fastplot server...
</p>

<h4>Install fastplot python library</h4>

<p>
<li>Go back to ('cd') the <i>fastplot</i> directory you downloaded</li>
<li>Type: <i>sudo python setup.py install</i>  </li>
If all goes well, you should see something like: <br>
<i>
Installed /Library/Python/2.7/site-packages/fastplot-0.0.1-py2.7.egg <br>
Processing dependencies for fastplot==0.0.1 <br>
Finished processing dependencies for fastplot==0.0.1 <br>
</i>
:+1:
</p>






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
