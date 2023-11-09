import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the acceptance probability
def acceptance_probability(delta_energy, temperature):
    return np.exp(-delta_energy / temperature) * 100

# Parameters
num_epochs = 100
temperature = 5.0
cooling_rate = 0.95

# Initialize a plot
plt.figure(figsize=(10, 6))

# Calculate and plot acceptance probability for the given temperature and cooling rate
acceptance_probabilities = []
current_temperature = temperature
for epoch in range(num_epochs):
    acceptance_probabilities.append(acceptance_probability(1, current_temperature))
    current_temperature *= cooling_rate

plt.plot(range(num_epochs), acceptance_probabilities, label=f'Temp {temperature}, Cooling Rate {cooling_rate}')

plt.xlabel('Epoch')
plt.ylabel('Acceptance Probability (in %)')
plt.title(f'Acceptance Probability vs. Epoch for Temperature {temperature} and Cooling Rate {cooling_rate}')
plt.legend()
plt.grid(True)

plt.show()
