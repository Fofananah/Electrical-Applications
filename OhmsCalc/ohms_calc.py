print("Ohm's Law Calculator")

intensity_input = input("Enter the current intensity (I) In Amperes.")
I = float(intensity_input)

resistance_input = input("Enter the resistance (R) in Ohms.")
R = float(resistance_input)

#Ohm's Law V = I * R
V = I * R

print("***********************************")
print(f"Current (I): {I} A")
print(f"Resistance (R): {R} Ω")
print(f"Calculated Voltage (V): {V} V")
print("***********************************")