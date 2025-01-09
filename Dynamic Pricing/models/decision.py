from models.state import State
from models.policy import Policy
from models.objective import Objective
from models.qlearning import QLearning
        

class Decision:
    def __init__(self, state, qlearning):
        
        self.state = state
        self.policy = Policy(state)
        self.qlearning = qlearning
        
    def decision_making(self):
        """
        we are calculting the fare and profit based on policy and qlearning
        """
        p_fare = self.policy.apply_policy()

        # getting action based on algorithm and calculate fare of algo
        currently_state = self.state.get_state()
        action_from_ql = self.qlearning.get_the_action(currently_state)
        if action_from_ql == "increase":
            ql_fare = self.state.current_fare * 1.3
        elif action_from_ql == "decrease":
            ql_fare = self.state.current_fare * 0.8
        else: 
            ql_fare = self.state.current_fare

        ql_fare = round(ql_fare, 2)

        num_of_rides_comp = min(self.state.riders, self.state.drivers)
        
        objective = Objective(self.state)
        p_profit = objective.calculate_profit(num_of_rides_comp)
        ql_profit = (ql_fare * num_of_rides_comp) - (num_of_rides_comp * 5) # base cost / ride is 5

        
        print(f"State: {currently_state}")
        print(f"Weather: {self.state.weather}, Event: {self.state.event}")
        print(f"Policy Fare: ${p_fare}, Policy Profit: ${p_profit}")
        print(f"Q-Learning Fare: ${ql_fare}, Q-Learning Profit: ${ql_profit}")

        return {
            "policy_fare": p_fare,
            "qlearning_fare": ql_fare,
            "policy_profit": p_profit,
            "qlearning_profit": ql_profit,
            "qlearning_action": action_from_ql
        }


