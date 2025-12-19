class Resistor:
    def __init__(self, resistance_ohms, a_node,z_node):
        if resistance_ohms <=0:
            raise ValueError("Resistance must be positive.")
        self.resistance = resistance_ohms
        # Resistor entrance and exit
        self.a_node = a_node
        self.z_node = z_node

class VoltageSource:
    def __init__(self,voltage_volts,pos_node,neg_node):
        self.voltage = voltage_volts   
        # Voltage source postive, and negative terminals   
        self.pos_node = pos_node
        self.neg_node= neg_node
        
class CurrentSource:
    def __init__(self,current_amps,from_node,to_node):
        self.current = current_amps      
        # Current flow direction 
        self.from_node = from_node
        self.to_node = to_node

class Circuit:
    def __init__(self):
        self.components = []
        # set to create unique ID's for each node
        self.nodes = set()
        # voltage dictionary for each node
        self.node_voltages = {}
        
    def add_components(self,component):
        self.components.append(component)
               
        if isinstance(component,Resistor):
            self.nodes.add(component.a_node)
            self.nodes.add(component.z_node)
        elif isinstance(component,VoltageSource):
            self.nodes.add(component.pos_node)
            self.nodes.add(component.neg_node)
        elif isinstance(component,CurrentSource):
            self.nodes.add(component.from_node)
            self.nodes.add(component.to_node)
            
    # current intensity calculation  I = V / R
    def get_resistor_current(self, resistor):
        v_start = self.node_voltages.get(resistor.a_node, 0.0)
        v_end = self.node_voltages.get(resistor.z_node, 0.0)
        v_total = v_start - v_end
        currentIntensity = v_total / resistor.resistance
        return currentIntensity

    # auto sets node voltage based on voltage source
    def apply_voltage(self):
        for comp in self.components:
            if isinstance(comp, VoltageSource):
                self.node_voltages[comp,pos_node] = comp.voltage
                self.node_voltages[comp,neg_node] = 0.0
        
def series_resistance(resistors):
    if not resistors:
        raise ValueError("No resistors in circuit.")
    
    series_total = 0.0
    for r in resistors:
        series_total += r.resistance
    return series_total

def parallel_resistance(resistors):
    if not resistors:
        raise ValueError("No resistors in circuit.")
    
    parallel_total = 0.0
    for r in resistors:
        parallel_total += 1 / r.resistance 
    return 1 / parallel_total