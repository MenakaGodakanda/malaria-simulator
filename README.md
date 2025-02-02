# Malaria Epidemiology Simulator
The Malaria Epidemiology Simulator is a Python-based tool that models the spread of malaria and evaluates the impact of various interventions such as bed nets, medications, and vaccinations. This project helps researchers and public health professionals understand malaria transmission and how different control strategies affect infection rates.<br><br>
The simulation follows a standard SIR (Susceptible-Infected-Recovered) model, which describes the spread of infectious diseases in a population (<a href="https://github.com/MenakaGodakanda/malaria-simulator/blob/main/Mathematical-Explanation.md">Mathematical Explanation</a>).

## Overview
<img width="1336" alt="Screenshot 2025-02-02 at 2 34 40 pm" src="https://github.com/user-attachments/assets/cdfd6221-b9f6-4c97-b445-cd32d0fef6f7" />

### Explanation
- **User Inputs Parameters** → Through CLI (`argparse`)
- **Main Controller** (`malaria_simulator.py`) → Runs the simulation
- **Population Model** (`population.py`) → Defines individuals & tracks infection states
- **Disease Transmission** → Simulates spread based on parameters
- **Interventions** (`interventions.py`) → Applies control measures (bed nets, medications)
- **Simulation Loop** → Runs for user-defined days, updating infections daily
- **Data Collection** → Stores results for visualization and CSV output
- **Visualization** → Creates graphs for insights
- **Outputs**:
  - **Terminal Output** → Shows infected count daily
  - **Graph** → Displays infection trend over time
  - **CSV File** → Stores infection data for further analysis

## Features
- **Agent-Based Modeling**: Simulates individuals in a population and tracks their infection status.
- **Configurable Parameters**: Adjust transmission rate, recovery rate, population size, and intervention coverage.
- **Interventions Module**: Implements bed nets, medications, and supports future vaccination strategies.
- **Graphical & Data Outputs**: Generates infection trend graphs and CSV reports for further analysis.
- **Command-Line Interface (CLI)**: Users can customize the simulation using command-line arguments.

## Installation & Setup

### 1. Install Python & Git
Ensure you have Python 3 and Git installed on Ubuntu:
```
sudo apt update
sudo apt install python3 python3-pip git
```

### 2. Clone the Repository
```
git clone https://github.com/MenakaGodakanda/malaria-simulator.git
cd malaria-simulator
```

### 3. Create a Virtual Environment
```
python3 -m venv malaria-sim-env
source malaria-sim-env/bin/activate
```

### 4. Install Dependencies
```
pip install numpy matplotlib pandas seaborn scipy argparse
```


## Usage
Run the simulator with configurable parameters:
```
python malaria_simulator.py --pop_size 1000 --init_infected 10 --trans_rate 0.05 --recov_rate 0.01 --days 100 --bed_nets 0.3 --medication 0.6
```
- This will simulate 1000 individuals, with 10 initially infected, a 5% transmission rate, and a 1% recovery rate. 30% of the population uses bed nets, and 60% receive medication.

### Available Parameters
| Parameter	| Description	| Default Value |
|------------|-----------|-------------|
|--pop_size |	Total population size	| 1000 |
|--init_infected	| Initial number of infected individuals	| 10
|--trans_rate	| Probability of transmission per interaction	| 0.05
|--recov_rate |	Probability of recovery per day	| 0.01
|--days	| Number of days to run the simulation	| 100
|--bed_nets	| Proportion of people using bed nets	| 0.3 (30%)
|--medication	| Effectiveness of malaria medication	| 0.6 (60%)

