from Core.Components.components import VoltageSource, Resistor, CurrentSource

friendship = VoltageSource(9001, 1,0)
potato = Resistor(5000, 1,2)
tomato = Resistor(2000, 2,0)

print("="*40)
print("↺ RUNTEST SIMULATION ↻")
print("="*40)

print("Components List")
print("----------------")
print("POWER SOURCE:")
print(f"Friendship: {friendship.voltage}|V")
print("\nRESISTORS:")
print(f"Potato: {potato.resistance}|Ω, Entrance: {potato.a_node} Exit: {potato.z_node}")
print(f"Tomato: {tomato.resistance}|Ω, Entrance: {tomato.a_node} Exit: {tomato.z_node}")

print("\n"+"="*40)
print("Circuit Structure")
print("="*40)

print("\nIn Parallel:")
print(f"Friendship splits at {friendship.pos_node}, "
      f"to power Potato and Tomato, and then returns back to friendship at {friendship.neg_node}.")

print("\nIn Series:")
print(f"Friendship goes through Potato, from {friendship.pos_node}, "
      f"to {potato.z_node}, then through Tomato from {potato.z_node} to {friendship.neg_node}, "
      f"\nthrough friendship 0 becomes 1.")