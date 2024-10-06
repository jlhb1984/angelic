printf('\n\n  A  N  G  E  L  I  C    A C T I V A D O\n\n')
opcion=1

while(opcion<>20)

printf('\n\n MENU\n 1. RESISTENCIAS EN SERIE Y PARALELO\n 2. DELTA ESTRELLA\n 3. ESTRELLA DELTA\n 4. GRADOS A RADIANES\n 5. RADIANES A GRADOS\n 6. REC-POL\n 7. POL-REC\n 8. SOLUCION CUADRATICA\n 9. COMPENSADORES\n 10. FRECUENCIA\n 11. L O C\n 12. ID JFET Y MOSFET EMP\n 13. ID MOSFET ENR Y MESFET\n 14. ANCHO DE PISTA\n 15. HAY/MAXWELL\n 16. L\n 17. INDUCTOMETRO\n 18. REGULADOR REDUCTOR\n 19. UBRR ATMEGA\n 20. SALIR')
opcion=input(' SELECCIONE LA OPCION ->')

select opcion
    
   case 1 then n=input(' DIGITE EL NUMERO DE RESISTENCIAS A SUMAR ->')
                n=n-1
                RSERIE=0
                RPARALELOAUX=0
                                                                       
                for i=0:n
                    R=input(' DIGITE EL VALOR DE R ->')
                    RSERIE=RSERIE+R 
                    RPARALELOAUX=RPARALELOAUX+1/R
                end
                
                RPARALELO=1/RPARALELOAUX
                printf('\n LA RESISTENCIA EN SERIE ES:')
                disp(RSERIE)
                printf('\n LA RESISTENCIA EN PARALELO ES:')
                disp(RPARALELO)
                                                    
    case 2 then RA=input(' DIGITE EL VALOR DE RA ->')
                RB=input(' DIGITE EL VALOR DE RB ->')
                RC=input(' DIGITE EL VALOR DE RC ->')
                R1=(RA*RB)/(RA+RB+RC)
                R2=(RB*RC)/(RA+RB+RC)
                R3=(RA*RC)/(RA+RB+RC)
                printf('\n EL VALOR DE R1 ES: ')
                disp(R1)
                printf('\n EL VALOR DE R2 ES: ')
                disp(R2)
                printf('\n EL VALOR DE R3 ES: ')
                disp(R3)
                
    case 3 then R1=input(' DIGITE EL VALOR DE R1 ->')
                R2=input(' DIGITE EL VALOR DE R2 ->')
                R3=input(' DIGITE EL VALOR DE R3 ->')
                RA=(R1*R2+R2*R3+R3*R1)/R1
                RB=(R1*R2+R2*R3+R3*R1)/R2
                RC=(R1*R2+R2*R3+R3*R1)/R3
                printf('\n EL VALOR DE RA ES:')
                disp(RA)
                printf('\n EL VALOR DE RB ES:')
                disp(RB)
                printf('\n EL VALOR DE RC ES:')
                disp(RC)  
    
    case 4 then angulograd=input(' DIGITE EL VALOR EN GRADOS ->')
                angulorad=(angulograd*%pi)/180
                printf(' EL ANGULO EN RADIANES ES: ')
                disp(angulorad)
                
    case 5 then angulorad=input(' DIGITE EL VALOR EN RADIANES ->')
                angulograd=angulorad*(180/%pi) 
                printf(' EL ANGULO EN GRADOS ES: ')
                disp(angulograd)
                
    case 6 then valorx=input(' DIGITE EL VALOR REAL ->')
                valorj=input(' DIGITE EL VALOR IMAGINARIO ->')
                amplitud=sqrt(valorx^2+valorj^2)
                fase=atan(valorj/valorx)
                printf(' EL VALOR DE LA AMPLITUD ES:')
                disp(amplitud)
                printf(' EL VALOR DE LA FASE ES:')
                disp(fase)
                
    case 7 then amplitud=input(' DIGITE LA AMPLITUD ->')
                fase=input(' DIGITE LA FASE EN RADIANES->')
                valorx=amplitud*cos(fase)
                valorj=amplitud*sin(fase)
                printf(' EL VALOR REAL ES:')
                disp(valorx)
                printf(' EL VALOR IMAGINARIO ES:')
                disp(valorj)
                
    case 8 then a=input(' DIGITE EL VALOR DE A ->')
                b=input(' DIGITE EL VALOR DE B ->')
                c=input(' DIGITE EL VALOR DE C ->')
                x1=(-b+sqrt(b^2-4*a*c))/(2*a)
                x2=(-b-sqrt(b^2-4*a*c))/(2*a)
                printf(' LA SOLUCIÓN ES:')
                disp(x1)
                disp(x2)
                
    case 9 then cita=input(' DIGITE EL VALOR DE CITA ->')
                ts=input(' DIGITE EL TIEMPO DE ASENTAMIENTO DESEADO ->')
        
                    if ts<0 then
                        printf(' EL TIEMPO DE ASENTAMIENTO DEBE SER MAYOR A 0')
                        ts=input(' DIGITE EL TIEMPO DE ASENTAMIENTO DESEADO ->')
                    end
        
                wn=(4/(cita*ts))
                printf(' PARAMETROS CALCULADOS CON CRITERIO 2 POR CIENTO PARA CITA=%f Y TIEMPO DE ASENTAMIENTO=%f\n', cita, ts)
                printf(' wn=%f\n', wn)
                raiz=sqrt(1-cita^2)
                wd=wn*raiz
                printf(' wd=%f\n', wd)
                tp=%pi/wd
                printf(' tp=%f\n', tp)
                beta=atan(raiz/(cita))
                printf(' beta=%f\n', beta)
                tr=(%pi-beta)/wd
                printf(' tr=%f\n', tr)
                mp=1-exp((-1)*cita*wn*tp)*sin(beta+wd*tp)
                printf(' mp=%f\n', mp)
                
                wn=(3/(cita*ts))
                printf(' PARAMETROS CALCULADOS CON CRITERIO 5 POR CIENTO PARA CITA=%f Y TIEMPO DE ASENTAMIENTO=%f\n', cita, ts)
                printf(' wn=%f\n', wn)
                raiz=sqrt(1-cita^2)
                wd=wn*raiz
                printf(' wd=%f\n', wd)
                tp=%pi/wd
                printf(' tp=%f\n', tp)
                beta=atan(raiz/(cita))
                printf(' beta=%f\n', beta)
                tr=(%pi-beta)/wd
                printf(' tr=%f\n', tr)
                mp=1-exp((-1)*cita*wn*tp)*sin(beta+wd*tp)
                printf(' mp=%f\n', mp)  
                
    case 10 then l=input(' DIGITE LA INDUCTANCIA ->')
                 c=input(' DIGITE LA CAPACITANCIA ->')
                 f=(1/(2*%pi))*sqrt(1/(l*c))
                 printf(' LA FRECUENCIA ES:')
                 disp(f)    
                 
    case 11 then lc=input(' DIGITE LA INDUCTANCIA O CAPACITANCIA->')
                 f=input(' DIGITE LA FRECUENCIA ->')
                 xcl=1/(4*%pi^2*f^2*lc)  
                 printf(' EL VALOR DE L O C ES:')
                 disp(xcl) 
                 
    case 12 then idss=input(' DIGITE IDSS ->')
                 vp=input(' DIGITE VP ->')
                 vgs=input(' DIGITE VGS ->')
                 id=idss*((1-vgs/vp)^2)
                 gmo=(2*idss)/(vp)
                 gm=gmo*(1-vgs/vp)
                 printf(' EL VALOR DE ID ES:')
                 disp(id)
                 printf(' EL VALOR DE GMO ES:')
                 disp(gmo)
                 printf(' EL VALOR DE GM ES:')
                 disp(gm)
    
    case 13 then idon=input(' DIGITE EL VALOR DE IDEON ->')
                 vgson=input(' DIGITE EL VALOR DE VGSON ->')
                 vgsth=input(' DIGITE EL VALOR DE VGSTH ->')
                 vgs=input(' DIGITTE EL VALOR DE VGS ->')
                 k=idon/((vgson-vgsth)^2)
                 printf(' EL VALOR DE K ES:')
                 disp(k)
                 gm=2*k*(vgs-vgsth)
                 printf(' EL VALOR DE GM ES: ')
                 disp(gm)
                 id=k*(vgs-vgsth)^2
                 printf(' EL VALOR DE ID ES:')
                 disp(id)
                                  
    case 14 then i=input(' DIGITE LA CORRIENTE EN A ->')
                 ti=input(' DIGITE LA TEMPERATURA AMBIENTE EN C ->')
                 tf=input(' DIGITE LA TEMPERATURA DE OPERACION EN C ->')
                 grosor=input(' DIGITE EL GROSOR EN 1 (35MICRAS),2 (70MICRAS) O 3 (105 MICRAS) ONZAS/PIE^2 ->')
                 k1=0.0647
                 k2=0.4280
                 k3=0.6732
                 
                 area=(i/(k1*(tf-ti)^k2))^(1/k3)
                 printf(' EL AREA PARA PISTA EXTERIOR ES:')
                 disp(area)
                 ancho=(area/(grosor*1.378))
                 printf(' EL ANCHO PARA PISTA EXTERIOR ES (Th MILESIMAS DE PULGADA):')
                 disp(ancho)
                 
                 k1=0.0150
                 k2=0.5453
                 k3=0.7379                 
                          
                 area=(i/(k1*(tf-ti)^k2))^(1/k3)
                 printf(' EL AREA PARA PISTA INTERIOR ES:')
                 disp(area)
                 ancho=(area/(grosor*1.378))
                 printf(' EL ANCHO PARA PISTA INTERIOR ES (Th MILESIMAS DE PULGADA):')
                 disp(ancho)
                 
    case 15 then r1=input(' DIGITE EL VALOR DE R1 ->')
                 r2=input(' DIGITE EL VALOR DE R2 ->')
                 r4=input(' DIGITE EL VALOR DE R4 ->')
                 c=input(' DIGITE EL VALOR DE C->')
                 w=input(' DIGITE EL VALOR DE W->')
                 rx=(r2*r4*w^2*r1*c^2)/(1+r1^2*w^2*c^2)
                 printf(' RX PUENTE HAY:')                 
                 disp(rx)
                 lx=(r2*r4*c)/(1+(r1*w*c)^2)
                 printf(' LX PUENTE HAY:')
                 disp(lx)
                 rx=(r4*r2)/r1
                 printf(' RX PUENTE MAXWELL:')
                 disp(rx)
                 printf(' LX PUENTE MAXWELL:')
                 lx=r4*r2*c
                 disp(lx)
                 
    case 16 then print("En pruebas!")
