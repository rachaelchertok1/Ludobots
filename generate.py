#This file alters what is in the world
import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5


for i in range(0,10):
    #Stores a box with initial position x=0, y=0, z=0
    pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length,width,height])
    z+=1
    length = length * 0.9
    width = width * 0.9
    height = height * 0.9
    

#tells pyrosim to close the sdf file
pyrosim.End() 

