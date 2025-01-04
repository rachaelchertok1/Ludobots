import pybullet as p
import time

t = 1/60
physicsClient = p.connect(p.GUI)

#Tells pybullet to read in the world described in box.sdf (which was created in generate.py)
p.loadSDF("box.sdf")
for i in range(0,1000):
    print("Iteration: ", i)
    time.sleep(t)
    p.stepSimulation()
p.disconnect()