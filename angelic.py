from diode import Diode
from jfet import Jfet
from mosfet import Mosfet
from atmega import Atmega
from pcb import PCB
from circuit import Circuit
from mathcalculus import Mathcalculus
from controller import Controller
from lm555 import Lm555
#from divisor import Divisor

print(" A  N  G  E  L  I  C")
option=int(input("\nMENU: \n1.Calculus.\n2.Circuit.\n3.Diode\n4.Transistor.\n5.ATMEGA.\n6.PCB.\n7.Controller.\n8.LM555. \n9.Exit! "))

while option!=9:
        
    if option==1:
        option_cal=int(input("  1.Grade to rads.\n  2.Rads to grades\n  3.roots.\n  4.Rec pol\n  5.Pol rec.\n  6.Return. "))
        while option_cal!=6:
            if option_cal==1:
                gradeang=float(input("Type grade value: "))
                Mathcalculus.calculate_rads(gradeang)
            elif option_cal==2:
                radang=float(input("Type rads value: "))
                Mathcalculus.calculate_grades(radang)
            elif option_cal==3:
                a=float(input("Type a value: "))
                b=float(input("Type b value: "))
                c=float(input("Type c value: "))
                Mathcalculus.calculate_roots(a,b,c)
            elif option_cal==4:
                xvalue=float(input("Type real value: "))
                yvalue=float(input("Type y value: "))
                Mathcalculus.calculate_pol(xvalue,yvalue)
            elif option_cal==5:
                amp=float(input("Type amplitude value: "))
                phase=float(input("Type phase value in rads: "))
                Mathcalculus.calculate_rec(amp,phase)        
            option_cal=int(input("  1.Grade to rads.\n  2.Rads to grades\n  3.roots.\n  4.Rec pol\n  5.Pol rec.\n  6.Return. "))
       
    elif option==2:
        option_circuit=int(input("  1.Serial & parallel impedance addition.\n  2.Y-D.\n  3.D-Y.\n  4.LC.\n  5.flc.\n  6.Hay-Maxwell.\n  7.V-I divisors.\n  8.Return. "))   
        while option_circuit!=8:
            if option_circuit==1:
                n=int(input("Type number of resistaces to sum: "))
                Circuit.calculate_resistances_addition(n)
            elif option_circuit==2:
                r1=float(input("Type R1 value: "))
                r2=float(input("Type R2 value: "))
                r3=float(input("Type R3 value: "))
                Circuit.calculate_yd(r1,r2,r3)
            elif option_circuit==3:
                ra=float(input("Type Ra value: "))
                rb=float(input("Type Rb value: "))
                rc=float(input("Type Rc value: "))
                Circuit.calculate_dy(ra,rb,rc)                
            elif option_circuit==4:
                l=float(input("Type L value in Henrys: "))
                c=float(input("Type C value in Faradays: "))
                Circuit.calculate_flc(l,c)
            elif option_circuit==5:
                lc=float(input("Type L value in Henrys or C value in Faradays: "))
                f=float(input("Type frequency value in Hz: "))
                Circuit.calculate_loc(lc,f)
            elif option_circuit==6:
                r1=float(input("Type R1 value: "))
                r2=float(input("Type R2 value: "))
                r3=float(input("Type R3 value: "))
                r4=float(input("Type R4 value: "))
                c=float(input("Type c value: "))
                w=float(input("Type w value: "))    
                Circuit.calculate_hmax(r1,r2,r3,r4,c,w)               
            elif option_circuit==7:
                z1=float(input("Type Z1(ra) value: "))
                z2=float(input("Type Z1(rb) value: "))
                vs=float(input("Type Vs value: "))
                Circuit.calculate_divisor(vs,z1,z2)
            option_circuit=int(input("  1.Serial & parallel impedance addition.\n  2.Y-D.\n  3.D-Y.\n  4.LC.\n  5.flc.\n  6.Hay-Maxwell.\n  7.V-I divisors.\n  8.Return. "))   
    
    elif option==3:
        option_diode=int(input("  1.id.\n  2.is.\n  3.vt.\n  4.vd.\n  5.n.\n  6.Return. "))  
        while option_diode!=6:
            if option_diode==1:
                isinvaux=float(input("Type inverse saturation current in picoAmperes: "))
                vd=float(input("Type direct polarization diode voltage: "))
                n=float(input("Type n, often is 1: "))
                temp=float(input("Type kelvin temperature (K=Celsius+273): "))
                Diode.calculate_id(isinvaux,vd,n,temp)   
            elif option_diode==2:
                idiode=float(input("Type id current: "))
                vd=float(input("Type direct polarization diode voltage: "))
                n=float(input("Type n, often is 1: "))
                temp=float(input("Type kelvin temperature (K=Celsius+273): "))
                Diode.calculate_is(idiode,vd,n,temp)
            elif option_diode==3:
                idiode=float(input("Type id current: "))
                isinvaux=float(input("Type inverse saturation current in picoAmperes: "))
                vd=float(input("Type direct polarization diode voltage: "))
                n=float(input("Type n, often is 1: "))
                Diode.calculate_vt(idiode,isinvaux,vd,n)
            elif option_diode==4:
                idiode=float(input("Type id current: "))
                isinvaux=float(input("Type inverse saturation current in picoAmperes: "))
                temp=float(input("Type kelvin temperature (K=Celsius+273): "))
                n=float(input("Type n, often is 1: "))
                vt=float(input("Type vt voltage: "))
                Diode.calculate_vd(idiode,isinvaux,temp,n,vt)
            elif option_diode==5:
                idiode=float(input("Type id current: "))
                isinvaux=float(input("Type inverse saturation current in picoAmperes: "))
                temp=float(input("Type kelvin temperature (K=Celsius+273): "))
                vt=float(input("Type vt voltage: "))
                vd=float(input("Type direct polarization diode voltage: "))
                Diode.calculate_n(idiode,isinvaux,temp,vt,vd)
            elif option_diode==6:
                vt=float(input("Type vt voltage: "))
                Diode.calculate_temp(vt)    
            option_diode=int(input("  1.id.\n  2.is.\n  3.vt.\n  4.vd.\n  5.n.\n  6.Return. "))                  
        
    elif option==4:
        option_transistor=int(input("  1.JFET & MOSFET EMP.\n  2.JFET & MOSFET ENR.\n  3.Return. "))
        while option_transistor!=3:
            if option_transistor==1:
                idss=float(input("Type Idss in Amp: "))
                vp=float(input("Type vp in Volts: "))
                vgs=float(input("Type vgs in Volts: "))
                Jfet.calculate_parameters_jfet(idss,vgs,vp)
            elif option_transistor==2:
                idon=float(input("Type idon value: "))
                vgson=float(input("Type vgson value: "))
                vgsth=float(input("Type vgsth value: "))
                vgs=float(input("Type vgs value: ")) 
                Mosfet.calculate_parameters_mosfet(idon,vgson,vgsth,vgs)
            option_transistor=int(input("  1.JFET & MOSFET EMP.\n  2.JFET & MOSFET ENR.\n  3.Return. "))
    
    elif option==5:
        f=float(input("Type frequency of oscilation(Hz): "))
        b=float(input("Type baude rate: "))
        Atmega.calculate_UBRR(f,b)
    
    elif option==6:
        i=float(input("Type I in Amperes: "))
        ti=float(input("Type enviironmental temperature in C: "))
        tf=float(input("Type opeational temperature in C: "))
        thickness=float(input("Type width in 1 (35u),2 (70u) or 3 (105u) ounces/foot^2: "))
        PCB.calculate_pcb_parameters(i,ti,tf,thickness)
        
    elif option==7:
        cita=float(input("Type cita value: "))
        ts=float(input("Type ts value: "))
        if ts<0:
            print("ts must be higher than 0.")
            ts=float(input("Type ts value: "))
        Controller.calculate_controller(cita,ts)   

    elif option==8:
        ra=float(input("Type ra conectada a VCC value en Ohms: "))
        rb=float(input("Type rb value en Ohms: "))
        c=float(input("Type c value en F: "))
        Lm555.calculate_parameters_lm555(ra,rb,c)
        
    option=int(input("\nCreate: \n1.Calculus.\n2.Circuit.\n3.Diode\n4.Transistor.\n5.ATMEGA.\n6.PCB.\n7.Controller.\n8.lm555 \n9.Exit! "))