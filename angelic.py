from diode import Diode
from jfet import Jfet
from mosfet import Mosfet
from atmega import Atmega
from pcb import PCB
from circuit import Circuit
from mathcalculus import Mathcalculus
from controller import Controller
from divisor import Divisor

print(" A  N  G  E  L  I  C")
option=int(input("Create: \n1.Calculus.\n2.Circuit.\n3.Diode\n4.Transistor.\n5.Exit "))

while option!=5:
    
    if option==1:
        optioncal=int(input("1.Grade to rads.\n2.Rads to grades\n.3.roots.\n4.Rec pol\n5.Pol rec.\n6.Return."))
        while optioncal!=6:
            if optioncal==1:
                gradeang=float(input("Type grade value: "))
                Mathcalculus.calculate_rads(gradeang)
            elif optioncal==2:
                radang=float(input("Type rads value: "))
                Mathcalculus.calculate_grades(radang)
            elif optioncal==3:
                a=float(input("Type a value: "))
                b=float(input("Type b value: "))
                c=float(input("Type c value: "))
                Mathcalculus.calculate_roots(a,b,c)
            elif optioncal==4:
                xvalue=float(input("Type real value: "))
                yvalue=float(input("Type y value: "))
                Mathcalculus.calculate_pol(xvalue,yvalue)
            elif option==5:
                amp=float(input("Type amplitude value: "))
                phase=float(input("Type phase value in rads: "))
                Mathcalculus.calculate_rec(amp,phase)        
            elif option==6:
                print("Returning to main menu.")
        optioncal=int(input("1.1.Grade to rads.\n1.2.Rads to grades\n.1.3.roots.\n1.4.Recpol"))
        
    '''
    if option == 1:
        isinvaux=float(input("Type inverse saturation current in picoAmperes: "))
        vd=float(input("Type direct polarization diode voltage: "))
        n=float(input("Type n, often is 1: "))
        temp=float(input("Type kelvin temperature (K=Celsius+273): "))
        Diode.calculate_id(isinvaux,vd,n,temp)   
                 
    elif option==2:
        idiode=float(input("Type id current: "))
        vd=float(input("Type direct polarization diode voltage: "))
        n=float(input("Type n, often is 1: "))
        temp=float(input("Type kelvin temperature (K=Celsius+273): "))
        Diode.calculate_is(idiode,vd,n,temp)
        
    elif option==3:
        idiode=float(input("Type id current: "))
        isinvaux=float(input("Type inverse saturation current in picoAmperes: "))
        vd=float(input("Type direct polarization diode voltage: "))
        n=float(input("Type n, often is 1: "))
        Diode.calculate_vt(idiode,isinvaux,vd,n)
               
    elif option==4:
        
        idiode=float(input("Type id current: "))
        isinvaux=float(input("Type inverse saturation current in picoAmperes: "))
        temp=float(input("Type kelvin temperature (K=Celsius+273): "))
        n=float(input("Type n, often is 1: "))
        vt=float(input("Type vt voltage: "))
        Diode.calculate_vd(idiode,isinvaux,temp,n,vt)
        
    elif option==5:
        idiode=float(input("Type id current: "))
        isinvaux=float(input("Type inverse saturation current in picoAmperes: "))
        temp=float(input("Type kelvin temperature (K=Celsius+273): "))
        vt=float(input("Type vt voltage: "))
        vd=float(input("Type direct polarization diode voltage: "))
        Diode.calculate_n(idiode,isinvaux,temp,vt,vd)
        
    elif option==6:
        vt=float(input("Type vt voltage: "))
        Diode.calculate_temp(vt)
        
    elif option==7:
        idss=float(input("Type Idss in Amp: "))
        vp=float(input("Type vp in Volts: "))
        vgs=float(input("Type vgs in Volts: "))
        Jfet.calculate_parameters_jfet(idss,vgs,vp)
        
    elif option==8:
        idon=float(input("Type idon value: "))
        vgson=float(input("Type vgson value: "))
        vgsth=float(input("Type vgsth value: "))
        vgs=float(input("Type vgs value: ")) 
        Mosfet.calculate_parameters_mosfet(idon,vgson,vgsth,vgs)
    
    elif option==9:
        f=float(input("Type frequency of oscilation(Hz): "))
        b=float(input("Type baude rate: "))
        Atmega.calculate_UBRR(f,b)
    
    elif option==10:
        i=float(input("Type I in Amperes: "))
        ti=float(input("Type enviironmental temperature in C: "))
        tf=float(input("Type opeational temperature in C: "))
        thickness=float(input("Type width in 1 (35u),2 (70u) or 3 (105u) ounces/foot^2: "))
        PCB.calculate_pcb_parameters(i,ti,tf,thickness) 
    
    elif option==11:
        n=int(input("Type number of resistaces to sum: "))
        Circuit.calculate_resistances_addition(n)
    
    elif option==12:
        ra=float(input("Type Ra value: "))
        rb=float(input("Type Rb value: "))
        rc=float(input("Type Rc value: "))
        Circuit.calculate_dy(ra,rb,rc)
        
    elif option==13:
        r1=float(input("Type R1 value: "))
        r2=float(input("Type R2 value: "))
        r3=float(input("Type R3 value: "))
        Circuit.calculate_yd(r1,r2,r3)
                                
    elif option==14:
        gradeang=float(input("Type grade value: "))
        Mathcalculus.calculate_rads(gradeang)
        
    elif option==15:
        radang=float(input("Type rads value: "))
        Mathcalculus.calculate_grades(radang)
        
    elif option==16:
        xvalue=float(input("Type real value: "))
        yvalue=float(input("Type y value: "))
        Mathcalculus.calculate_pol(xvalue,yvalue)
        
    elif option==17:
        amp=float(input("Type amplitude value: "))
        phase=float(input("Type phase value in rads: "))
        Mathcalculus.calculate_rec(amp,phase)
        
    elif option==18:
        a=float(input("Type a value: "))
        b=float(input("Type b value: "))
        c=float(input("Type c value: "))
        Mathcalculus.calculate_roots(a,b,c)
        
    elif option==19:
        l=float(input("Type L value in Henrys: "))
        c=float(input("Type C value in Faradays: "))
        Circuit.calculate_flc(l,c)
        
    elif option==20:
        lc=float(input("Type L value in Henrys or C value in Faradays: "))
        f=float(input("Type frequency value in Hz: "))
        Circuit.calculate_loc(lc,f)
        
    elif option==21:
        r1=float(input("Type R1 value: "))
        r2=float(input("Type R2 value: "))
        r3=float(input("Type R3 value: "))
        r4=float(input("Type R4 value: "))
        c=float(input("Type c value: "))
        w=float(input("Type w value: "))    
        Circuit.calculate_hmax(r1,r2,r3,r4,c,w)
        
    elif option==22:
        cita=float(input("Type cita value: "))
        ts=float(input("Type ts value: "))
        if ts<0:
            print("ts must be higher than 0.")
            ts=float(input("Type ts value: "))
        Controller.calculate_controller(cita,ts)
        
    elif option==23:
        z1=float(input("Type Z1 value: "))
        z2=float(input("Type Z1 value: "))
        vs=float(input("Type Vs value: "))
        Divisor.calculate_divisor(vs,z1,z2)
    '''            
    