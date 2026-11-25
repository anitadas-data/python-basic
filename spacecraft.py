class spacecraft:
    def __init__(self, name, modle, mass, max_speed, fuel_capacity, crew_capacity, year):
         self.name = name
         self.modle = modle
         self.mass = mass
         self.max_speed = max_speed
         self.fuel_capacity = fuel_capacity
         self.crew_capacity = crew_capacity
         self.year = year
    def start(self):
         print("spacecraft started")

    def stop(self):
         print("spacecraft stoped")

    def accelerate(self):
         print("spacecraft accelerating")

    def refuel(self):
         print("spacecraft is refueling")

    def display_specs(self):
        print("Name:", self.name)
        print("Model:", self.model)
        print("Mass:", self.mass)
        print("Max Speed:", self.max_speed)
        print("Fuel Capacity:", self.fuel_capacity)
        print("Crew Capacity:", self.crew_capacity)
        print("Year:", self.year)     
    @staticmethod
    def calculate_travel_time(distance,speed):
         return distance/speed
    
class cargoShip(spacecraft):
    def __init__(self, name, model, mass, max_speed,fuel_capacity, crew_capacity, year,cargo_capacity, current_cargo, cargo_type):
        super().__init__(name, model, mass, max_speed,fuel_capacity, crew_capacity, year)
        self.cargo_capacity = cargo_capacity
        self.current_cargo = current_cargo
        self.cargo_type = cargo_type

    def load_cargo(self):
        print("cargo loaded")

    def unload_cargo(self):
        print("cargo unloaded")

    def display_cargo_status(self):
        print("Cargo Capacity:", self.cargo_capacity)
        print("Current Cargo:", self.current_cargo)
        print("Cargo Type:", self.cargo_type)

    def accelerate(self):
        print("CargoShip accelerates slowly and gently")
class fighterShip(spacecraft):
    def __init__(self, name, model, mass, max_speed, fuel_capacity, crew_capacity, year, weapons, shield_strength, missiles,
        maneuverability):
        super().__init__(name, model, mass, max_speed,fuel_capacity, crew_capacity, year)
        self.weapons = weapons
        self.shield_strength = shield_strength
        self.missiles = missiles
        self.maneuverability = maneuverability
    def attack(self):
        print("FighterShip attacks")

    def launch_missile(self):
        print("Missile launched")

    def activate_shield(self):
        print("Shield activated")

    def accelerate(self):
        print("FighterShip has responsive acceleration")


class explorationShip(spacecraft):
    def __init__(self, name, model, mass, max_speed, fuel_capacity, crew_capacity, year, ship_range, sensor_range,
                  research_capacity, life_support):
        super().__init__(name, model, mass, max_speed,fuel_capacity, crew_capacity, year)
        self.ship_range = ship_range
        self.sensor_range = sensor_range
        self.research_capacity = research_capacity
        self.life_support = life_support 
    def scan_space(self):
        print("Scanning space")

    def collect_data(self):
        print("Collecting data")

    def calculate_mission_range(self):
        print("Mission range:", self.ship_range)

    def accelerate(self):
        print("ExplorationShip accelerates gently")


class Interceptor(fighterShip):

    def __init__(self, name, model, mass, max_speed,fuel_capacity, crew_capacity, year,weapons, shield_strength, missiles,
                 maneuverability,targeting_range, boost_power,interception_range):

        super().__init__(
            name, model, mass, max_speed,
            fuel_capacity, crew_capacity, year,
            weapons, shield_strength, missiles,
            maneuverability
        )

        self.targeting_range = targeting_range
        self.boost_power = boost_power
        self.interception_range = interception_range

    def lock_target(self):
        print("Target locked")

    def intercept(self):
        print("Interceptor is chasing the target")

    def activate_boost(self):
        print("Boost activated")

    def accelerate(self):
        print("Interceptor has high speed acceleration")

cargo = cargoShip("Cargo1", "C101", 5000, 800, 10000, 20, 2026, 3000, 1000, "Food")

fighter = fighterShip("Fighter1", "F101", 2000, 2500,5000, 2, 2026,"Laser", 100, 10, "High")

explorer = explorationShip("Explorer1", "E101", 3000, 1500,8000, 10, 2026, 50000, 10000, 500, "30 Days")

interceptor = Interceptor("Interceptor1", "I101", 1800, 3500,6000, 2, 2026,"Laser", 150, 10, "Very High",5000, 1000, 10000)
# Calling accelerate()
cargo.accelerate()
fighter.accelerate()
explorer.accelerate()
interceptor.accelerate()
# Static method
print(spacecraft.calculate_travel_time(1000, 100))  