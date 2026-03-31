import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self):
        self.distance_traveled += self.current_speed

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-15, 15))
            car.drive()

    def print_status(self):
        print(f"\n{'Biển số':<10} | {'Tốc độ':<8} | {'Quãng đường':<12}")
        print("-" * 35)
        for car in self.cars:
            print(f"{car.registration_number:<10} | {car.current_speed:<8} | {car.distance_traveled:<12.1f} km")

    def race_finished(self):
        for car in self.cars:
            if car.distance_traveled >= self.distance:
                return True
        return False

if __name__ == "__main__":
    list_of_cars = []
    for i in range(1, 11):
        list_of_cars.append(Car(f"ABC-{i}", random.randint(100, 200)))

    race = Race("Grand Demolition Derby", 8000, list_of_cars)

    hours = 0
    while not race.race_finished():
        race.hour_passes()
        hours += 1
        
        if hours % 10 == 0:
            print(f"\n--- Thời điểm: {hours} giờ ---")
            race.print_status()

    print(f"\n=== CUỘC ĐUA KẾT THÚC SAU {hours} GIỜ ===")
    race.print_status()