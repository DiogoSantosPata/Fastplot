import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "fastplot",
    version = "0.0.1",
    author = "Diogo Santos-Pata",
    author_email = "diogo.santos.pata@gmail.com",
    description = ("Fast and real-time plotting in Python is still far from being achieved. fastplot takes advantage of the rendering capabilities of modern web-browsers and Javascript to quickly update visualisations.  Get the best of both worlds: Python to compute, JavaScript to render.  As you can see this package its still in early stage.... please help :) " ),
    url = "https://github.com/DiogoSantosPata/Fast_Plot_Python_in_the_Browser",
    packages=['fastplot'],
    long_description=read('README'),
)