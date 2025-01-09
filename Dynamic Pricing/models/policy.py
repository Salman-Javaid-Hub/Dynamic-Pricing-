class Policy:
    def __init__(self, state):
        self.state = state

    def apply_policy(self):
        
        if self.state.riders > self.state.drivers:
            fare_factor = 1.3 
        elif self.state.riders < self.state.drivers:
            fare_factor = 0.8
        else:
            fare_factor = 1.0

        self.state.current_fare = self.state.base_fare * fare_factor * self.state.w_cost * self.state.e_cost
        self.state.current_fare = round(self.state.current_fare, 2)

        return self.state.current_fare

