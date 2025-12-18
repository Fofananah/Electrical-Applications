from dc_core import Resistor, series_resistance, parallel_resistance

tomato = Resistor(5000, 1,2)
potato = Resistor(2000, 2,0)

req = series_resistance([potato,tomato])
print("Potato,Tomato?", req,'Ω')

req_parallel = parallel_resistance([potato,tomato])
print("Chopped!", req_parallel,'Ω')