from dc_core import Resistor, series_resistance, parallel_resistance

potato = Resistor(5000)
tomato = Resistor(2000)

req = series_resistance([potato,tomato])
print("Potato Tomato:", req)

req_parallel = parallel_resistance([potato,tomato])
print("Chopped!", req_parallel)