#!/usr/bin/env python
# coding: utf-8

# # Homework Assignment 2
# 
# You will be analyzing an xyz file for water (water.xyz) and measuring the distances between all the atoms in the molecule.  The file is located in the data folder of your workshop materials. The output of your code should look like this.
# 
# ```
# O to O : 0.0
# O to H1 : 0.969
# O to H2 : 0.969
# H1 to O : 0.969
# H1 to H1 : 0.0
# H1 to H2 : 1.527
# H2 to O : 0.969
# H2 to H1 : 1.527
# H2 to H2 : 0.0
# ```
# To do this you will need to use the distance formula.
# 
# $$distance = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2 + (z_1 - z_2)^2}$$
# 
# As you can see that you will need to square stuff and take the square root.  To take the square root, you will use a function from numpy, `numpy.sqrt()`.  To square something, use `**` notation.  As in, `3**2 = 9` is $3^2 =9$.

import os
import numpy
import argparse

def calculate_distance(coords1,coords2):
    x_distance = coords1[0] - coords2[0]
    y_distance = coords1[1] - coords2[1]
    z_distance = coords1[2] - coords2[2]
    distance = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return distance

def bond_check(atom_distance, min_length=0, max_length=1.5):
    """
    Checks if a distance is a bond based on a minimum and maximum
    Inputs: distance, minimum length for bond, maximum length for bond
    Defaults: minimum: 0 angstroms, maximum: 1.5 angstroms
    """
    if atom_distance > min_length and atom_distance < max_length:
        return True
    else:
        return False

def open_xyz(filename):
    """
    This function opens a standard xyz file.
    It returns the symbols as strings and the coordinates as floats.
    """
    xyz_file = numpy.genfromtxt(fname=filename, dtype='unicode', skip_header=2)
    symbols = xyz_file[:,0]
    coords = xyz_file[:,1:]
    coords = coords.astype(float)
    return symbols, coords

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="This script analyzes a user given xyz file and outputs the lengths of all the bonds.")
	parser.add_argument('xyz_file', help='The filepath of the xyz file to analyze.')
	args = parser.parse_args()
	
	file_location = args.xyz_file
	symbols, coordinates = open_xyz(file_location)
	
	#print(calculate_distance(coordinates[0],coordinates[1]))
	num_atoms = len(symbols)
	for num1 in range(0,num_atoms):
	    for num2 in range(0,num_atoms):
	        if num1<num2:
	            distance=calculate_distance(coordinates[num1],coordinates[num2])
	            if bond_check(distance) is True:
	                print(F'{symbols[num1]} to {symbols[num2]} : {distance:.3f}')


# In[ ]:




