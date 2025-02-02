import numpy as np

class Population:
    def __init__(self, size, initial_infected, transmission_rate, recovery_rate):
        self.size = size
        self.transmission_rate = transmission_rate
        self.recovery_rate = recovery_rate
        self.states = np.zeros(size)  # 0: Susceptible, 1: Infected, 2: Recovered
        infected_indices = np.random.choice(size, initial_infected, replace=False)
        self.states[infected_indices] = 1

    def update(self):
        new_infected = []
        for i in range(self.size):
            if self.states[i] == 0:  # Susceptible
                if np.any(self.states == 1) and np.random.rand() < self.transmission_rate:
                    new_infected.append(i)
            elif self.states[i] == 1:  # Infected
                if np.random.rand() < self.recovery_rate:
                    self.states[i] = 2  # Recovered
        
        for i in new_infected:
            self.states[i] = 1

