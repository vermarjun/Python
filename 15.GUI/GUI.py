from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from IPython.display import display
w = widgets.IntSlider()

display(w)

def func(x):
    return x

# interact(func, x=10)