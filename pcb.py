class PCB:
    i=float
    ti=float
    tf=float
    thickness=float
    outerarea=float
    innerarea=float
    outerwidth=float
    innerwidth=float
    
    def __init__(self,i,ti,tf,thickness,outerarea,innerarea,outerwidth,innerwidth):
        self.i=i
        self.ti=ti
        self.tf=tf
        self.thickness=thickness
        self.outerarea=outerarea
        self.innerarea=innerarea
        self.outerwidth=outerwidth
        self.innerwidth=innerwidth
        
    def calculate_pcb_parameters(i,ti,tf,thickness):
        k1=0.0647
        k2=0.4280
        k3=0.6732    
        outerarea=(i/(k1*(tf-ti)**k2))**(1/k3)
        outerwidth=(outerarea/(thickness*1.378))
        k1=0.0150
        k2=0.5453
        k3=0.7379
        innerarea=(i/(k1*(tf-ti)**k2))**(1/k3)
        innerwidth=(innerarea/(thickness*1.378))
        pcb1=PCB(i,ti,tf,thickness,outerarea,innerarea,outerwidth,innerwidth)
        print(vars(pcb1))
        
    