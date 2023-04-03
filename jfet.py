from transistor import Transistor

class Jfet(Transistor):
    id=float
    idss=float
    vgs=float
    vp=float
    gm=float
    gmo=float
       
    def __init__(self,bjt,fetemp,fetenr,id,idss,vgs,vp,gm,gmo):
        super().__init__(bjt,fetemp,fetenr)
        self.id=id
        self.idss=idss
        self.vgs=vgs
        self.vp=vp
        self.gm=gm
        self.gmo=gmo
                
    def calculate_parameters_jfet(idss,vgs,vp):
        id=idss*((1-vgs/vp)**2)
        gmo=(2*idss)/(vp)
        gm=gmo*(1-vgs/vp)
        jfet1=Jfet(id,idss,vgs,vp,gm,gmo)
        print(vars(jfet1))
        
        