class Atmega:
    f=float
    b=float
    asynch_n_mode=float
    asynch_2_speed_mode=float
    synch_master_mode=float
    
    def __init__(self,f,b,asynch_n_mode,asynch_2_speed_mode,synch_master_mode):
        self.f=f
        self.b=b
        self.asynch_n_mode=asynch_n_mode
        self.asynch_2_speed_mode=asynch_2_speed_mode
        self.synch_master_mode=synch_master_mode
    
    def calculate_UBRR(f,b):
        asynch_n_mode=f/(16*b)-1
        asynch_2_speed_mode=f/(8*b)-1
        synch_master_mode=f/(2*b)-1
        atmega1=Atmega(f,b,asynch_n_mode,asynch_2_speed_mode,synch_master_mode)
        print(vars(atmega1))
        
        
