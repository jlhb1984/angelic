from ci import Ci

class lm555:
    f=float
    ra=float
    rb=float
    c=float

def __init__(self,analog,digital,f,ra,rb,c):
    self.analog=analog
    self.digital=digital
    self.f=f
    self.ra=ra
    self.rb=rb
    self.c=c

def calculate_parameters_lm555(f,ra,rb,c):
    f=1/((ra*(ra+rb))*c)


