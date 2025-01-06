#This file alters what is in the world
import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("world.sdf")

length = 0.9
width = 0.9
height = 0.9

x = 0
y = 0
z = 0.5

pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length,width,height])

    
    

#tells pyrosim to close the sdf file
pyrosim.End() 

