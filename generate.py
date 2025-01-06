#This file alters what is in the world
import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")

length = 0.9
width = 0.9
height = 0.9

x = 0
y = 0
z = 0.5


#Cube tower size 5x5x10 (5 rows by 5 cols each with 10 cubes)
for j in range(0, 5):
       
    for k in range(0,5):
            
        for i in range(0,10):
            #Stores a box with initial position x=0, y=0, z=0
            pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length,width,height])
            z+=1
            length = length * 0.9
            width = width * 0.9
            height = height * 0.9
        length = 0.9
        width = 0.9
        height = 0.9
        x += 1
    x = 0
    y += 1
    
    
    

#tells pyrosim to close the sdf file
pyrosim.End() 

