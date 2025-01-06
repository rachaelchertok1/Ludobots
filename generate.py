#This file alters what is in the world
import pyrosim.pyrosim as pyrosim


    


def Create_World():
    pyrosim.Start_SDF("world.sdf")

    length = 1
    width = 1
    height = 1
    
    x = 2
    y = 2
    z = 0.5

    pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length,width,height])

    #tells pyrosim to close the sdf file
    pyrosim.End() 
   
def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    
    length = 1
    width = 1
    height = 1

    x = 0
    y = 0
    z = 0.5
    
    pyrosim.Send_Cube(name="Torso", pos=[x,y,z], size=[length,width,height])
    pyrosim.End()

def main():
    Create_World()
    Create_Robot()
    
if __name__ == "__main__":
    main()
    

    

