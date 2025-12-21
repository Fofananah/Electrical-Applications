from ..Components.components import Resistor

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