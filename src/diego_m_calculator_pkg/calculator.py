

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import re


def handle_special_notations(function:str):
    #replace ^ with ** for exponentiation
    function = function.replace('^','**')
    #replace : with / for division
    function = function.replace(':','/')
    #replace blank spaces between number and () or number and x with * or x and number or () with *
    pattern_1 = r'([0-9x])\s*([x\(\w])'
    function = re.sub(pattern_1, r'\1*\2', function)
    pattern_2 = r'([x\)])\s*([0-9x])'
    function = re.sub(pattern_2, r'\1*\2', function)
    pattern_3 = r'(\))\s*(\()'
    function = re.sub(pattern_3, r'\1*\2', function)
    #get left side of the equation if it has a y
    if 'y' in function:
        function = function.split('=')[1].strip()
    else:
        function = function.strip()
    return function

def generate_plot_data(function:str, x_range:tuple=(-10,10), step:float=0.1):
    function = handle_special_notations(function)

    #list of x vals
    x_vals = np.arange(x_range[0],x_range[1], step)

    x = sp.symbols('x')
    f = sp.sympify(function)
    #convert to numpy expression
    f = sp.lambdify(x,f,"numpy")

    #calculate y_vals
    y_vals = f(x_vals)

    return x_vals, y_vals
    

def draw_graph(function:str, x_range:tuple=(-10,10), step:float=0.1, color:str = 'blue'):
    function = handle_special_notations(function)

    #generate x and y vals
    x_vals, y_vals = generate_plot_data(function, x_range, step)
    #draw the graph
    plt.figure()
    plt.plot(x_vals, y_vals, color=color)
    plt.show()