//                 N=input(' DIGITE EL NUMERO DE VUELTAS ->')
//                 l=input(' DIGITE LA LONGITUD ->')
//                 r=input(' DIGITE EL RADIO ->')
//                 a=(%pi*r^2)
//                 lb=(N/l)^2*l*acir*4*%pi*1d-7
//                 printf(' L CIRCULAR:')
//                 disp(lb)
//                 a=(r^2)
//                 printf(' L CUADRADA:')
//                 lb=(N/l)^2*l*a*4*%pi*1d-7
//                 disp(lb)
                 
    case 17 then f=input(' DIGITE EL VALOR DE LA FRECUENCIA (Hz)->')
                 c=input(' DIGITE EL VALOR DE LA CAPACITANCIA ->')
                 r=input(' DIGITE EL VALOR DE LA RESISTENCIA->')
                 v=input(' DIGITE EL VALOR DEL VOLTAJE->')
                 i=v/r
                 w=2*%pi*f
                 a=(i*w)^2
                 b=(2*i^2)/c
                 c=(i^2)/((w*c)^2)+i^2*r^2-v^2
                 s=poly(0,'s')
                 l=roots(a*s^2-b*s+c)
                 printf(' EL VALOR DE LA BOBINA ES:')
                 disp(l)
                 
    case 18 then f=input(' DIGITE EL VALOR DE LA FRECUECNIA (Hz)->')
                 vs=input(' DIGITE EL VALOR DEL VOLTAJE DC ->')
                 l=input(' DIGITE EL VALOR DE LA INDUCTANCIA -> ')
                 di=vs/(4*f*l)
                 printf(' EL VALOR DI MAX ES: ')
                 disp(di)                                    
                 
    case 19 then f=input(' DIGITE LA FRECUENCIA DE OSCILACION (Hz)->')
                 b=input(' DIGITE LA RATA DE BAUDIOS->')
                 u=f/(16*b)-1
                 printf(' ASYNCHRONUS NORMAL MODE UBRR: ')
                 disp(u)
                 u=f/(8*b)-1
                 printf(' ASYNCHRONUS DOUBLE SPEED MODE UBRR: ')
                 disp(u)
                 u=f/(2*b)-1
                 printf(' SYNCHRONUS MASTER MODE UBRR: ')
                 disp(u)
                                 
    case 20 then printf('\n\n CHAO AMIGOS :)\n')
                 
    else
    printf(' OPCION NO VALIDA')
    
    end
end
