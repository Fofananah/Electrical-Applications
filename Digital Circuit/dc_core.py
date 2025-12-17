class Resistor:
    def __init__(self, resistance_ohms):
        if resistance_ohms <=0:
            raise ValueError("Resistance must be positive.")
        self.resistance = resistance_ohms

class VoltageSource:
    def __init__(self,voltage_volts):
        self.voltage = voltage_volts
        
class CurrentSource:
    def __init__(self,current_amps):
        self.current = current_amps


class Circuit:
    def __init__(self):
        self.components = []
        self.nodes = set()


def series_resistance(resistors):
    if not resistors:
        raise ValueError("No resistors in circuit.")
    
    total = 0.0
    for r in resistors:
        total += r.resistance
    return total

def parallel_resistance(resistors):
    if not resistors:
        raise ValueError("No resistors in circuit.")
    
    inverse_total = 0.0
    for r in resistors:
        inverse_total += 1 / r.resistance 
    return 1 / inverse_total