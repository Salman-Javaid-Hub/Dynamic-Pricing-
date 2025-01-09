class Objective:
    def __init__(self, state):
        
        self.state = state

    def calculate_profit(self, rides_done):
    
        revenue = self.state.current_fare * rides_done

        cost_per_ride = 5
        weather_cost = self.state.w_cost
        event_cost = self.state.e_cost

        cpr_with_exogenous = cost_per_ride * weather_cost * event_cost #cpr = cost per ride
        overall_cost = cpr_with_exogenous * rides_done

        profit = revenue - overall_cost
        return round(profit, 2)
        

    def calculate_reward(self, profit):
       
        if profit > 500:
            return profit * 1.2
        elif profit > 50:
            return profit 
        else:
            return profit * 0.5 #penalty in case drops the profit

