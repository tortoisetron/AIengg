class Car:
    total_cars = 0
    def __init__(self,model,brand):
        self.model = model
        self.brand = brand
        Car.total_cars += 1
    
    def get_brand(self):
        return self.brand

class ElectricCar(Car):
    def __init__(self,model,brand,battery_size):
        super().__init__(model,brand)
        self.battery_size = battery_size

# ecar = ElectricCar("Toyota", "Tesla", 100)
car = Car("Honda", "Civic")
print(car.total_cars)
print(Car.total_cars)
# print(cars.brand)
# print(cars.battery_size)
