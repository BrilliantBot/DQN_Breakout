import gym
import random
import matplotlib.pyplot as plt

"""Create our environment. Basically we define what game we want to play"""
env = gym.make('BreakoutDeterministic-v4')

"""Reset our environment, notice it returns the first frame of the game"""
first_frame = env.reset()
plt.imshow(first_frame)

"""Now we can take actions using the env.step function. In breakout the actions are:
    0 = Stay Still
    1 = Start Game/Shoot Ball
    2 = Move Right
    3 = Move Left"""
    
"""I start the game by step(1), then receive the next frame, reward, done, and info"""
next_frame, next_frames_reward, next_state_terminal, info = env.step(1)
plt.imshow(next_frame)
print('Reward Recieved = ' + str(next_frames_reward))
print('Next state is a terminal state: ' + str(next_state_terminal))
print('info[ale.lives] tells us how many lives we have. Lives: ' + str(info['ale.lives']))

"""Now lets take a bunch of random actions and watch the gameplay using render.
If the game ends we will reset it using env.reset"""

for i in range(10000):
    a = random.sample([0,1,2,3] , 1)[0]
    f_p,r,d,info = env.step(a)
    env.render()
    if d == True:
        env.reset()
        
"""And thats it. Let's head back to brilliantbot.org to make this agent an expert at Breakout!"""