# File_organizer
My very first project on python, a simple file organizer to make life easier when dealing with unorganized folders.

The repository contains : 

file organizer script which is a jupyter notebook

"Files" folder, which is an example folder with some different type files (img,texts,audio)

addfile.py which is an alternative script that you can use from the command prompt to run same process of file organizer but on a single file
 
##File organizer

Two main functions : 
                    
First, it creates folders (if not already present) based on files extension on a specific path (you can copy past the path on "directory" variable or simply remove "Files" from directory variable and placing the notebook wherever is needed.

Second, it moves all files on relative folders and report every movement on a csv file indicating name,type,size. 

An additional and optional script is below in the code, it gets information from the image folder, transform images in numpy arrays and create a tabulate reporting mean value of greyscale, RGB or RGBA pixels.


