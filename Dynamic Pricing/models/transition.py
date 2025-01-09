from models.objective import Objective

class Transition:
    def __init__(self, state, qlearning):
       
        self.state = state
        self.qlearning = qlearning

    def trans_action(self, action):
        
        objective = Objective(self.state)
        previous_state = self.state.get_state()

        if action == "increase":
            self.state.riders = max(0, self.state.riders - 4) 
        elif action == "decrease":
            self.state.riders = self.state.riders + 2 

        #change of state hapens, so calculate fare on based of state changed
        self.state.state_updation()

        rides_done = min(self.state.riders, self.state.drivers)
        profit = objective.calculate_profit(rides_done)
        reward = objective.calculate_reward(profit)

        # qvalue will be updated after state changed
        next_state_key = self.state.get_state()
        self.qlearning.q_value_updation(previous_state, action, reward, next_state_key)

        return self.state