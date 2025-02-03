# Mathematical Explanation

The Python scripts of this project simulate the spread of malaria using a **discrete-time stochastic SIR model** with **interventions** (bed nets and medication). Below is a step-by-step explanation of how the mathematical equations govern the simulation.

## 1. SIR Model and Core Equations
The simulation follows a standard SIR (Susceptible-Infected-Recovered) model, which describes the spread of infectious diseases in a population. The three main compartments are:
- **Susceptible (𝑆)**: Individuals who can be infected.
- **Infected (𝐼)**: Individuals who have malaria and can spread it.
- **Recovered (𝑅)**: Individuals who have recovered and are immune.

The **continuous-time SIR model** is described by the following differential equations:

### Susceptible (S) Equation
```math
\frac{dS}{dt} = -\beta {S I}
```
- $$\beta$$ is the **transmission rate**, determining how easily the infection spreads.
- 𝑆𝐼 represents interactions between susceptible and infected individuals.
- The negative sign indicates that susceptible individuals are **decreasing** over time.

### Infected (I) Equation
```math
\frac{dI}{dt} = \beta {S I} - \gamma I
```
- The first term ($$\beta$$𝑆𝐼) represents new infections.
- The second term ($$\gamma$$𝐼) represents recovery.
- $$\gamma$$ is the **recovery rate**, which defines the probability per time step that an infected person recovers.

### Recovered (R) Equation
```math
\frac{dR}{dt} = \gamma I
```
- Recovered individuals increase as infected individuals recover.

## 2. How These Equations Are Implemented in the Script
The simulation uses a discrete-time approximation of the SIR equations. Instead of using continuous derivatives, the population updates at each time step.

### Population Class (`Population.py`)
Each individual in the population is assigned a state:
- **Susceptible (0)**
- **Infected (1)**
- **Recovered (2)**

At each time step:
1. New infections occur based on a random probability tied to the transmission rate $$\beta$$.
2. Infected individuals recover based on the recovery rate $$\gamma$$.

#### 1. Infection Process in the Code
```
if self.states[i] == 0:  # Susceptible
    if np.any(self.states == 1) and np.random.rand() < self.transmission_rate:
        new_infected.append(i)
```
- A susceptible individual 𝑆 has a chance to become infected.
- If **at least one infected person exists** ( $$\sum$$𝐼 > 0), a random number is drawn.
- If $$rand$$ < $$\beta$$, the individual transitions to **infected (1)**.
This implements the discrete-time approximation:

$$S_{t+1} = S_{t} - \Delta S$$
where  $$\Delta S 	\approx \beta SI$$

#### 2. Recovery Process in the Code
```
elif self.states[i] == 1:  # Infected
    if np.random.rand() < self.recovery_rate:
        self.states[i] = 2  # Recovered
```
- An infected individual has a probability $$\gamma$$ of recovering at each time step.
- If $$rand$$ < $$\gamma$$, the individual transitions to **recovered (2)**.

<br><br>
This implements:<br>

$$I_{t+1} = I_{t} + \Delta S - \Delta R$$
<br>where<br>  $$\Delta R 	\approx \gamma I$$ <br>
$$R_{t+1} = R_{t} + \Delta R$$

## 3. Interventions and Their Equations
The model includes **two intervention strategies: bed nets and medication**, which modify the core SIR equations.

### A. Bed Nets (Reducing Susceptibility)
Bed nets reduce the number of susceptible individuals who can be infected. Mathematically, we modify 𝑆:

$$S_{effective} = S(1 - C_{b})$$

where:
- $$C_{b}$$ is the **bed net coverage** (e.g., 20% means 20% of people are protected).
- This means that a fraction of susceptible individuals will **not be infected**.

#### Implementation in the Code (`Interventions.py`)
```
protected = int(population.size * self.bed_net_coverage)
for i in np.random.choice(population.size, protected, replace=False):
    if population.states[i] == 0:
        population.states[i] = -1  # Protected (won't be infected)
```
- A fraction of the population is randomly chosen to be **protected (-1)**.
- Protected individuals **cannot become infected**.
Effectively, this modifies the infection equation:

$$S_{t+1} = S_{t}(1 - C_{b}) - \beta SI$$

### B. Medication (Increasing Recovery Rate)
Medication increases the recovery rate $$\gamma$$, meaning infected individuals recover faster:

$$\gamma_{effective} = \gamma + C_{m}$$

where:
- $$C_{m}$$ is **medication effectiveness** (e.g., 50% increases recovery by 50%).
- This reduces the time an individual remains infected

#### Implementation in the Code (`Interventions.py`)
```
if population.states[i] == 1:  # Infected
    if np.random.rand() < self.medication_effectiveness:
        population.states[i] = 2  # Recovered
```
- Each infected person has an **extra probability** of recovery.
- If $$rand$$ < $$C_{m}$$, the individual transitions to **recovered**.
Effectively, this modifies the recovery equation:

$$R_{t+1} = R_{t} + (\gamma + C_{m})I$$

## 4. Running the Simulation (`Malaria_simulation.py`)
The simulation runs for a given number of **days**:
```
for day in range(days):
    intervention.apply_bed_nets(pop)
    pop.update()
    intervention.apply_medication(pop)
    history.append(np.count_nonzero(pop.states == 1))  # Track infected count
```
1. **Apply bed nets** (reduce susceptibility).
2. **Update population** (apply infection and recovery).
3. **Apply medication** (increase recovery rate).
4. **Record the number of infected individuals**.
This gives a time series of infected individuals, which is plotted.

## 5. Summary of Mathematical Equations Used

| Process	| Continuous Equation	| Discrete Approximation | Code Implementation |
|------------|-----------|-------------|-----------|
| New infections | $$\frac{dS}{dt} = -\beta {S I}$$| $$S_{t+1} = S_{t} - \beta SI$$| `if np.random.rand() < trans_rate:` |
| New recoveries | $$\frac{dR}{dt} = \gamma I$$| $$R_{t+1} = R_{t} + \gamma I$$| `if np.random.rand() < recov_rate:` |
| Bed nets | $$S_{effective} = S(1 - C_{b})$$ | $$S_{t+1} = S_{t}(1 - C_{b}) - \beta SI$$ | `states[i] = -1`|
| Medication | $$\gamma_{effective} = \gamma + C_{m}$$ | $$R_{t+1} = R_{t} + (\gamma + C_{m})I$$| `if np.random.rand() < medication:`|


## Conclusion
- The simulation is a **stochastic** implementation of the **SIR model**.
- **Bed nets** reduce the **number of susceptible individuals**.
- **Medication** increases the **recovery rate**.
- The model captures **disease dynamics over time**, allowing for different intervention strategies.
This approach helps in **understanding malaria spread** and the **effectiveness of interventions** in controlling outbreaks.





