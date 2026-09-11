from abc import ABC, abstractmethod



class Vehicle(ABC):

    def __init__(self, vehicle_id: str, model: str, base_rate: float):
        self.__vehicle_id = vehicle_id
        self.__model = model
        self.base_rate = base_rate

    
    @property
    def vehicle_id(self):
        return self.__vehicle_id

    
    @property
    def model(self):
        return self.__model

    
    @property
    def base_rate(self):
        return self.__base_rate

    
    @base_rate.setter
    def base_rate(self, rate):
        if rate <= 0:
            raise ValueError("Base rate must be greater than 0.")
        self.__base_rate = float(rate)

    
    @abstractmethod
    def calculate_rental_cost(self, days: int) -> float:
        pass

    @abstractmethod
    def display_details(self) -> None:
        pass



class Car(Vehicle):

    def __init__(self, vehicle_id: str, model: str,
                 base_rate: float, num_doors: int,
                 luxury_fee: float = 0.0):

        super().__init__(vehicle_id, model, base_rate)

        self.num_doors = num_doors
        self.luxury_fee = luxury_fee

    
    def calculate_rental_cost(self, days: int) -> float:
        return (self.base_rate * days) + self.luxury_fee

    
    def display_details(self) -> None:
        print("Vehicle Type : Car")
        print("Vehicle ID   :", self.vehicle_id)
        print("Model        :", self.model)
        print("Base Rate    :", self.base_rate)
        print("Doors        :", self.num_doors)
        print("Luxury Fee   :", self.luxury_fee)



class Bike(Vehicle):

    def __init__(self, vehicle_id: str, model: str,
                 base_rate: float, engine_capacity: int):

        super().__init__(vehicle_id, model, base_rate)

        self.engine_capacity = engine_capacity

    
    def calculate_rental_cost(self, days: int) -> float:

        cost = self.base_rate * days

        
        if days > 5:
            cost = cost * 0.90

        return cost

    
    def display_details(self) -> None:
        print("Vehicle Type : Bike")
        print("Vehicle ID   :", self.vehicle_id)
        print("Model        :", self.model)
        print("Base Rate    :", self.base_rate)
        print("Engine CC    :", self.engine_capacity)



car1 = Car("C101", "Toyota Camry", 2500, 4, 1000)
car2 = Car("C102", "Honda City", 2000, 4)

bike1 = Bike("B101", "Royal Enfield Classic 350", 1000, 350)
bike2 = Bike("B102", "Yamaha MT-15", 800, 155)



fleet = [car1, car2, bike1, bike2]



days = 7

print("========== VEHICLE RENTAL SYSTEM ==========")


for vehicle in fleet:
    print("\n--------------------------------------------")


    vehicle.display_details()

    
    cost = vehicle.calculate_rental_cost(days)

    print("Rental Duration:", days, "days")
    print("Total Rental Cost: ₹", cost)

print("--------------------------------------------")
