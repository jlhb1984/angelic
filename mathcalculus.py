from math import pi,atan,cos,sin

class Mathcalculus:
    gradeang=float
    radang=float
    xvalue=float
    yvalue=float
    amp=float
    phase=float
    a=float
    b=float
    c=float
    x1=float
    x2=float
            
    def __init__(self,gradeang,radang,xvalue,yvalue,amp,phase,a,b,c,x1,x2):
        self.gradeang=gradeang
        self.radang=radang
        self.xvalue=xvalue
        self.yvalue=yvalue
        self.amp=amp
        self.phase=phase
        self.a=a
        self.b=b
        self.c=c
        self.x1=x1
        self.x2=x2
        
    def calculate_rads(gradeang):
        radang=(gradeang*pi)/180
        rads=Mathcalculus(gradeang,radang,0,0,0,0,0,0,0,0,0)
        print(vars(rads))
        
    def calculate_grades(radang):
        gradeang=radang*(180/pi)
        grades=Mathcalculus(gradeang,radang,0,0,0,0,0,0,0,0,0)
        print(vars(grades))
        
    def calculate_pol(xvalue,yvalue):
        amp=(xvalue**2+yvalue**2)**(0.5)
        phase=atan(yvalue/xvalue)
        pol=Mathcalculus(0,0,xvalue,yvalue,amp,phase,0,0,0,0,0)
        print(vars(pol))
    
    def calculate_rec(amp,phase):
        xvalue=amp*cos(phase)
        yvalue=amp*sin(phase)
        rec=Mathcalculus(0,0,xvalue,yvalue,amp,phase,0,0,0,0,0)
        print(vars(rec))
    
    def calculate_roots(a,b,c):
        x1=(-b+(b**2-4*a*c)**(0.5))/(2*a)
        x2=(-b-(b**2-4*a*c)**(0.5))/(2*a)
        roots=Mathcalculus(0,0,0,0,0,0,a,b,c,x1,x2)
        print(vars(roots))