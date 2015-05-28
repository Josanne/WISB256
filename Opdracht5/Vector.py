import math

class Vector():
    vector = []
    
    
    def __init__(self,n,vector=0):
        if type(vector) == list:
            self.vector = vector
        else:
            self.vector = [vector]*n

    def __str__(self):
        string = ""
        
        for x in self.vector:
            string += str(x) + '\n'
        return string
        
    def lincomb(self,other,alpha,beta):
        w = []
        #alpha*self+beta*other
        for i in range(len(other.vector)):
            x = alpha*self.vector[i]+beta*other.vector[i]
            w.append(x)
        return Vector(len(w), w)
        
    def scalar(self,alpha):
        return self.lincomb(self, alpha ,0)
        
    def inner(self,other):
        y = 0
        for i in range(len(self.vector)):
            x = self.vector[i] * other.vector[i]
            y += x
        return y
    
    def norm(self):
        return math.sqrt(self.inner(self))
