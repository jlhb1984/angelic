from circuit import Circuit

class Divisor(Circuit):
    vo=float
    vs=float
    
    #Aquí van todos los valores de la subclase divisor.    
    def __init__(self,n,rserial,rparallel,ra,rb,rc,r1,r2,r3,l,c,flc,lc,f,xcl,r4,rxhay,lxhay,rxmax,lxmax,vo,vs):
        #Aquí van toos las variables de la superclase circuit.
        super().__init__(n,rserial,rparallel,ra,rb,rc,r1,r2,r3,l,c,flc,lc,f,xcl,r4,rxhay,lxhay,rxmax,lxmax)       
        #Inicializo las variables de la subclase.
        self.vo=vo
        self.vs=vs
    
    def calculate_divisor(vs,ra,rb):
        vo=(rb*vs)/(ra+rb)
        print(vo)
        divisor1=Divisor(0,0,0,ra,rb,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,vo,vs)
        print(vars(divisor1))