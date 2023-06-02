import io
import numpy as np
import sys
from gym.envs.toy_text import discrete

""" Actions """
UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

class GridWorldEnv(discrete.DiscreteEnv):
    """
    This is the gridworld enviroment from  Sutton's Reinforcement Learning book
    it consist on a grid of MxN with terminal states at the top left and botton right corner

    Example

    T o o o
    o o o o
    o x o o
    o o o T

    where:

    x: your position
    T: terminal state

    """

    metadata = {'render.modes': ['human', 'ansi']}

    def __init__(self, shape=[4,4]):

        if not isinstance(shape,(list,tuple)) or not len(shape) == 2:
            raise ValueError('shape argument must be a list/tuple of length 2')

        self.shape = shape
        
        nS = np.prod(shape)
        nA = 4

        MAX_Y = shape[0]
        MAX_X = shape[1]

        # it represent the dynamics of the Markov descition process
        P = {}
        #world
        grid = np.arange(nS).reshape(shape)
        # array iterator
        player = np.nditer(grid, flags=['multi_index'])


        while not player.finished:
            s = player.iterindex
            y,x = player.multi_index #position of the player

            P[s] = {a:  [] for a in range(nA)}

            done = lambda s: s == 0 or s == (nS - 1)
            reward  = 0.0 if done(s) else -1.0

            #in the terminal state
            if done(s):
                P[s][UP] = [(1.0, s, reward, True)]
                P[s][RIGHT] = [(1.0, s, reward, True)]
                P[s][DOWN] = [(1.0, s, reward, True)]
                P[s][LEFT] = [(1.0, s, reward, True)]
            else:
                number_state_up = s if y == 0 else s - MAX_X
                number_state_right = s if x == (MAX_X - 1) else s + 1
                number_state_down = s if y == (MAX_Y - 1) else s + MAX_X
                number_state_left = s if x == 0 else s - 1
                P[s][UP] = [(1.0, number_state_up, reward, done(number_state_up))]
                P[s][RIGHT] = [(1.0, number_state_right, reward, done(number_state_right))]
                P[s][DOWN] = [(1.0, number_state_down, reward, done(number_state_down))]
                P[s][LEFT] = [(1.0, number_state_left, reward, done(number_state_left))]

            player.iternext()
            
        # We expose the model of the environment for educational purposes
        # This should not be used in any model-free learning algorithm
        self.P = P
        # Initial state distribution is uniform
        isd = np.ones(nS) / nS

        super(GridWorldEnv, self).__init__(nS,nA,P,isd)
        
    def render(self,mode='human',close=False):
        """ render the gridWorld for visualization """
        if close:
            return
            

        renderingFile = io.StringIO() if mode == 'ansi' else sys.stdout

        grid = np.arange(self.nS).reshape(self.shape)
        player = np.nditer(grid, flags=['multi_index'])

        while not player.finished:
            s = player.iterindex
            y,x = player.multi_index

            if self.s == s:
                rendering = " X "
            elif s == 0 or s == self.nS - 1:
                rendering = " T "
            else:
                rendering = " o "
            if x == 0:
                rendering = rendering.lstrip()
            if x == self.shape[1] - 1:
                rendering  = rendering.rstrip()

            renderingFile.write(rendering)

            if x == self.shape[1] - 1:
                renderingFile.write("\n")

            player.iternext()
