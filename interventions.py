import numpy as np

class Interventions:
    def __init__(self, bed_net_coverage=0, medication_effectiveness=0):
        self.bed_net_coverage = bed_net_coverage
        self.medication_effectiveness = medication_effectiveness

    def apply_bed_nets(self, population):
        protected = int(population.size * self.bed_net_coverage)
        for i in np.random.choice(population.size, protected, replace=False):
            if population.states[i] == 0:
                population.states[i] = -1  # Protected (won't be infected)
    
    def apply_medication(self, population):
        for i in range(population.size):
            if population.states[i] == 1:  # Infected
                if np.random.rand() < self.medication_effectiveness:
                    population.states[i] = 2  # Recovered

