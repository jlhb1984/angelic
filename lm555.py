from ci import Ci

class Lm555(Ci):
    analog=bool
    digital=bool
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

    def calculate_parameters_lm555(ra,rb,c):
        f=1/((1.44*(ra+2*rb))*c)
        lm5551=Lm555(False,True,f,ra,rb,c)
        print(vars(lm5551))


