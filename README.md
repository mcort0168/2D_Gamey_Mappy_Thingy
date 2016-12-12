# 2d_text_map

## Introduction
This program is run in python and uses several aspects from the pygame library and it's modules to convert a regular txt file into a 2d pixel map.

##Process:
1. First you must have atxt file created using the following variables seperated by commmas:
..* g = grass
..* s = sand 
..* d = dirt 
..* c = cement 
..* n = snow and 
..* x = empty space used to either end the line or indent the map properly.
A special letter is w which equals a wall. When the program reads this variable it understands that the character pixel cannot go over this pixel and cannot go any further in that direction.
