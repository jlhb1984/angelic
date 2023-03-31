from math import exp,log

class Diode:
    idiode=float
    isinv=float
    vd=float
    n=float
    temp=float
    vt=float
    
    def __init__(self,idiode,isinv,vd,n,temp,vt):
        self.idiode=idiode
        self.isinv=isinv
        self.vd=vd
        self.n=n
        self.temp=temp
        self.vt=vt
        
    def calculate_id(isinvaux,vd,n,temp):
        vt=((1.38*(10**(-23)))*temp)/(1.6*(10**(-19)))
        isinv=isinvaux*(10**(-12))
        idiode=isinv*(exp(vd/(n*vt))-1)
        print(idiode)
        diode_id=Diode(idiode,isinv,vd,n,temp,vt)
        print(vars(diode_id))
        
    def calculate_is(idiode,vd,n,temp):
        vt=((1.38*(10**(-23)))*temp)/(1.6*(10**(-19)))
        isinv=(idiode/(exp(vd/(n*vt))-1))
        diode_is=Diode(idiode,isinv,vd,n,temp,vt)
        print(vars(diode_is))
        
    def calculate_vt(idiode,isinvaux,vd,n):
        isinv=isinvaux*(10**(-12))
        vt=vd/(log(idiode/isinv+1))
        temp=vt*(1.6*(10**(-19)))/(1.38*(10**(-23)))
        diode_vt=Diode(idiode,isinv,vd,n,temp,vt)
        print(vars(diode_vt))
        
    def calculate_vd(idiode,isinvaux,temp,n,vt):
        isinv=isinvaux*(10**(-12))
        vd=n*vt*log(idiode/isinv+1)
        diode_vd=Diode(idiode,isinv,vd,n,temp,vt)
        print(vars(diode_vd))
        
    def calculate_n(idiode,isinvaux,temp,vt,vd):
        isinv=isinvaux*(10**(-12))
        n=vd/(vt*log(idiode/isinv+1))
        diode_n=Diode(idiode,isinv,vd,n,temp,vt)
        print(vars(diode_n))
        
    def calculate_temp(vt):
        temp=vt*(1.6*(10**(-19)))/(1.38*(10**(-23)))
        diode_temp=Diode(0,0,0,0,temp,vt)
        print(vars(diode_temp))