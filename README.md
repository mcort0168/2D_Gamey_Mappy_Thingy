# 2d_text_map

## Introduction
This program is run in python and uses several aspects from the pygame library and it's modules to convert a regular txt file into a 2d pixel map using specified characters and then create an interactive map between these pixels and a character and enemies if desired.

##Process:
1. First you must have a txt file created using the following variables seperated by commmas:
  * g = grass
  * s = sand 
  * d = dirt 
  * c = cement 
  * n = snow and 
  * x = empty space used to either end the line or indent the map properly.
  * w = wall and makes up a list of pixels the character cannot go over thus is a boundary.
 2. After the program opens, reads, and then splits the file up it converts every letter into a 16 by 16 pixel terrain image and creates the map based off those pixels.
 3. It then goes through the player, wall and monster classes to ensure if the player collides witha  wall it cannot go through it and if the player pixel comes into contact with the monster pixels it stops at them and every moment of contact does damage to the player and monster. Once the monsters health drops to 0 it disappears.
 4. However if the player dies the window automatically closes and then Prints out a string of test informing the player they died and to try again.
 5. The last part of this code executes the commands needed to display the pixels, character, monsters, walls and key commands for what to do when a key is pressed in a while loop.
 
 ## Purpose
 The reason this code was created was both as a project and for fun. Creating things is always such an exhilerating experience and using this format creating simeple game maps is quite easy now if you know some pyhton basics. If not hey there's always google.
 
 ### special notes
 Just to reiterate pygame is necessary to run this code.
 An enemy spreadsheet has been included as well if you want to change or add more enemies you only need to clip them at 16 by 16 pixels and save them. Make sure their backgrounds are transparent.
 
 ###Thank you for playing and have fun bumping into blocks!
