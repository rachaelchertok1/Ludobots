import pybullet as p
import time

t = 1/60
physicsClient = p.connect(p.GUI)
for i in range(0,1000):
    print("Iteration: ", i)
    time.sleep(t)
    p.stepSimulation()
p.disconnect()