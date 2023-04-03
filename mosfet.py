from transistor import Transistor

class Mosfet(Transistor):
    idon=float
    vgson=float
    vgsth=float
    vgs=float
    k=float
    gm=float
    id=float
    
    def __init__(self,bjt,fetemp,fetenr,idon,vgson,vgsth,vgs,k,gm,id):
        super().__init__(bjt,fetemp,fetenr)
        self.ideon=idon
        self.vgson=vgson
        self.vgsth=vgsth
        self.vgs=vgs
        self.k=k
        self.gm=gm
        self.id=id
        
    def calculate_parameters_mosfet(idon,vgson,vgsth,vgs):
        k=idon/((vgson-vgsth)**2)
        gm=2*k*(vgs-vgsth)
        id=k*(vgs-vgsth)**2
        mosfet1=Mosfet(idon,vgson,vgsth,vgs,k,gm,id)
        print(vars(mosfet1))
        
        
        
        
    
        
        