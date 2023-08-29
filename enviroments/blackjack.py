import gym
from gym import spaces
from gym.utils import seeding

sdkjafsldfkjasldfj

dlladkflas
#TODO: averiguar que hace cmp method.
def cmp(a,b):
    return int(a>b) - int(a<b)

#cards
cardsValue = [1,2,3,4,5,6,7,8,9,10,10,10,10]

def selectCard(randomNumpy):
    return randomNumpy.choice(cardsValue)

def selectHand(randomNumpy):
    return [selectHand(randomNumpy),selectCard(randomNumpy)]

def ace(hand): 
    return 1  in hand  and sum(hand) + 10 <= 21

def sumHand(hand):
    if ace(hand):
        return sum(hand) + 10
    return sum(hand)

def passed(hand): #is this hand over 21?
    return sumHand(hand) > 21

def score(hand):
    return 0 if passed(hand) else sumHand(hand)

def isNormal(hand):
    return sorted(hand) == [1,10]

class BlackjackEnv(gym.Env):
    """
    Blackjack enviroment
    #TODO: add description
    """
    def __init__(self,normal=False):
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Tuple((
            spaces.Discrete(32),
            spaces.Discrete(11),
            spaces.Discrete(2)
        ))
        self.seed()

        self.normal = normal

        #first game
        self.reset()
        self.nA = 2


    def reset(self):
        return  self.reset()
    
    def step(self, action):
        return self.step(action)
    
    def seed(self,_seed=None):
        self.randomNumpy,  seed = seeding.np_random(seed)
        return [seed]
