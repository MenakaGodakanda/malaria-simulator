import argparse
import matplotlib.pyplot as plt
import numpy as np
import os
import csv
from population import Population
from interventions import Interventions

def run_simulation(pop_size, init_infected, trans_rate, recov_rate, days, bed_nets, medication):
    pop = Population(pop_size, init_infected, trans_rate, recov_rate)
    intervention = Interventions(bed_nets, medication)

    history = []
    for day in range(days):
        intervention.apply_bed_nets(pop)
        pop.update()
        intervention.apply_medication(pop)
        infected_count = np.count_nonzero(pop.states == 1)  # Track infected count
        history.append(infected_count)
        print(f"Day {day + 1}: Infected = {infected_count}")

    return history

def save_to_csv(data, filename):
    # Ensure the data directory exists
    os.makedirs('data', exist_ok=True)
    
    # Write the data to a CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Day', 'Infected'])
        for day, infected in enumerate(data, start=1):
            writer.writerow([day, infected])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pop_size", type=int, default=1000)
    parser.add_argument("--init_infected", type=int, default=10)
    parser.add_argument("--trans_rate", type=float, default=0.05)
    parser.add_argument("--recov_rate", type=float, default=0.01)
    parser.add_argument("--days", type=int, default=100)
    parser.add_argument("--bed_nets", type=float, default=0.2)
    parser.add_argument("--medication", type=float, default=0.5)

    args = parser.parse_args()
    history = run_simulation(args.pop_size, args.init_infected, args.trans_rate, args.recov_rate, args.days, args.bed_nets, args.medication)

    # Save the results to a CSV file
    csv_filename = os.path.join('data', 'simulation_results.csv')
    save_to_csv(history, csv_filename)
    print(f"Simulation results saved to {csv_filename}")

    # Plot the results
    plt.plot(history)
    plt.xlabel("Days")
    plt.ylabel("Infected Population")
    plt.title("Malaria Spread Simulation")
    plt.show()