## Example Output 01
### 1. Console Output
This shows the number of infected people each day. The infection may initially increase before interventions take effect, leading to a decline in cases.
![Screenshot 2025-02-02 134455](https://github.com/user-attachments/assets/981865e1-d28a-4a82-a80f-91042eaa23fc)
![Screenshot 2025-02-02 134515](https://github.com/user-attachments/assets/034dedd5-6b9a-4dca-b5e9-9be2b1e0952b)

### 2. Graphical Output (Matplotlib)
A line graph is displayed, showing the number of infected individuals over time.
- The infection spreads initially, then declines as interventions take effect.
![Screenshot 2025-02-02 134515 - Copy](https://github.com/user-attachments/assets/5cc4c5c3-9cad-4e91-9aa8-e7f1789cb6e1)

- **X-axis**: Days (1 to 100)
- **Y-axis**: Number of Infected Individuals
- **Line Trend**:
  - Initial increase in infections (due to transmission).
  - Peak in infections at a certain day.
  - Gradual decline as interventions (bed nets, medication) take effect.

### 3. CSV Output (data/simulation_results.csv)
The program save the simulation results to a CSV file in the `data/` folder.
- Example CSV Output (`data/simulation_results.csv`)
![Screenshot 2025-02-02 134532](https://github.com/user-attachments/assets/efde5e5a-abe1-47cd-895b-46b23735e881)
![Screenshot 2025-02-02 134553](https://github.com/user-attachments/assets/0cba40f7-824a-4819-ac21-16088a03963e)

- This file can be used for further analysis or visualization.

### Expected Behavior
#### 1. What Looks Correct
- The infection starts at 10 and increases to 15 (Day 1), which is expected due to transmission.
- After Day 2, the numbers decline, which is logical as recoveries and interventions take effect.
- Final infections reach 0 (Day 11-12), which is expected given the high medication effectiveness (60%).

#### 2. What Looks Wrong
- Weird Increase in Cases (Day 5-6 & Day 9)
  - Day 4 → Day 5: Infected jumps from 4 → 6
  - Day 5 → Day 6: Infected jumps from 6 → 8
  - Day 8 → Day 9: Infected jumps from 1 → 4

- Why is this strange?
  - With a low 5% transmission rate and 30% population protected by bed nets, new infections should gradually decrease, not randomly increase.
  - Once cases drop to 1 infected person (Day 8), it is highly unlikely that cases suddenly rise again (Day 9: 4 infected).
  - If medication is 60% effective, infections should decline smoothly.

- Fluctuation Instead of a Smooth Decline
  - In a well-functioning model, you should not see infections jump back up after dropping.
  - Possible cause: A bug in the reinfection logic where recovered people become susceptible again too soon.

#### 3. Possible Causes of Error
- Incorrect Recovery Calculation
  - Ensure that recovered people stay immune and are not reinfected immediately.
- Reinfection Due to Transmission Rate Misapplication
  - The transmission rate (5%) should only apply to susceptible individuals.
  - If the code accidentally applies it to recovered individuals, it could cause reinfections.
- Check How Medication is Implemented
  - With 60% medication effectiveness, the decline in infections should be much smoother.

### Summary
This simulation demonstrates how malaria spreads and how interventions help control it, making it a valuable epidemiology tool.

## Example Output 02
![Screenshot 2025-02-02 150014](https://github.com/user-attachments/assets/3aeba9ff-3f78-4478-9cf6-18eb001bf760)

### Expected Behavior
#### 1. Initial Increase or Stability:
- The infection count should increase or remain stable in the first few days because the transmission rate (6%) is higher than the recovery rate (2%).
- Infections decline from Day 1 (65) to Day 2 (55), which suggests that transmission is not outpacing recovery.
- *This is possible, but it depends on how many people were protected by bed nets and how effective medication was.

#### 2. Gradual Decline in Infections:
- The recovery rate is low (2%), so the decline should be slow unless medication is significantly helping.
- By Day 10, infections are at 7, which means recovery & interventions are working effectively.
- The 40% medication effectiveness could be speeding up the recovery.

#### 3. Small Fluctuation in Infections (Days 11-25):
- Day 11-24: Infection count remains between 1 and 2 infected individuals.
- This could happen if:
- A small number of people are still transmitting malaria.
- Some reinfections occur.
- This is unusual but not impossible since the transmission rate is low.

#### 4. Simulation Ends at Zero Cases (Day 26):
- This is expected as the infected individuals eventually recover without spreading to new people.

## Example Output 03
![Screenshot 2025-02-02 150227](https://github.com/user-attachments/assets/55a2c320-5fcd-4b05-b975-4cbe31885c3f)

### Expected Behavior of the Simulation
- Day 1-2: The infection count initially rises or remains steady due to ongoing transmission.
- Day 3-10: The number of infected individuals declines steadily due to recoveries & interventions (bed nets reducing transmission and medication helping recovery).
- Day 11-20: The number of infections drops sharply as more people recover or are protected.
- Day 18: Zero infections, meaning the outbreak has ended.

### Why Is This Output Reasonable?
- Infections start at 80 and increase slightly (Day 1: 97 infected) → Expected due to transmission.
- Infections peak and decline as people recover (Recovery Rate = 6%) → Matches expected epidemic curve.
- Interventions (30% bed nets & 20% medication) help reduce cases → Gradual decrease seen in data.
- Simulation ends with zero infections → Since recovery + interventions stop further spread.




## Project Structure
```
malaria-simulator/
│── malaria_simulator.py   # Main script to run the simulation
│── population.py          # Defines population and infection dynamics
│── interventions.py       # Implements malaria control strategies
│── README.md              # Project documentation
│── data/                  # Folder for storing simulation results (CSV)
```

## License
This project is licensed under the MIT License. 
