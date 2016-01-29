
from __future__ import division
import numpy as np
from pysd import functions

def time():
    return _t

def lookup_function_call():
    """
    
    """
    loc_dimension_dir = 0 
    output = lookup_function_table(time())

    return output

def rate():
    """
    
    """
    loc_dimension_dir = 0 
    output = lookup_function_call()

    return output

def accumulation():
    return _state['accumulation']

def _accumulation_init():
    try:
        loc_dimension_dir = accumulation.dimension_dir
    except:
        loc_dimension_dir = 0
    return 0

def _daccumulation_dt():
    try:
        loc_dimension_dir = accumulation.dimension_dir
    except:
        loc_dimension_dir = 0
    return rate()

def lookup_function_table(x):
    return functions.lookup(x,
                            lookup_function_table.xs,
                            lookup_function_table.ys)

lookup_function_table.xs = [0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0]
lookup_function_table.ys = [0.0, 0.0, 1.0, 1.0, 0.0, 0.0, -1.0, -1.0, 0.0, 0.0]

def final_time():
    """
    
    """
    loc_dimension_dir = 0 
    output = 45

    return output

def initial_time():
    """
    
    """
    loc_dimension_dir = 0 
    output = 0

    return output

def saveper():
    """
    
    """
    loc_dimension_dir = 0 
    output = time_step()

    return output

def time_step():
    """
    
    """
    loc_dimension_dir = 0 
    output = 0.25

    return output
