from scipy.integrate import odeint
from numpy import arange
import random
class Lorenz():

    def __init__(self, y0, sigma=10,rho=28,beta=8/3):
        self.y0 = y0 
        self.sigma = sigma
        self.rho = rho
        self.beta = beta
        
    def solve(self,T,dt):
        t = arange(0,T,dt)
            
        
        return odeint(self.func, self.y0, t)
    
    def func(self,old,t):
        newx = self.sigma*(old[1]-old[0])
        newy = old[0]*(self.rho-old[2])-old[1]
        newz = old[0]*old[1]-self.beta*old[2] 
        return [newx, newy, newz]
