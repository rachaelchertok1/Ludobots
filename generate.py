#This file alters what is in the world
import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("box.sdf")

length = 1
width = 2
height = 3

x = 0
y = 0
z = 1.5
#Stores a box with initial position x=0, y=0, z=0
pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length,width,height])

#tells pyrosim to close the sdf file
pyrosim.End() 

