import gym
import gym_gazebo
import time
import random

env = gym.make('MARATop3DOFROS2-v0')

for i in range(100):
    env.reset()
    for _ in range(50):
        # take a random action
        print("Ep: "+ str(i) + " Step: " + str(_))
        observation, reward, done, info = env.step(env.action_space.sample())