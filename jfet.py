class Jfet:
    id=float
    idss=float
    vgs=float
    vp=float
    gm=float
    gmo=float
       
    def __init__(self,id,idss,vgs,vp,gm,gmo):
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
        
        