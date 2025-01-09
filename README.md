# Dynamic Pricing for Ridesharing

## Overview
This project implements a Q-learning-based dynamic pricing system for ride-sharing platforms. It adjusts fares in real-time based on demand, supply, and external factors (e.g., weather, events), aiming to maximize profitability and user satisfaction.

## Features

Real-time dynamic fare adjustment.
Incorporates exogenous factors like weather and events.
Reinforcement learning for adaptive and optimized decision-making.
Outperforms traditional policy-based pricing methods.
Balances supply-demand dynamics for fair and efficient operations.
## Repository Structure

main.py: Entry point for executing the model and visualizing results.
data/: Contains the dataset rides.csv for training and evaluation.
models/: Modular components for the system:
state.py: Manages system state.
policy.py: Implements policy-based pricing.
qlearning.py: Q-learning algorithm for fare optimization.
decision.py: Compares pricing strategies.
objective.py: Calculates profit and rewards.
transition.py: Handles state transitions and updates Q-values.

## Installation

Clone this repository:
bash
Copy code
git clone https://github.com/your-username/dynamic-pricing.git  

## Usage

Place your data file in the data/ folder.
Run main.py to execute the model and visualize results:
bash
Copy code
python main.py  

## Methodology

Sequential decision framework with state and action variables.
Q-learning with epsilon-greedy strategy for action selection.
Real-time adaptation to changing supply-demand and external conditions.

## Results

Q-learning demonstrated higher profitability and adaptability than traditional pricing.
Balanced supply-demand dynamics with better user satisfaction.

## Future Improvements

Integration of real-time data.
Enhanced reward mechanism for better decision-making.
Pilot testing in real-world scenarios.

This README will help users understand the project, navigate the repository, and run the code effectively. Let me know if you'd like more details added!
