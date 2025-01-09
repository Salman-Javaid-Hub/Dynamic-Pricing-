import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation
from models.state import State
from models.decision import Decision
from models.transition import Transition
from models.objective import Objective
from models.qlearning import QLearning

filepath = r"C:/Users/Hp/Desktop/Dynamic Project/data/rides.csv"
data = pd.read_csv(filepath)

base_fare = 10
states = ["high_high", "high_low", "low_high", "low_low"]
actions = ["increase", "decrease", "maintain"]
num_of_riders = []
num_of_drivers = []

#policy and q-learning fares
p_fares = []
q_fares = []

##policy and q-learning profit
p_profit = []
q_profit = []

#which actions are taken e.g. increase, decrease, maintain
taken_actions = [] 
#captueing the states according to their status. e.g. number of higi_high state, low_high state etc
state_evolving = {}
#how did the algorithm take action to take make profit
qprofit_with_taken_actions = []

#algorithm initialisation
qlearning = QLearning(states, actions)


def main():

    #total fare and profit 
    pfare_total = 0
    qfare_total = 0
    p_profit_total = 0
    q_profit_total = 0

    for index, row in data.iterrows():
        riders = row.get("riders", 0)
        drivers = row.get("drivers", 0)
        rides = row.get("rides", 0)

        
        state = State(riders=riders, drivers=drivers, base_fare=base_fare)

        num_of_riders.append(riders)
        num_of_drivers.append(drivers)

        decision = Decision(state, qlearning)
        decision_result = decision.decision_making()
        action = decision_result["qlearning_action"] 

        transition = Transition(state, qlearning)
        old_q_value = qlearning.q_table[state.get_state()][action]
        print(f"Q value before= {old_q_value}")
        state_updated = transition.trans_action(action)
    
        taken_actions.append(action)
        qprofit_with_taken_actions.append(decision_result["qlearning_profit"])

        #this is for the visualisation
        p_fares.append(decision_result["policy_fare"])
        q_fares.append(decision_result["qlearning_fare"])
        p_profit.append(decision_result["policy_profit"])
        q_profit.append(decision_result["qlearning_profit"])

        #this is to calculate total fare and profit at the end of the data
        pfare_total = pfare_total + decision_result["policy_fare"]
        qfare_total = qfare_total + decision_result["qlearning_fare"]
        p_profit_total = p_profit_total + decision_result["policy_profit"]
        q_profit_total = q_profit_total + decision_result["qlearning_profit"]
        
        print(f"Total fare of Policy: ${pfare_total:.2f}")
        print(f"Total fare of Q learning: ${qfare_total:.2f}")
        print(f"Total profit of Policy: ${p_profit_total:.2f}")
        print(f"Total profit of Q learning: ${q_profit_total:.2f}")
        print("")

main()


figure, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 6))

def update(frame):
    ax1.clear()
    ax2.clear()

    #profit comparison plot
    ax1.plot(p_profit[:frame], label="Policy Profit", color="blue")
    ax1.plot(q_profit[:frame], label="Qlearning Profit", color="orange")
    ax1.set_title("Polciy and Qlearning Profit Comparison")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Profit")
    ax1.grid(True)
    ax1.legend()

    #fare comparison plot
    ax2.plot(p_fares[:frame], label="Policy Fare", color="green")
    ax2.plot(q_fares[:frame], label="Qlearning Fare", color="red")
    ax2.set_title("Polciy and Qlearning Fare Comparison")
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Fare")
    ax2.grid(True) 
    ax2.legend()

visualisation = FuncAnimation(figure, update, frames=len(p_fares), interval=300, repeat=False)
plt.tight_layout(pad=3.0)
plt.show()

#visuulisations for different categories
def riders_drivers_comp(riders, drivers):
    figure, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 6))

    ax1.plot(riders, color='purple', linestyle='--', marker='o', label='Riders')
    ax1.set_title("Riders Availability Over Time")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Number of Riders")
    ax1.grid(True)

    ax2.plot(drivers, color='brown', linestyle='-.', marker='x', label='Drivers')
    ax2.set_title("Drivers Availability Over Time")
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Number of Drivers")
    ax2.grid(True)

    plt.tight_layout(pad=3.0)
    plt.show()

def p_q_profit_with_actions(prof, profits, actions):
    plt.figure(figsize=(14, 8))
    plt.plot(prof, label="Policy Profit", color="blue", linewidth=2)
    plt.plot(profits, label="Qlearning Profit", color="green", linewidth=2)
    for i, taken_action in enumerate(actions):
        plt.text(i, profits[i] + 50, taken_action, fontsize=10, rotation=90, color="black") 
    plt.title("Profit over Policy with Qlearning Actions")
    plt.xlabel("Time")
    plt.ylabel("Profit")
    plt.legend()
    plt.grid(alpha=0.8)
    plt.tight_layout(rect=[0, 0.05, 1, 1]) 
    plt.show()


riders_drivers_comp(num_of_riders, num_of_drivers)
p_q_profit_with_actions(p_profit, qprofit_with_taken_actions, taken_actions)
