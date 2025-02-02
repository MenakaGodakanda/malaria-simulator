# Malaria Epidemiology Simulator
The Malaria Epidemiology Simulator is a Python-based tool that models the spread of malaria and evaluates the impact of various interventions such as bed nets, medications, and vaccinations. This project helps researchers and public health professionals understand malaria transmission and how different control strategies affect infection rates.

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
| Parameter	| Description	| Input Value |
|------------|-----------|-------------|
|--pop_size |	Total population size	| 1000 |
|--init_infected	| Initial number of infected individuals	| 10
|--trans_rate	| Probability of transmission per interaction	| 0.05
|--recov_rate |	Probability of recovery per day	| 0.01
|--days	| Number of days to run the simulation	| 100
|--bed_nets	| Proportion of people using bed nets	| 0.3 (30%)
|--medication	| Effectiveness of malaria medication	| 0.6 (60%)

## Example Output
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

### Summary
This simulation demonstrates how malaria spreads and how interventions help control it, making it a valuable epidemiology tool.

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
