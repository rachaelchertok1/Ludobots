import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("box.sdf")

#Stores a box with initial position x=0, y=0, z=0.5
pyrosim.Send_Cube(name="Box", pos=[0,0,0.5], size=[1,1,1])

#tells pyrosim to close the sdf file
pyrosim.End() 

