import random

class QLearning:
    def __init__(self, states, actions, alpha=0.1, gamma=0.9, epsilon=0.2):
       
        self.alpha = alpha 
        self.gamma = gamma 
        self.epsilon = epsilon
        self.q_table = {state: {action: 0 for action in actions} for state in states}

    def get_the_action(self, state):

        if random.random() < self.epsilon:
            print("Random action chosen.")
            return random.choice(list(self.q_table[state].keys()))
        else:
            print("Best action based on Q-values chosen.")
            return max(self.q_table[state], key=self.q_table[state].get)  

    def q_value_updation(self, state, action, reward, next_state):

        current_qvalue = self.q_table[state][action]
        max_next_qvalue = max(self.q_table[next_state].values())
        new_qvalue = current_qvalue + self.alpha * (reward + self.gamma * max_next_qvalue - current_qvalue)
        self.q_table[state][action] = new_qvalue

        print(f"Updated Q-value: State={state}, Action={action}, Reward={reward}, Next State={next_state}, New Q-value={new_qvalue}")
        print("")
