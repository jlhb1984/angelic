from math import pi

class Circuit:
    n=int
    rserial=float
    rparallel=float
    ra=float
    rb=float
    rc=float
    r1=float
    r2=float
    r3=float
    l=float
    c=float
    flc=float
    lc=float
    f=float
    xcl=float
    vo=float
    vs=float
    
    def __init__(self,n,rserial,rparallel,ra,rb,rc,r1,r2,r3,l,c,flc,lc,f,xcl,r4,rxhay,lxhay,rxmax,lxmax,vo,vs):
        self.n=n
        self.rserial=rserial
        self.rparallel=rparallel
        self.ra=ra
        self.rb=rb
        self.rc=rc
        self.r1=r1
        self.r2=r2
        self.r3=r3
        self.l=l
        self.c=c
        self.flc=flc
        self.lc=lc
        self.f=f
        self.xcl=xcl
        self.r4=r4
        self.rxhay=rxhay
        self.lxhay=lxhay
        self.rxmax=rxmax
        self.lxmax=lxmax
        self.vo=vo
        self.vs=vs      
        
    def calculate_resistances_addition(n):
        rserial=0
        rparallelaux=0
        
        for i in range(0,n,1):
            r=float(input("Type R value: "))
            rserial=rserial+r 
            rparallelaux=rparallelaux+1/r
        rparallel=1/rparallelaux
        circuit_radd=Circuit(n,rserial,rparallel,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
        print(vars(circuit_radd))
        
    def calculate_dy(ra,rb,rc):
         r1=(ra*rb)/(ra+rb+rc)
         r2=(rb*rc)/(ra+rb+rc)
         r3=(ra*rc)/(ra+rb+rc)
         circuitdy=Circuit(0,0,0,ra,rb,rc,r1,r2,r3,0,0,0,0,0,0,0,0,0,0,0,0,0)
         print(vars(circuitdy))
         
    def calculate_yd(r1,r2,r3):
        ra=(r1*r2+r2*r3+r3*r1)/r1
        rb=(r1*r2+r2*r3+r3*r1)/r2
        rc=(r1*r2+r2*r3+r3*r1)/r3
        circuityd=Circuit(0,0,0,ra,rb,rc,r1,r2,r3,0,0,0,0,0,0,0,0,0,0,0,0,0)
        print(vars(circuityd)) 
        
    def calculate_flc(l,c):
        flc=(1/(2*pi))*((1/(l*c))**(0.5)) 
        circuit_flc=Circuit(0,0,0,0,0,0,0,0,0,l,c,flc,0,0,0,0,0,0,0,0,0,0)
        print(vars(circuit_flc))
    
    def calculate_loc(lc,f):
        xcl=1/(4*(pi**2)*(f**2)*lc)
        circuit_loc=Circuit(0,0,0,0,0,0,0,0,0,0,0,0,lc,f,xcl,0,0,0,0,0,0,0)
        print(vars(circuit_loc))
    
    def calculate_hmax(r1,r2,r3,r4,c,w):
        rxhay=(r2*r4*(w**2)*r1*(c**2))/(1+(r1**2)*(w**2)*(c**2))
        lxhay=(r2*r4*c)/(1+(r1*w*c)**2)
        rxmax=(r4*r2)/r1
        lxmax=r4*r2*c
        circuit_hmax=Circuit(0,0,0,0,0,0,r1,r2,r3,0,c,0,0,0,0,r4,rxhay,lxhay,rxmax,lxmax,0,0)
        print(vars(circuit_hmax))
         
    def calculate_divisor(vs,ra,rb):
        vo=(rb*vs)/(ra+rb)
        print(vo)
        divisor1=Circuit(0,0,0,ra,rb,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,vo,vs)
        print(vars(divisor1))