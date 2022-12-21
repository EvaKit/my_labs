class Rocket():
    def __init__(self, total_weight, amount_of_fuel, engine_status):      
        self.total_weight = total_weight
        self.amount_of_fuel = amount_of_fuel
        self.engine_status = engine_status
    def spend_fuel(self, count):              
        self.amount_of_fuel -= count           
        self.total_weight -= count             
        if self.amount_of_fuel <= 0:
            self.amount_of_fuel = 0
            self.engine_status = False
            return False
        elif self.amount_of_fuel > 0:
            self.engine_status = True
            return True
    def get_fuel_level(self):                                       
        return f'Топливо: {self.amount_of_fuel}'
    def get_total_weight(self):                                     
        return f'Общая масса: {self.total_weight}'
    def get_is_engine_running(self):                                
        return f'Состояние двигателя: {self.engine_status}'

def main():
    Adam_Smith = Rocket(12000, 5000, True)
    while Adam_Smith.amount_of_fuel > 0:
        Adam_Smith.spend_fuel(500)
        print(Adam_Smith.get_fuel_level(), end='; ')
        print(Adam_Smith.get_total_weight(), end='; ')
        print(Adam_Smith.get_is_engine_running())
main()
