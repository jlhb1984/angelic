from math import exp,sin,cos,pi,atan

class Controller:
    cita2=float
    ts2=float
    wn2=float
    wd2=float
    tp2=float
    beta2=float
    tr2=float
    mp2=float
    cita5=float
    ts5=float
    wn5=float
    wd5=float
    tp5=float
    beta5=float
    tr5=float
    mp5=float
    
    def __init__(self,cita2,ts2,wn2,wd2,tp2,beta2,tr2,mp2,cita5,ts5,wn5,wd5,tp5,beta5,tr5,mp5):
        self.cita2=cita2
        self.ts2=ts2
        self.wn2=wn2
        self.wd2=wd2
        self.tp2=tp2
        self.beta2=beta2
        self.tr2=tr2
        self.mp2=mp2
        self.cita5=cita5
        self.ts5=ts5
        self.wn5=wn5
        self.wd5=wd5
        self.tp5=tp5
        self.beta5=beta5
        self.tr5=tr5
        self.mp5=mp5
        
    def calculate_controller(cita,ts):
        wn2=(4/(cita*ts))
        root=(1-cita**2)**(0.5)
        wd2=wn2*root
        tp2=pi/wd2
        beta2=atan(root/(cita))
        tr2=(pi-beta2)/wd2
        mp2=1-exp((-1)*cita*wn2*tp2)*sin(beta2+wd2*tp2)
        cita2=cita
        ts2=ts
        
        controller2=Controller(cita2,ts2,wn2,wd2,tp2,beta2,tr2,mp2,0,0,0,0,0,0,0,0)
        print(vars(controller2))
        
        wn5=(3/(cita*ts))
        root=(1-cita**2)**(0.5)
        wd5=wn5*root
        tp5=pi/wd5
        beta5=atan(root/(cita))
        tr5=(pi-beta5)/wd5
        mp5=1-exp((-1)*cita*wn5*tp5)*sin(beta5+wd5*tp5)
        cita5=cita
        ts5=ts
        controller5=Controller(0,0,0,0,0,0,0,0,cita5,ts5,wn5,wd5,tp5,beta5,tr5,mp5)
        print(vars(controller5))
        
        