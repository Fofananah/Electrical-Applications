class Resistor:
    def __init__(self, resistance_ohms):
        if resistance_ohms <=0:
            raise ValueError("Resistance must be positive.")
        self.R = resistance_ohms

def series_resistance(resistors):
    if not resistors:
        raise ValueError("No resistors in circuit.")
    total = 0.0
    
    for r in resistors:
        total += r.R
    return total