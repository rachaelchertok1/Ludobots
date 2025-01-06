#This file alters how the world is simulated
import pybullet as p
import pybullet_data
import time

t = 1/60
physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

#Setting up gravity in the world
p.setGravity(0,0,-9.8)

#Adding a floor
planeId = p.loadURDF("plane.urdf")

#Tells pybullet to read in the world described in box.sdf (which was created in generate.py)
p.loadSDF("boxes.sdf")
for i in range(0,2000):
    print("Iteration: ", i)
    time.sleep(t)
    p.stepSimulation()
p.disconnect()