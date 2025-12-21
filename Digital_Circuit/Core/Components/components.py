class Components:
    pass

class Resistor(Components):
    def __init__(self, resistance_ohms, a_node,z_node):
        if resistance_ohms <=0:
            raise ValueError("Resistance must be positive.")
        self.resistance = resistance_ohms
        # Resistor entrance and exit
        self.a_node = a_node
        self.z_node = z_node

class VoltageSource(Components):
    def __init__(self,voltage_volts,pos_node,neg_node):
        self.voltage = voltage_volts   
        # Voltage source postive, and negative terminals   
        self.pos_node = pos_node
        self.neg_node= neg_node
        
class CurrentSource(Components):
    def __init__(self,current_amps,from_node,to_node):
        self.current = current_amps      
        # Current flow direction 
        self.from_node = from_node
        self.to_node = to_node