#This file alters what is in the world
import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5

'''
x_box1 = 0
y_box1 = 0
z_box1 = 0.5

x_box2 = 0
y_box2 = 0
z_box2 = 1.5
'''

for i in range(0,10):
    #Stores a box with initial position x=0, y=0, z=0
    pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length,width,height])
    z+=1
    

#pyrosim.Send_Cube(name="Box2", pos=[x_box2,y_box2, z_box2], size=[length,width,height])

#tells pyrosim to close the sdf file
pyrosim.End() 

