from ..Components.components import Components

class Circuit:
    def __init__(self):
        self.components = []
        # set to create unique ID's for each node
        self.nodes = set()
        # voltage dictionary for each node
        self.node_voltages = {}
        
    def add_component(self,component):
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
                self.node_voltages[comp.pos_node] = comp.voltage
                self.node_voltages[comp.neg_node] = 0.0