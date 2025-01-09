from models.exogenous import Exogenous

class State:
    def __init__(self, riders, drivers, base_fare=10):
        
        self.riders = riders
        self.drivers = drivers
        self.base_fare = base_fare
        self.exogenous = Exogenous()

        self.weather, self.w_cost = self.exogenous.weather_calculation()
        self.event, self.e_cost = self.exogenous.event_calculation()

        #this is initial fare
        self.current_fare = self.fare_calculation()

    def fare_calculation(self):
        
        fare_factor = 1.3 if self.riders > self.drivers else 0.8
        initial_fare = self.base_fare * fare_factor * self.w_cost * self.e_cost
        return round(initial_fare, 2)

    def state_updation(self, riders=None, drivers=None):
       #this function will be used when transition function alters the current state
        if riders is not None:
            self.riders = riders
        if drivers is not None:
            self.drivers = drivers

        #fare will be calculated again after updating state
        self.weather, self.w_cost = self.exogenous.weather_calculation()
        self.event, self.e_cost = self.exogenous.event_calculation()
        self.current_fare = self.fare_calculation()

    def get_state(self):
        riders_category = "high" if self.riders > self.drivers else "low"
        drivers_category = "high" if self.drivers > self.riders else "low"
        return f"{riders_category}_{drivers_category}"