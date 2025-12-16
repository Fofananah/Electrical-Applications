from dc_core import Resistor, series_resistance

potato = Resistor(5000)
tomato = Resistor(2000)

req = series_resistance([potato,tomato])

print("Potato Tomato:", req)